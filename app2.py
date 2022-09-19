# import packages 
from flask import Flask, render_template
import requests 

app = Flask(__name__)

# first page
@app.route('/')
def home_page():
    return render_template('homepage.html')

# second page
@app.route('/other')
def other_page():
    return render_template('other.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
