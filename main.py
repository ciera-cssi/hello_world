import webapp2
import logging

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('In hello handler')
        self.response.write('<h2>Hello CSSI!</h2>')
        self.response.write('<i>I hope you are having a fun week!</i>')
        self.response.write('<ul>')
        self.response.write('<li>Robot controller')
        self.response.write('<li>pterodactyl')
        self.response.write('<li>Evolution')
        self.response.write('</ul>')
        
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
