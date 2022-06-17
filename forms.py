from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, InputRequired, Email, Length
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField(label='Email', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password', validators=[Length(min=8, max=30,
                             message="Your password should contain a minimum of 8 and a maximum of 20 characters.")])
    submit = SubmitField(label="Sign Up")


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password')
    submit = SubmitField(label="Log in")


class CommentForm(FlaskForm):
    body = StringField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
