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
        template = jinja_env.get_template('templates/hello.html')
        self.response.write(template.render())

class AllStudentsPage(webapp2.RequestHandler):
    def get(self):
        cssi = [
            {"name":"Asia", "university": "SDSU"},
            {"name":"Taylore", "university": "Stanford"},
            {"name":"Brian", "university": "UT%20Austin"},
            {"name":"Zach", "university": "UC%20Irvine"},
        ]
        template_vars = {
            "cssi" : cssi,
        }
        template = jinja_env.get_template('templates/all_students.html')
        self.response.write(template.render(template_vars))

class StudentPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'name': self.request.get('student_name'),
            'university': self.request.get('university')
        }
        template = jinja_env.get_template('templates/student.html')
        self.response.write(template.render(template_vars))

class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Shhh! This is the secret entrance!')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is the about page!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/all_students', AllStudentsPage),
    ('/student', StudentPage),
    ('/secretentrance', SecretPage),
    ('/about', AboutPage),
], debug=True)
