
# Abby Careers — Job Application Website

## Overview
A small job listing and application website built with Flask, HTML/CSS, and JavaScript.

## Features
- View job listings
- Apply to a job (prefilled form via query params)
- Simple server-side form handling

## Run locally
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt   # flask
4. flask run
5. Open http://127.0.0.1:5000/

## Notes
- Add persistent storage (SQLite) for production.
- Secure file uploads and enable HTTPS when deploying.
