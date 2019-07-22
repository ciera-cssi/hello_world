import webapp2
import logging

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('In hello handler')
        self.response.write('Hello World!')

class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Shhh! This is the secret entrance!')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is the about page!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/secretentrance', SecretPage),
    ('/about', AboutPage),
], debug=True)
