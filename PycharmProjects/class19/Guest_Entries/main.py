#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("hello.html", params=params)

    def post(self):
        result = self.request.get("text")
        result2 = self.request.get("name")
        result3 = self.request.get("email")


        msg = Message(text=result, name=result2, email=result3)
        msg.put()

        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("hello.html", params=params)

class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_detail.html", params=params)

class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_edit.html", params=params)

    def post(self, message_id):
        new_text = self.request.get("text")
        new_email = self.request.get("email")
        new_name = self.request.get("name")
        message = Message.get_by_id(int(message_id))
        message.text = new_text
        message.email = new_email
        message.name = new_name
        message.put()
        return self.redirect_to("entries")

class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_delete.html", params=params)

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        message.deleted = True
        message.put()
        return self.redirect_to("entries")




app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="entries"),
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler, name="message_edit"),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteMessageHandler, name="message_delete"),
], debug=True)
