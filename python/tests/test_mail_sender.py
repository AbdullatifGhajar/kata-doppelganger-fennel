from unittest.mock import MagicMock
from ..mail_sender import MailSender, Request


class Response:
    def __init__(self, code):
        self.code = code


class HttpClient:
    def post(self, url, request):
        self.posted_url = url
        self.posted_request = request

        return Response(200)


class FailingHttpClient(HttpClient):
    def post(self, url, request):
        super().post(url, request)

        return Response(503)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


def test_send_v1():
    http_client = MagicMock()
    http_client.post = MagicMock(return_value=None)

    mail_sender = MailSender(http_client)

    user = MagicMock(name="Hugo", email="hugo@efrei.net")
    message = "Hello Hugo!"

    mail_sender.send_v1(user, message)

    http_client.post.assert_called_once_with(
        mail_sender.base_url,
        Request(user.name, user.email, "New notification", message),
    )


def test_send_v2():
    mail_sender = MailSender(FailingHttpClient())
    user = User("Hugo", "hugo@efrei.net")
    message = "Hello Hugo!"

    mail_sender.send_v2(user, message)

    assert isinstance(mail_sender.http_client.posted_request, Request)
