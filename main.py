import webapp2
import logging
# Step 1: Import jinja and os
import jinja2
import os

# Step 2: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('In hello handler')
        # Step 3: use the jinja environment to get our html
        template = jinja_env.get_template('hello.html')
        self.response.write(template.render())


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
