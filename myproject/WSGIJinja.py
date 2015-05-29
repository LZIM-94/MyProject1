
import selector
from jinja2 import Environment,FileSystemLoader


aboutme_ref = """<a href="aboutme/aboutme.html">aboutme.html</a>"""
index_ref = """<a href="../index.html">index.html</a>"""

succes = '200 OK'
headers = [('Content-Type','text/html; charset=UTF-8')]

class Base(object):

    def __init__(self,environ,start_response,link,template):
        self.env = environ
        self.start_response = start_response
        self.teplates  = Environment(loader=FileSystemLoader('templates'))
        self.template = template
        self.link = link

    def __iter__(self):
        self.start_response(succes,headers)
        template = self.teplates.get_template(self.template)
        yield template.render(link=self.link)
             
class Index(Base):
    def __init__(self,environ,start_response):
        Base.__init__(self, environ, start_response, aboutme_ref, "index.html")

class AboutMe(Base):
    def __init__(self,environ,start_responce):
        Base.__init__(self,environ,start_responce,index_ref,"aboutme.html")

def init():
    sel =  selector.Selector()
    sel.add("/index.html",GET=Index)
    sel.add("/aboutme/aboutme.html",GET=AboutMe)
    return sel


if __name__=="__main__":
    from paste.httpserver import serve
    app = init()
    serve( app, host='localhost', port=8000)
