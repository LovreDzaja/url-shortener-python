import json
import random
import string
from urllib.parse import quote

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
shortened_urls = {}

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()

        while short_url in shortened_urls:
            short_url = generate_short_url()

        shortened_urls[short_url] = long_url
        with open("urls.json", "w") as file:
            json.dump(shortened_urls, file)
        return f"Shortened URL: {request.url_root}{quote(short_url)}"  # Use quote to properly encode the URL
    return render_template("index.html")

@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    try:
        with open("urls.json", "r") as file:
            shortened_urls = json.load(file)
    except FileNotFoundError:
        shortened_urls = {}

    app.run(debug=True)