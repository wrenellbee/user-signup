# Unit 2 Large Assignment #3: Sign Up Form

# Note to self: Maybe I should turn some of these functions inside signup() into their OWN FUNCTIONS

# Import needed libraries
from flask import Flask, request, redirect, render_template
import cgi

# Set up Flask and debugging
app = Flask(__name__)
app.config['DEBUG'] = True

# Render the home page
@app.route("/")
def index():
    return render_template('signup-form.html', title="Sign Up")

# Setup the signup function
@app.route("/", methods=['POST'])
def signup():

    # Pull in the data for your four variables
    username = request.form['username']
    password = request.form['password']
    verifypw = request.form['verifypw']
    email = request.form['email']

    # Initialize empty strings for the errors
    username_error = ""
    password_error = ""
    verifypw_error = ""
    email_error = ""

    # Validate content present in username field
    if username == "":
        username_error = cgi.escape("Please enter a username.")
        username = username
        password = ""
        verifypw = ""
        email = email
        return render_template('signup-form.html', title="Sign Up",
            username=username,
            password=password,
            verifypw=verifypw,
            email=email,
            username_error=username_error,
            password_error=password_error,
            verifypw_error=verifypw_error,
            email_error=email_error)

    # Validate username length
    if len(username) < 3 or len(username) > 20:
        username_error = cgi.escape("Your username must be 3-20 characters.")
        username = username
        password = ""
        verifypw = ""
        email = email
        return render_template('signup-form.html', title="Sign Up",
            username=username,
            password=password,
            verifypw=verifypw,
            email=email,
            username_error=username_error,
            password_error=password_error,
            verifypw_error=verifypw_error,
            email_error=email_error)

    # Validate no spaces in username
    for character in username:
        if character == " ":
            username_error = cgi.escape("Your username may not contain spaces.")
            username = username
            password = ""
            verifypw = ""
            email = email
            return render_template('signup-form.html', title="Sign Up",
                username=username,
                password=password,
                verifypw=verifypw,
                email=email,
                username_error=username_error,
                password_error=password_error,
                verifypw_error=verifypw_error,
                email_error=email_error)

    # Validate content present in password field
    if password == "":
        password_error = cgi.escape("Please enter a password.")
        username = username
        password = ""
        verifypw = ""
        email = email
        return render_template('signup-form.html', title="Sign Up",
            username=username,
            password=password,
            verifypw=verifypw,
            email=email,
            username_error=username_error,
            password_error=password_error,
            verifypw_error=verifypw_error,
            email_error=email_error)

    # Validate password length
    if len(password) < 3 or len(password) > 20:
        password_error = cgi.escape("Your password must be 3-20 characters.")
        username = username
        password = ""
        verifypw = ""
        email = email
        return render_template('signup-form.html', title="Sign Up",
            username=username,
            password=password,
            verifypw=verifypw,
            email=email,
            username_error=username_error,
            password_error=password_error,
            verifypw_error=verifypw_error,
            email_error=email_error)

    # Validate no spaces in password


#Run the app
app.run()
