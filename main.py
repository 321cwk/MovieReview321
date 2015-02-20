import jinja2
import webapp2
import urllib2
import json
import os
 
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),
    extensions={'jinja2.ext.autoescape'})


class MainPage(webapp2.RequestHandler):
    def get(self):
        title_to_search = 'matrix'
        omdb_api_url = "http://www.omdbapi.com/?t=" + title_to_search + '&y=&plot=short&r=json'
        response = urllib2.urlopen(omdb_api_url).read()
        data = json.loads(response.decode('utf8'))
        
        film = data['Title'] + '  ' + data['Year'] + '  ' + data['Plot']
        
        template = JINJA_ENVIRONMENT.get_template('form.html')
        template_values = {
            'film': film,
        }
        self.response.write(template.render(template_values))
        
    def post(self):
        searchtitle = self.request.get('t')
        searchyear = self.request.get('y')
        searchplot = self.request.get('plot')
        title_to_search = searchtitle
        omdb_api_url = "http://www.omdbapi.com/?t=" + title_to_search + '&y=&plot=short&r=json'
        response = urllib2.urlopen(omdb_api_url).read()
        data = json.loads(response.decode('utf8'))
        
        film = data['Title'] + '  ' + data['Year'] + '  ' + data['Plot']
        
        template = JINJA_ENVIRONMENT.get_template('form.html')
        template_values = {
            'film': film,
        }
        self.response.write(template.render(template_values))
        
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/movie', MainPage),
], debug=True)
