from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import URL, DataRequired

class BookmarkForm(Form):
    url = StringField('The URL for your bookmark:', validators=[URL(message='Sorry, Invalid URL.')])
    description = StringField('Add an optional description:')

    # Override validate and provide sensible default behaviour
    # for incomplete url and description
    def validate(self):
    #     if not self.url.data.startswith('http://') or\
    #         self.url.data.startswith('https://'):
    #         self.url.data = 'http://' + self.url.data
    #
         if not Form.validate(self):
             return False

         if not self.description.data:
             self.description.data = self.url.data

         return True

class LoginForm(Form):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')