import SimpleHTTPServer
import SocketServer

PORT = 8000
server_address = ("", PORT)
PUBLIC_RESOURCE_PREFIX = '/'
PUBLIC_DIRECTORY = './dist2/'

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if self.path.startswith(PUBLIC_RESOURCE_PREFIX):
            if self.path == PUBLIC_RESOURCE_PREFIX or self.path == PUBLIC_RESOURCE_PREFIX + '/':
                return PUBLIC_DIRECTORY + 'index.html'
            else:
                return PUBLIC_DIRECTORY + path[len(PUBLIC_RESOURCE_PREFIX):]
        else:
            return SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self, path)


httpd = SocketServer.TCPServer(server_address, MyRequestHandler)

print "serving at port %s" % PORT
httpd.serve_forever()
