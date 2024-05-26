from flask import render_template
from app import app
from app import db
from models import Post


@app.route('/')
def index():
    name = "Ivan"
    return render_template("index.html", n=name)


@app.route('/test')
def create():
    p = Post(title='Второй пост', body='Разработка на flask тестовый второй пост.')
    try:
        db.session.add(p)
        db.session.commit()
        return render_template('test_msg.html', status='Успешно', msg='Данные записаны в базу данных')
    except Exception as err:
        print(f"Ошибка добавления тестового поста в БД {err}")
        return render_template('test_msg.html', status='Ошибка',
                               msg=f"Ошибка добавления тестового поста в БД <br> {err}")


@app.route('/gets')
def get_posts():
    posts = Post.query.all()
    posts = "<br>".join([f"{p.id}{p.title}" for p in posts])
    return render_template('test_msg.html', status='Успешно', msg=f'Данные из БД: <br>{posts}')
