#For reference - to submit to a different handler
# form = """
# <form method="post" action="/testform">
# <input name="q">
# <input type="submit">
# </form>
# """

index_page = """
<center><h2> Welcome to my Web Dev Practice site </h2></center>
<center><h3> Following are few test items you can explore: </h3></center>
<center>
<ul>
	<li><a href="/check_bday">Check Valid Birthday</a></li>
	<li><a href="/rot13">ROT13 Encryption</a></li>
	<li><a href="/signup">Sign Up Form</a></li>
	<li><a href="/templates/ex1">Templates Ex-1</a></li>
	<li><a href="/templates/fizzbuzz">FizzBuzz Programming</a></li>
</ul>
</center>
"""

bdayform = """
<form method="post">
<h2>What is your Birthday?</h2>
	<label>Month
		<input type="text" name="month" value="%(months)s">
	</label>
	<label>Day
		<input type="text" name="day" value='%(day)s'>
	</label>
	<label>Year
		<input type="text" name="year" value='%(year)s'>
	</label>
<br>
<div style="color:red">%(errors)s</div>
<br/>
<input type="submit">
</form>
"""

rot13form = """
<form method="post">
<h2>Enter a Text to be ROT13 encrypted</h2>
<br/>
<textarea name="text" rows="10" cols="50">%(output)s</textarea><br/>
<input type="submit">
</form>
"""

signupform = """
<form method="post">
<h2>Signup</h2>
	<table>
	<tr>
	<td>Username</td>
	<td><input type="text" name="username" value='%(username)s'></td><td><label style="color:red">%(username_errors)s</label></td>
	</tr>
	<tr>
	<td>Password</td>
	<td><input type="password" name="password" value='%(password)s'></td><td><label style="color:red">%(password_errors)s</label></td>
	</tr>
	<tr>
	<td>Verify Password</td>
	<td><input type="password" name="verify" value='%(verify)s'></td><td><label style="color:red">%(verify_errors)s</td>
	</tr>
	<tr>
	<td>Email (Optional)</td>
	<td><input type="text" name="email" value='%(email)s'></td><td><label style="color:red">%(email_errors)s</label></td>
	</tr>
	</table>
<br/>
<input type="submit">
</form>
"""

form_html = """
<form>
<h2> Add a food </h2>
<input type = 'text' name='food'/>
%s
<button>Add</button>
</form>
"""

hidden_html =  """
<input type='hidden' value="%s">
"""

shopping_list_html = """
<br>
<br>

<h2> Shopping List </h2>

<ul>
%s
</ul>
"""

items_html = "<li>%s</li>"