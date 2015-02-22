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
import webapp2
from common_files import helper_functions
from render_forms.all_forms import index_page,bdayform,rot13form,signupform

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(index_page)

class ValidBdayHandler(webapp2.RequestHandler):
	def write_form(self, errors="", month="", day="", year=""):
		self.response.out.write(bdayform %{"errors":helper_functions.escape_html(errors),
										"months":helper_functions.escape_html(month),
										"day": helper_functions.escape_html(day),
										"year":helper_functions.escape_html(year)})

	def get(self):
		self.write_form()

	def post(self):
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')

		month = helper_functions.valid_month(user_month)
		day = helper_functions.valid_day(user_day)
		year = helper_functions.valid_year(user_year)

		if month and day and year:
			self.redirect("/thanks")
		else:
			self.write_form("INVALID!!",user_month,user_day,user_year)

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("That looks like a valid day")

# class TestHandler(webapp2.RequestHandler):
# 	def post(self):
# 		# q = self.request.get("q")
# 		# self.response.out.write(q)

# 		self.response.headers['Content-Type'] = 'text/plain'
# 		self.response.write(self.request)
# 		self.response.write(self.request.headers)

from rot13 import rot13_helper
class RotThirteenHandler(webapp2.RequestHandler):
	def write_form(self, text=""):
		self.response.out.write(rot13form %{"output":helper_functions.escape_html(text)})

	def get(self):
		self.write_form()

	def post(self):
		text = self.request.get('text')
		if text:
			# return_text = rot13_helper.converted_text(text)
			return_text = text.encode('rot13')
		else:
			return_text = ''
		self.write_form(return_text)


class SignUpHandler(webapp2.RequestHandler):
	def write_form(self, errors={}, username="", email = ""):
		self.response.out.write(signupform %{"username_errors":helper_functions.escape_html(errors.get('username','')),
										"password_errors":helper_functions.escape_html(errors.get('password','')),
										"verify_errors":helper_functions.escape_html(errors.get('verify_password','')),
										"email_errors":helper_functions.escape_html(errors.get('email','')),
										"username":helper_functions.escape_html(username),
										"email": helper_functions.escape_html(email),
										"password":"",
										"verify":""
										})

	def get(self):
		self.write_form()

	def post(self):
		errors = {}
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify_password = self.request.get('verify')
		user_email = self.request.get('email')

		username = helper_functions.valid_username(user_username)
		

		if user_password == "" or not helper_functions.valid_password(user_password):
			errors['password'] = "That's not a valid password"

		if user_password != user_verify_password:
			errors['verify_password'] = "Your Passwords do not match"

		if user_email:
			email = helper_functions.valid_email(user_email)
			if not email:
				errors['email'] = "That's not a valid email"

		if not username:
			errors['username'] = "That's not a valid username"

		if errors == {}:
			self.redirect("/welcome?username=" + user_username)
		else:
			self.write_form(errors,user_username,user_email)

class WelcomeForSignUpHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get('username')
		if helper_functions.valid_username(username):
			self.response.out.write("Welcome, {}".format(username))
		else:
			self.redirect('/signup')

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/thanks',ThanksHandler),
	('/check_bday',ValidBdayHandler),
	('/rot13',RotThirteenHandler),
	('/signup',SignUpHandler),
	('/welcome',WelcomeForSignUpHandler)
	# ('/testform', TestHandler)
], debug=True)
