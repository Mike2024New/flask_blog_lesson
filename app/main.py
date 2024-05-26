"""БАЗА ДАННЫХ МОЖЕТ БЫТЬ СОЗДАНА ТОЛЬКО ИЗ КОНТЕКСТА ПРИЛОЖЕНИЯ
ВСЕ ОСТАЛЬНЫЕ МАТЕРИАЛЫ УСТАРЕВШИЕ (ДО СЕГОДНЯ 25.05.24), данный пример учебный и в качестве БД пока что выбрана
sqlite

ВАЖНО!
1.) БАЗА ДАННЫХ ИНИЦИАЛИЗИРУЕТСЯ И КОННЕКТИТСЯ ТОЛЬКО ЧЕРЕЗ МЕНЕДЖЕР КОНТЕКСТА FLASK (app.context)
2.) ВО ИЗБЕЖАНИЕ ЦИКЛИЧЕСКОГО ИМПОРТА, РЕГИСТРАЦИЮ BLUEPRINT ПРОИЗВОДИТЬ В MAIN.PY А НЕ В APP.PY, НО ВСЕ РАВНО ЕСТЬ
НЮАНС В ТОМ, ЧТО В ФАЙЛЕ BLUEPRINT.PY (В ПАПКЕ POSTS) СРЕДА ПАЙЧАРМ РУГАЕТСЯ НА ТО ЧТО НЕ ВИДИТ MODELS.PY

==================================================================================
!!! - АРХИВАЖНО: ЕСЛИ ПОДКЛЮЧАТЬСЯ К MYSQL, POSTGRES И Т.Д., В ФАЙЛЕ CONFIG.PY НЕДОПУСТИМО НАПРЯМУЮ ПРОПИСЫВАТЬ
АДРЕСА К ЛОГИНАМ И ПАРОЛЯМ, ЭТИ ДАННЫЕ НУЖНО ХРАНИТЬ В СИСТЕМНЫХ ПЕРЕМЕННЫХ И ЗАГРУЖАТЬ ИХ OS.GETENV
МОЖНО КОНЕЧНО ИСПОЛЬЗОВАТЬ .GITIGNORE, НО ЕСТЬ ШАНС ЗАБЫТЬ ПРО ЭТО (ЧЕЛОВЕЧЕСКИЙ ФАКТОР) И ДАННЫЕ УТЕКУТ - !!!
БАЗА ДАННЫХ КОТОРАЯ СОЗДАЁТСЯ В ПАПКЕ INSTANCE (УЧЕБНАЯ SQLITE), ДОБАВЛЕНА В .GITIGNORE
==================================================================================
"""
from app import app
from models import db
from posts.blueprint import posts

import view

# ниже по тексту подключения blueprints
app.register_blueprint(posts)  # регистрируем blueprints (модуль) posts

with app.app_context():
    """connect с базой данных устанавливается именно в этой точке"""
    print(f"Запущен обработчик: {view.__name__}")  # эта строка сделана просто, чтобы добиться зеленой галочки вверху))
    db.create_all()  # создание базы данных (IF NOT EXISTS в orm работает по умолчанию)
    db.session.commit()  # сохраняем изменения -> база создастся и сохранится в папке instance/

if __name__ == '__main__':
    app.run()
