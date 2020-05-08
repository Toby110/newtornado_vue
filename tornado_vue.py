#!/usr/bin/python
#coding=utf-8
import tornado.web
import tornado.ioloop
import asyncio
import sqlite3
import json

settings={
    "template_path":"template",
    "static_path":"static",
    "debug":"true",
}

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        db=sqlite3.connect('template/words.db')
        db.row_factory=sqlite3.Row
        cur=db.cursor()
        sql='select * from whlxx'
        data=cur.execute(sql).fetchall()
        data=[dict(row) for row in data]
        self.write(json.dumps(data))

def make_app():
    return tornado.web.Application([
        (r'/',IndexHandler),
        (r'/login',LoginHandler)
    ],**settings)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app=make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
    