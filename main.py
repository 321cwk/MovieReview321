#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja
import webapp2
import urllib2
import json
 
        
title_to_search = raw_input("Give me a title: ")

omdb_api_url = "http://www.omdbapi.com/?t=" + title_to_search + '&y=&plot=short&r=json'
 
response = urllib2.urlopen(omdb_api_url).read()
 
data = json.loads(response.decode('utf8')) 
 
print 'Title:  ' + data['Title']
print '-------------------'
print 'Year:  ' + data['Year']
print '-------------------'
print 'Plot:  ' + data['Plot']
print '-------------------'

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        
        
    def post(self):
        searchtitle = self.request.get('t')
        searchyear = self.request.get('y')
        searchplot = self.request.get('plot')
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
