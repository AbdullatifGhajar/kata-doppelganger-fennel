from ..mail_sender import MailSender

class HttpClient:
    def post(self, url, request):
        self.posted_url = url
        self.posted_request = request
        
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
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    pass
