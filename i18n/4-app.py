#!/usr/bin/env python3
"""Module that allows forcing a locale through a URL parameter."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Babel configuration for the app's supported languages and defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best locale, prioritizing the locale URL parameter."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Render the index page."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
