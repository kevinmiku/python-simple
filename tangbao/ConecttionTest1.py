# coding=utf-8
#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import tornado.httpserver
class ServerHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        query = urllib.request.splitquery(path)
        print(query)
        self.send_header("Content-type","text/html")
        self.send_header("test","This is test")
        self.end_headers()
        buf = '''''<!DOCTYPE HTML> 
                        <html> 
                        <head><title>Get page</title></head> 
                        <body> 

                        <form action="post_page" method="post"> 
                          username: <input type="text" name="username" /><br /> 
                          password: <input type="text" name="password" /><br /> 
                          <input type="submit" value="POST" /> 
                        </form> 

                        </body> 
                        </html>'''
        #buf = bytes(buf,encoding="utf-8")
        self.wfile.write(buf)

    def do_POST(self):
        path = self.path
        print(path)
        datas = self.rfile.read(int(self.headers['content-length']))
        datas = urllib.request.unquote(datas).decode("utf-8",'ignore')

        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("test","This is test")
        self.end_headers()
        buf = '''''<!DOCTYPE HTML> 
        <html> 
            <head><title>Post page</title></head> 
            <body>Post Data:%s  <br />Path:%s</body> 
        </html>'''%(datas,self.path)
        self.wfile.write(buf)

def start_server(port):
    http_server = HTTPServer(('',int(port)),ServerHTTP)
    http_server.serve_forever()


if __name__ == '__main__':
    start_server(8000)