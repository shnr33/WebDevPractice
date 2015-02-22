import cgi
import logging
def escape_html(str):
	# str.replace("&","&amp;")
	# str.replace("<","&lt;")
	# str.replace(">","&gt;")
	# str.replace('"',"&quot;")
	# return str
	return cgi.escape(str, quote=True)

def valid_month(month):
	months = ['January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December']

	month_cap = month.capitalize()
	if month_cap in months:
		return month_cap

def valid_day(day):
	if day and day.isdigit():
		if int(day) in range(1,32):
				return int(day)

def valid_year(year):
	if year and year.isdigit():
		if int(year) > 1900 and int(year) <=2020:
			return int(year)

import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
	return USER_RE.match(username)

def valid_password(password):
	return PWD_RE.match(password)

def valid_email(email):
	return EMAIL_RE.match(email)