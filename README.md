# URL Shortener using Flask

This is a simple URL shortening service implemented in Python using the Flask web framework. It allows users to input a long URL and generates a shorter version of that URL. When someone accesses the shortened URL, they are redirected to the original long URL.

## Code Explanation

### Libraries and Modules

- **json**: The `json` module is used for reading and writing data in JSON format. In this code, it is utilized to store and retrieve the mappings between short and long URLs in a JSON file.

- **random**: The `random` module is employed for generating random characters, which are used to create unique short URLs. It helps ensure that each generated short URL is distinct.

- **string**: The `string` module provides a collection of characters, including uppercase letters, lowercase letters, and digits. These characters are used to construct the random short URLs.

- **urllib.parse.quote**: The `urllib.parse.quote` function is used to properly encode URLs. This ensures that special characters in URLs are handled correctly, preventing issues when redirecting users to the original long URLs.

- **Flask**: Flask is a web framework for creating web applications in Python. It provides the necessary tools and functionality to build the URL shortening service. Routes are defined to handle URL shortening and redirection, and the application is run using Flask.

### Short URL Generation

```python
def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url
```
- The `generate_short_url` function generates a random short URL of a specified length (default is 6 characters). It utilizes characters from the `string` module (letters and digits) and the `random` module to create unique short URLs.

### Handling Root ("/") Route

```python
@app.route("/", methods=["GET", "POST"])
def index():
    # ...
}
```
### Redirecting to Original URL

This route function handles requests to access a shortened URL. It retrieves the original long URL associated with the provided short URL from the `shortened_urls` dictionary and redirects users to the original URL if found.

### Main Block

```python
if __name__ == "__main__":
    # ...
}
```

In the main block of the code:

- The code loads previously shortened URLs from a JSON file named "urls.json" using the `json` module. This allows the service to retain previously generated short URLs even after restarting the application.

- If the "urls.json" file doesn't exist (e.g., on the first run), an empty dictionary is used as the initial data storage for the shortened URLs.

- Finally, the Flask application is run in debug mode. Enabling debug mode makes the application accessible for testing and development, providing helpful error messages and auto-reloading when code changes are detected.
