from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy를 사용해 데이터베이스 저장
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'  #테이블 이름 : users
    email = db.Column(db.String, primary_key = True)
    password = db.Column(db.String(64))
    apikey = db.Column(db.String(128))