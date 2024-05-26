from flask import Blueprint, render_template
from models import Post  # это решение из видеоурока выглядит жидким, нужно подумать о структуре проекта

posts = Blueprint("posts", __name__, url_prefix="/blog", template_folder="templates")


@posts.route('/')
def index():
    """главная страница этого приложения (модуля - blueprint)"""
    posts_all = Post.query.all()
    if len(posts_all) == 0:
        posts_all = False
    return render_template('posts/index.html', posts_all=posts_all)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post=post)
