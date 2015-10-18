from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')  # excutues routes
def hello():
    print 'hello world'
    return "hello world"


@app.route('/about', methods=["POST"])
def about():
    firstname = request.form.get("first")
    lastname = request.form.get("last")
    print "about page"
    return render_template('index.html', first=firstname, last=lastname)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    name = request.values.get('name')
    email = request.values.get('email')
    message = request.values.get('message')
    return render_template('contact.html', name=name, email=email, message=message)

# to submit a form and then return the anwers from the from to the same route
# use two routes with the same route name one will render from template and the other one will display
# the form text that was entered after submiit button


@app.route('/returnform')
def my_form():
    return render_template('returnform.html')

# returns the text in the from to the same request


@app.route('/returnform', methods=["POST"])
def my_from():
    text = request.form['text']
    return text

#  TO RUN APPLICATION
#  tells py to run development web server, only if current .py file is running

if __name__ == "__main__":
    app.run(debug=True)
