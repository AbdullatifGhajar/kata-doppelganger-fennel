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
    mail_sender = MailSender(HttpClient())
    user = User("Hugo", "hugo@efrei.net")
    message = "Hello Hugo!"
    
    mail_sender.send_v1(user, message)
    
    assert mail_sender.http_client.posted_request.name == "Hugo"
    assert mail_sender.http_client.posted_request.email == "hugo@efrei.net"


def test_send_v2():
    mail_sender = MailSender(FailingHttpClient())
    user = User("Hugo", "hugo@efrei.net")
    message = "Hello Hugo!"
    
    mail_sender.send_v2(user, message)

    assert type(mail_sender.http_client.posted_request) == Request

    
    