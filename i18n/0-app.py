#!/usr/bin/env python3
"""Module that defines a basic Flask app with a single index route."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Render the index page."""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
