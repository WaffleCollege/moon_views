# import os

# from flask import Flask

# def create_app(test_config=None):
#     # Flaskアプリを作って設定する
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # /にアクセスした時に"Hello, World!"を返すシンプルなコード
#     @app.route('/')
#     def hello():
#         return 'Hello, World!'
    
#     # CLI コマンドを登録
#     from . import db
#     db.init_app(app)

#     from . import blogs
#     app.register_blueprint(blogs.blog_bp)

#     return app
from flask import Flask
# SQLAlchemyをインポート
from flask_sqlalchemy import SQLAlchemy
# SQLAlchemyのdeclarative_baseをインポート
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db = SQLAlchemy()  # ここでインスタンス作成

def create_app():
    # アプリケーションのインスタンスを作成
    app = Flask(__name__)
    # SQLiteのデータベースファイルを指定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
    # SQLAlchemyの設定を無効化
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # SQLAlchemyのインスタンスをアプリに紐付け

    # blueprintの登録
    from . import blogs
    app.register_blueprint(blogs.blog_bp)

    # データベースのテーブルを作成
    with app.app_context():
        db.create_all()

    return app