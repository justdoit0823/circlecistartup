# -*- coding: utf-8 -*-


from tornado import web
from tornado import httpserver
from tornado import ioloop


class HelloworldHandler(web.RequestHandler):

    def get(self):
        self.write('Hello world')

settings = {
    'handlers': [(r'/', HelloworldHandler)]
}

def main():

    app = web.Application(settings['handlers'])
    server = httpserver.HTTPServer(app)
    server.listen(7777)
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
