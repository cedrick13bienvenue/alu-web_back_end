#!/usr/bin/env python3
"""Module that sets up a Flask app with basic Babel configuration."""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Babel configuration for the app's supported languages and defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Render the index page."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
