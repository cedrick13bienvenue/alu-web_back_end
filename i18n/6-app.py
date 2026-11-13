#!/usr/bin/env python3
"""Module that prioritizes a logged-in user's locale preference."""
from typing import Dict, Optional
from flask import Flask, g, render_template, request
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Babel configuration for the app's supported languages and defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Optional[Dict]:
    """Return the user dictionary for the login_as URL parameter, or None."""
    login_id = request.args.get("login_as")
    if login_id is None:
        return None
    try:
        return users.get(int(login_id))
    except ValueError:
        return None


@app.before_request
def before_request() -> None:
    """Set the logged-in user, if any, as a global on flask.g.user."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the locale from URL params, user settings, or headers."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Render the index page."""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
