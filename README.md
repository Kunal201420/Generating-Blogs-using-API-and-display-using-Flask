# New Blog Web App

## Overview
This project is a Flask-based web application that automatically generates and displays blog posts by fetching top news headlines from the NewsAPI. It creates a dynamic blog site with routes for viewing all posts, individual posts, an about page, and a contact form with email notifications. The app uses a custom `Post` model to structure news data into blog-friendly format.

## Features
- Fetches real-time top headlines via NewsAPI and converts them into blog posts.
- Displays all posts on the home page with current date.
- Individual post view by post name/slug.
- Contact form with email submission using Gmail SMTP.
- Basic login form (placeholder for authentication).
- Responsive templates for index, post, about, and contact pages.

## Tech Stack
- **Backend**: Flask, Flask-WTF for forms, Werkzeug for password hashing.
- **Data**: NewsAPI for content, dotenv for environment variables.
- **Email**: smtplib for Gmail integration.
- **Model**: Custom `Post` class for blog post objects.
- **Templates**: Jinja2 HTML (index.html, post.html, about.html, contact.html).

## Quick Setup
1. Clone the repo and install dependencies:  
   `pip install flask flask-wtf newsapi-python python-dotenv werkzeug`
2. Create `.env` file with:
   (NewsAPI key is embedded by default)
3. Run `python main.py` – app starts on `http://127.0.0.1:5000/` in debug mode.


