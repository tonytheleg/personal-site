from flask import Flask, render_template, send_file, current_app as app

app = Flask(__name__)

@app.route('/')
def serve_site():
    return render_template('index.html')

@app.route('/healthcheck')
def check_health():
    return "SITE IS UP"

@app.route('/resume')
def serve_pdf():
    return send_file('static/files/Antony-Natale-Resume.pdf', attachment_filename='Antony-Natale-Resume.pdf')    