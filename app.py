import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')

def home():

    data ={
        'name': 'Aditya More',
        'title': 'Python Developer & CS Student.',
        'about': 'I build cool stuff with Python',
        'skills': ['Python', 'C++', 'HTML/CSS', 'Flask', 'Linux'],
        'projects': [
            {
                'title': 'Portfolio Website',
                'desc': 'Personal site built with Flask and HTML/CSS',
                'tech': 'Python, Flask, HTML/CSS'
            },
            {
                'title': 'Weather App',
                'desc': 'Full stack weather app with Flask, live API data and secure key handling.',
                'tech': 'Python, Flask, JS, HTML/CSS',
                'live': 'https://weather-app-ghph.onrender.com/',
                'github': 'https://github.com/onionloop/weather-app'
            },

            {
                'title': 'TinyLink - URL Shortener',
                'desc': 'Full stack URL shortener built with Flask, secure ID generation and click analytics.',
                'tech': 'Python, Flask, SQLite, JS, HTML/CSS',
                'live': 'https://url-shortener-p9vd.onrender.com/',
                'github': 'https://github.com/onionloop/url-shortener'
            },
            {
                'title': 'Coming Soon',
                'desc': 'Next project loading soon...',
                'tech': 'Python, Flask, HTML/CSS'
            }
        ]
    
    }
    return render_template('index.html', **data)


@app.route('/contact', methods=['POST'])
def contact():
    
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"Message from {name} [{email}]: {message}")
    return '<h2> Message received! Go back <a href="/">Home</a></h2>'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
    