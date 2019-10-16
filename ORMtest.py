# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os
# import pymysql
# import datetime
# pymysql.install_as_MySQLdb()
# app=Flask(__name__)
# #连接数据库
# BASE_DIR=os.path.abspath(os.path.dirname(__file__))##当前文件  项目所在的根目录
# # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASE_DIR,'test.db')
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost/flask'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True#请求结束之后自动提交
# app.config['SQLALCHEMY_RTACK_MODIFICATIONS']=True#跟踪修改
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True#
# app.config['DEBUG']=True#
#
# db=SQLAlchemy(app)   #绑定flask项目

# class BaseModel(db.Model):
#     __abstract__=True
#     id=db.Column(db.Integer,primary_key=True)
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#     def merge(self):
#         db.session.merge(self)
#         db.session.commit()
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#封装继承使用
# class User(BaseModel):
#     __tablename__='user'  #表名
#     # id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(32))
#     age=db.Column(db.Integer)
#     time=db.Column(db.DATETIME,default=datetime.datetime.now)

# user = User(name="awu",age=19)
# # #  增加数据
# user.save()

### 更新数据
# user = User.query.get(1)
# user.name="aliu"
# user.merge()

## 删除数据
# user = User.query.get(3)
# user.delete()




#创建模型
# class UserInfo(db.Model):
#     __tablename__='userinfo'  #表名
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(32))
#     age=db.Column(db.Integer)
#     time=db.Column(db.DATETIME,default=datetime.datetime.now())
#
# ##数据迁移
# db.create_all()##同步表结构
# ##增加数据
#单条增加
# userinfo=UserInfo(name='xiaoxiaowang',age=19)
# db.session.add(userinfo)
# db.session.commit()

#增加多条
# db.session.add_all([
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19)
# ])
# db.session.commit()
#查询all
# data = UserInfo.query.all()
# print (data)

#get
# data = UserInfo.query.get(1)
# print (data)
# print (data.name)

#不同  id=1 进行查询
# data = UserInfo.query.get(ident=1)
# print (data)
# print (data.name)

#filter   filter_by    过滤  条件
# data = UserInfo.query.filter_by(name="xiaoxiaowang").all()
# print (data)
# data = UserInfo.query.filter(UserInfo.name == "xiaoxiaowang").all()
# print (data)
# #first()
# data = UserInfo.query.filter(UserInfo.name == "xiaoxiaowang").first()
# print (data)


#order_by   排序

## order_by 排 序
# 升序
# data = UserInfo.query.order_by(UserInfo.id).all()
# print (data)
# data =UserInfo.query.order_by("id").all()
# print (data)
# # 降序
# # data = UserInfo.query.order_by(UserInfo.id.desc()).all()
# # print (data)
# data =UserInfo.query.order_by(db.desc("id")).all()
# print (data)

#分页
## sql  select * from userinfo limit 2,3;  2代表从哪里开始   3 取多少条
# data = UserInfo.query.offset(2).limit(2).all()
## limit(2)  取2条数据
## offset(2) 偏移2
# print (data)


# #修改
# data = UserInfo.query.filter(UserInfo.id==1).first()
# data.name = "lisi"
# db.session.merge(data)
# db.session.commit()


#删除
## 删除
#delete
# data = UserInfo.query.filter().first()
# print(data.id)
# db.session.delete(data)
# db.session.commit()

# data = UserInfo.query.filter(UserInfo.id == 2).delete()
# db.session.commit()


# @app.route('/')
# def index():
#     return 'ormtest'
#
# if __name__ == '__main__':
#     app.run()