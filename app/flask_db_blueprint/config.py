import os

#--------------------------------------#
# 設定ファイル
#--------------------------------------#
cf = {} # 削除しないでください

# デバッグ表示を有りにする
cf['DEBUG'] = 1

# BD設定
cf['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'db_name': 'flask_db_blueprint',
})

# TRACK_MODIFICATIONSを無効にしておく
cf['SQLALCHEMY_TRACK_MODIFICATIONS'] = False