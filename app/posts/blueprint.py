from flask import Blueprint, render_template, request
from models import Post, add_post  # это решение из видеоурока выглядит жидким, нужно подумать о структуре проекта

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


@posts.route('/test', methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        p = Post(title=request.form["title"], body=request.form["body"])
        try:
            add_post(p)
            return render_template('test_msg.html', status='Успешно',
                                   msg='Данные записаны в базу данных')
        except Exception as err:
            print(f"Ошибка добавления тестового поста в БД {err}")
            return render_template('test_msg.html', status='Ошибка',
                                   msg=f"Ошибка добавления тестового поста в БД <br> {err}")
    return render_template("posts/add_post.html")


"""
@posts.route('/test')
def create():
    p = Post(title='Второй пост', body='Разработка на flask тестовый второй пост.')
    try:
        add_post(p)
        return render_template('test_msg.html', status='Успешно', msg='Данные записаны в базу данных')
    except Exception as err:
        print(f"Ошибка добавления тестового поста в БД {err}")
        return render_template('test_msg.html', status='Ошибка',
                               msg=f"Ошибка добавления тестового поста в БД <br> {err}")

"""
