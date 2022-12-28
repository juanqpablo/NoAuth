
class Request():
    def __init__(self, name, method, headers, body, url):
        self.name = name
        self.method = method
        self.headers = headers
        self.body = body
        self.url = url
