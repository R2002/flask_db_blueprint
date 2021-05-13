from flask import Flask
import config, views
from database import init_database

# create_app
def create_app():
    # Flask
    app = Flask(__name__)
    # config
    app.config.update(config.cf)
    # DB初期設定
    init_database(app)
    return app

# app
app = create_app()

# Blueprint
# データベース参照（view）: views/index.py
app.register_blueprint(views.index.app)

# 一行追加（insert）, 一行変更（update）, 一行削除（delete）: views/database.py
app.register_blueprint(views.database.app)
