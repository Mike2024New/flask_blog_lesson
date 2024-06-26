from app import db
from datetime import datetime
import re


def slugify(s):
    """обработка заголвка поста, чтобы сформировать ссылку (удаляем ненужные символы)"""
    pattern = r'[^\w]'
    return re.sub(pattern, '-', s).lower()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Post id>: {self.id},title:{self.title}>'
