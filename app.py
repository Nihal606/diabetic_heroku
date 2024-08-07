from flask import Flask,render_template
from asyncio import protocols
app=Flask(__name__)


@app.route('/') #decorator
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/contact')
def contact():
    return "welcome to contact page"
@app.route('/cart')
def cart():
    return "welcome to cart page"
app.run(debug=True)

# http://127.0.0.1:5000
# http-hyper text transfer protocol, https-secured http
#127.0.0.1-local host
#5000-port number
#/ - route