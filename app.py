from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("BaseTemp.html")

@app.route('/FrontPage')
def FrontPage():
    return render_template('FrontPage.html')

@app.route('/Projects')
def projects():
    return render_template('Projects.html')

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/contact')
def contact():
    return 'The Contact Page'

@app.route('/faq')
def faq():
    return 'The Contact Page'

if __name__ == '__main__':
    app.run()