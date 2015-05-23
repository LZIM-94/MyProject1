from paste import reloader
from paste.httpserver import serve
import os


TOP = "<div class='top'>Middleware TOP</div>"
BOTTOM =  "<div class='botton'>Middleware BOTTOM</div>"

class MidWare(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        res = self.app(environ, start_response)[0]
        if res.find('<body>') >-1:
            headhtml,bodyhtml = res.split('<body>')
            data,endhtml = bodyhtml.split('</body>')
            data = '<body>'+ TOP + data + BOTTOM+'</body>'
            yield headhtml + data + endhtml
        else:
            yield TOP + res + BOTTOM


def app(environ, start_response):
    
    path = environ['PATH_INFO']
    file_path = '.' + path  
    if not os.path.isfile(file_path):
        file_path ='./index.html' 

    file_data = open(file_path,'r')
    file_content = file_data.read()

    file_data.close()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [file_content ]

	
app = MidWare(app)


if __name__ == '__main__':
    from paste import reloader
    from paste.httpserver import serve

    reloader.install()
    serve(app, host='127.0.0.1', port=8000)
