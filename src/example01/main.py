from google.appengine.ext import ndb
import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class Order(ndb.Model):
  crust = ndb.StringProperty(required=True)
  size = ndb.StringProperty(required=True)
  sauce = ndb.StringProperty(required=True)
  cheese = ndb.StringProperty(required=True)
  topings = ndb.StringProperty(required=True)


class MainHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/input_order.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('templates/output_order.html')
        crust_value = self.request.get('crust')
        size_value = self.request.get('size')
        sauce_value = self.request.get('sauce')
        cheese_value = self.request.get('cheese')
        topings_value = self.request.get('topings')
        pizza_order = {
          'crust_answer': crust_value,
          'size_answer': size_value,
          'sauce_answer': sauce_value,
          'cheese_answer': cheese_value,
          'topings_answer': topings_value }
        order_record = Order(crust=crust_value, size=size_value, sauce=sauce_value, cheese=cheese_value, topings=topings_value)
        order_record.put()
        self.response.write(template.render(pizza_order))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
