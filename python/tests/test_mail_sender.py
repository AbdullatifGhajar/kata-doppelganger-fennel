from unittest.mock import MagicMock

from ..mail_sender import MailSender, Request


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
    http_client = MagicMock()
    response = MagicMock(code=503)
    http_client.post = MagicMock(return_value=response)
    mail_sender = MailSender(http_client)

    user = MagicMock(name="Hugo", email="hugo@efrei.net")
    message = "Hello Hugo!"

    mail_sender.send_v2(user, message)

    last_call_args = http_client.post.call_args[0]

    assert isinstance(last_call_args[1], Request)
