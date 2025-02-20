from flask import Flask, redirect, url_for
import subprocess
import datetime
import os

app = Flask(__name__)

@app.route('/htop')
def htop_info():
    name = "Meruva Sanjay"
    username = os.getenv("USER", "mvsanjay")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Run top command
    top_output = subprocess.getoutput("top -b -n 1")

    # Format output
    response = f"Name: {name}\nUser: {username}\nServer Time (IST): {server_time}\n\nTOP output:\n{top_output}"
    return f"<pre>{response}</pre>"

@app.route("/")
def home():
    return redirect(url_for('htop_info'))  # Redirects '/' to '/htop'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
