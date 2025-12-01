import smtplib
from flask import Flask, render_template, request
from post import Post
import os
from dotenv import load_dotenv
from datetime import datetime
from newsapi import NewsApiClient
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, length, DataRequired, Email, Length
from werkzeug.security import generate_password_hash


load_dotenv()

newsapi = NewsApiClient(api_key='f06d11a28cc14b21871a6db21d05a5f4')
# /v2/top-headlines
articles = newsapi.get_top_headlines()

#email
MY_EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


post_objects = []
for post in articles['articles']:
    post_obj = Post(post['source']['name'],
                    post['title'],
                    post['description'],
                    post['content'],
                    post['url'],
                    post['urlToImage'])

    post_objects.append(post_obj)



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class MyForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")


@app.route('/')
def get_all_posts():
    today = datetime.now().date()
    return render_template('index.html', all_posts=post_objects , today=today )


@app.route('/about')
def about():
    today = datetime.now().date()
    return render_template('about.html', today=today)


@app.route('/post/<name>')
def show_post(name):
    today = datetime.now().date()
    requested_post = None
    for blog_post in post_objects:
        if blog_post.name == name:
            requested_post = blog_post
    return render_template('post.html', post=requested_post, today=today)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    today = datetime.now().date()
    if request.method == "GET":
        return render_template("contact.html", today=today)
    else:
        name = request.form['name']
        email = request.form['email']
        phone_no = request.form['phone']
        msg = request.form['message']
        print(f"{name}\n{email}\n{phone_no}\n{msg}")
        send_email(name, email, phone_no, msg)
        return render_template('contact.html',submit=f"Successfully sent your message.{name}.", today=today)


def send_email(name, email, phone , msg):

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(MY_EMAIL, EMAIL_PASSWORD)
    s.sendmail(from_addr=email,
               to_addrs=MY_EMAIL,
               msg=f"Subject: Message Received from Blogy.io \n\n {name}\n{email}\n{phone}\n{msg}"
               )
    s.quit()



if __name__ == "__main__":
    app.run(debug=True)
