from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True 

def valid_username(username):
    space = ' '
    if space in username:
        username_error = 'There is space in your username!'
        return False
    elif len(username)==0:
        username_error = 'Username cannot be empty!'
        return False
    else:
        return True

def valid_password(password):
    space = ' '
    if space in password:
        password_error = 'There is space in your password!'
        return False
    elif len(password)>20 or len(password)<3:
        password_error = 'Password is too long or too short!'
        return False
    else:
        return True

def valid_passwordconf(password, passwordconf):
    if password != passwordconf:
        passwordconf_error = 'Password and password confirmation do not match!'
        return False
    elif len(password)==0 or len(passwordconf)==0:
        return False
    else:
        return True

def valid_email(email):
    space = ' '
    if len(email)==0:
      return True
    else:
      if email.count('@')!=1 or email.count('.')!=1:
          email_error = "Invalid email form!"
          return False
      elif space in email:
          email_error = 'There is space in your email address!'
          return False
      elif len(email)>20 or len(email)<3:
          email_error = 'email is too long or too short!'
          return False
      else:
          return True


@app.route("/")
def index():
    template = jinja_env.get_template('base.html')
    return template.render()

@app.route("/welcome", methods=['POST'])
def validation():
    username=request.form['username']
    password=request.form['password']
    passwordconf=request.form['passwordconf']
    email=request.form['email']
    username_error = ' '
    password_error = ' '
    passwordconf_error = ' '
    email_error = ' '

    if valid_username(username) and valid_password(password) and valid_passwordconf(password, passwordconf) and valid_email(email):
        template = jinja_env.get_template('welcome.html')
        return template.render(username = username)
        
    else:
        if valid_username(username)==False:
            username_error='Invalid username!'
        if valid_password(password)==False:
            password_error='Invalid password!'
        if valid_passwordconf(password, passwordconf)==False:
            passwordconf_error='Password do not match!'
        if valid_email(email)==False:
            email_error='Invalid email!'

        template = jinja_env.get_template('base.html')
        return template.render(username_error=username_error, password_error=password_error, passwordconf_error=passwordconf_error, email_error=email_error)

#@app.route("/welcome", methods=['POST'])
#def welcome():
#    template = jinja_env.get_template('welcome.html')
#    return template.render(username = username)
app.run()