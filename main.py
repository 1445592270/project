from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()
app=Flask(__name__)
BASE_DIR=os.path.abspath(os.path.dirname(__file__))##当前文件  项目所在的根目录

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASE_DIR,'test.db')
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True#请求结束之后自动提交
app.config['SQLALCHEMY_RTACK_MODIFICATIONS']=True#跟踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True#
app.config['DEBUG']=True#
# SECRET_KEY='wefwefwqefwedfwefwef'##session密钥设置
app.secret_key='edqefqefqefqefqefqef'
db=SQLAlchemy(app)
