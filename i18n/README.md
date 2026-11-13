# i18n

## Description
This project builds up a small Flask app that supports internationalized
(i18n) text and localized timestamps, using Flask-Babel: parametrized
templates, locale selection from the URL, request headers, or a mock
logged-in user's settings, and time zone inference with validation.

## Resources
- [Flask-Babel](https://python-babel.github.io/flask-babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](http://pytz.sourceforge.net/)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to parametrize Flask templates to display different languages
- How to infer the correct locale from URL parameters, user settings, or
  request headers
- How to localize timestamps

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- Code follows the `pycodestyle` style (version 2.5)
- The first line of all files is exactly `#!/usr/bin/env python3`
- All `*.py` files are executable
- All modules, classes, and functions are documented with real, explanatory docstrings
- All functions and coroutines are type-annotated

## Setup
```
pip3 install -r requirements.txt
```

Flask-Babel's `localeselector`/`timezoneselector` decorator API used here
was removed in Flask-Babel 3+, so this project pins Flask and Flask-Babel
to the last versions that support it (see `requirements.txt`).

## Tasks
| File | Description |
| --- | --- |
| `0-app.py` | A basic Flask app with a single `/` route |
| `1-app.py` | Babel setup: a `Config` class with supported languages, default locale, and timezone |
| `2-app.py` | `get_locale` - picks the best locale from the request's `Accept-Language` header |
| `3-app.py` | Parametrized templates using `_()`/`gettext`, with compiled `en`/`fr` translations |
| `4-app.py` | `get_locale` - can be forced via a `locale` URL parameter |
| `5-app.py` | A mock login system (`get_user`, `before_request`) and a translated welcome message |
| `6-app.py` | `get_locale` - priority order: URL parameter, user setting, request header, default |
| `7-app.py` | `get_timezone` - priority order: URL parameter, user setting, default; validated with `pytz` |

## Usage
```
python3 7-app.py
```

Then, with the server running:
```
curl http://127.0.0.1:5000/
curl 'http://127.0.0.1:5000/?locale=fr'
curl 'http://127.0.0.1:5000/?login_as=2'
curl 'http://127.0.0.1:5000/?login_as=1&timezone=Asia/Tokyo'
```

## Regenerating translations
After adding a new message ID to a template:
```
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
# fill in the new msgstr values in translations/{en,fr}/LC_MESSAGES/messages.po
pybabel compile -d translations
```
