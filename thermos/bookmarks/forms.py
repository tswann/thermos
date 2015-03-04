__author__ = 'thomassw'

from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.validators import URL, Regexp

class BookmarkForm(Form):
    url = StringField('The URL for your bookmark:', validators=[URL(message='Sorry, Invalid URL.')])
    description = StringField('Add an optional description:')
    tags = StringField('Tags', validators=[Regexp(r'^[a-zA-Z0-9, ]*$',
                                                  message="Tags can only contain letters and numbers")])

    # Override validate and provide sensible default behaviour
    # for incomplete url and description
    def validate(self):
        if not self.url.data.startswith("http://") or\
         self.url.data.startswith("https://"):
         self.url.data = "http://" + self.url.data

        if not Form.validate(self):
         return False

        if not self.description.data:
         self.description.data = self.url.data

        # Filter out empty and duplicate tag names
        stripped = [t.strip() for t in self.tags.data.split(',')]
        not_empty = [tag for tag in stripped if tag]
        tagset = set(not_empty)
        self.tags.data = ",".join(tagset)

        return True
