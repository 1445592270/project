from flask import render_template,request,redirect,session,jsonify
from main import *
from models import *
import time
from datetime import datetime
import functools


#登录装饰器
def LoginVaild(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        email = request.cookies.get('email')
        userid = request.cookies.get('userid')
        session_email = session.get("email")
        if email and userid and session_email :
            user=User.query.filter(User.email==email,User.id==userid)
            if user:
                return func(*args,**kwargs)
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')
    return inner


@app.route("/index/")
@LoginVaild
def index():
    data=UserInfo.query.all()
    return render_template("index.html",**locals())



## 登出
@app.route('/logout/',methods=['get','post'])
def logout():
    # 删除cookie   删除  session
    response = redirect("/login/")
    response.delete_cookie("email")
    response.delete_cookie("userid")
    # keys = request.COOKIES.keys()
    # print(keys)
    # for one in keys:
    #     response.delete_cookie(one)

    session.pop('email')
    # del session['email']
    return response
@app.route("/login/",methods=['get','post'])
def login():
    if request.method=='POST':
        error_arg=''
        email=request.form.get('email')
        password=request.form.get('password')
        if email and password:
            user=User.query.filter(User.email==email).first()
            if user:
                if user.password==password:

                    error_arg='登录成功'
                    response = redirect("/index/")
                    response.set_cookie("email", user.email)
                    # print(user.email,user.id)
                    response.set_cookie("userid", str(user.id))
                    response.set_cookie("username", user.name)
                    session['email'] = user.email
                    return response
            else:
                error_arg='该邮箱不存在'
        else:
            error_arg='邮箱或密码不存在'
    return render_template("login.html",**locals())
@app.route("/register/",methods=['get','post'])
def register():
    if request.method=='POST':
        error_msg=''
        email=request.form.get('email')
        password=request.form.get('password')
        password2=request.form.get('password2')
        if email and password:
            if password==password2:
                user=User.query.filter(User.email==email).first()
                if user:
                    error_msg = '用户存在，正在跳转登录页面'
                    time.sleep(3)
                    return redirect('/login/')
                else:
                    user=User(email=email,password=password)
                    user.save()
            else:
                error_msg='两次密码不一致'
        else:
            error_msg='邮箱或密码不存在'
    return render_template("register.html",**locals())


from test import MyDate

@app.route("/userinfo/")
@LoginVaild
def userinfo():
    obj = MyDate()
    result = obj.get_date()
    user_email=request.cookies.get('email')
    user=User.query.filter(User.email==user_email).first()
    # print(user)
    # print(result)
    return render_template("userinfo.html",**locals())

#
# if __name__ == '__main__':
#     app.run(debug=True)


@app.route('/leavel_list/',methods=['get','post'])
@LoginVaild
def leavel_list():
    #适用于mysql
    # if request.method=='POST':
    #     userid=request.cookies.get('userid')
    #     data=request.form
    #     start_time=data.get('start_time')
    #     end_time=data.get('end_time')
    #     leavel=Leavel()
    #     leavel.request_id=userid
    #     leavel.request_name=data.get('username')
    #     leavel.request_type=data.get('type')
    #     leavel.request_start=data.get('start_time')
    #     leavel.request_end=data.get('end_time')
    #     leavel.request_description=data.get('dec')
    #     leavel.request_phone=data.get('phone')
    #     leavel.request_status=0
    #     leavel.save()
    #     return redirect("/leavel_all_list/")

    #以下使用sqlite
    if request.method=='POST':
        userid=request.cookies.get('userid')
        data=request.form
        data1=request.form.to_dict()
        lis=[]
        # print(data1)
        for i,j in data1.items():
            lis.append(len(j))
        print(lis)
            # print(len(j))
        if 0 not in lis:
            # print(data)
            # print(data[0][1])
            start=data.get('start_time').replace('T',' ')
            end=data.get('end_time').replace('T',' ')
            start_time=datetime.strptime(start, '%Y-%m-%d %H:%M')
            end_time=datetime.strptime(end, '%Y-%m-%d %H:%M')
            # print(start_time,end_time)
            leavel=Leavel()
            leavel.request_id=userid
            leavel.request_name=data.get('username')
            leavel.request_type=data.get('type')
            leavel.request_start=start_time
            leavel.request_end=end_time
            leavel.request_description=data.get('dec')
            leavel.request_phone=data.get('phone')
            leavel.request_status=0
            leavel.save()
            return redirect("/leavel_all_list/")
        else:
            return redirect('/leavel_list/')
    return render_template('leavel_list.html')

from sdk.pager import Pager
@app.route("/leavel_all_list/<int:page>/",methods=["get","post"])
@LoginVaild
def leavel_all_list(page):
    leave = Leavel.query.filter(Leavel.request_id == request.cookies.get("userid")).all()
    pager=Pager(leave,10)
    page_data=pager.page_data(page)
    page_data=pager.page_data(page)
    return render_template("leavel_all_list.html",**locals())


@app.route('/chexiao/',methods=['get','post'])
def chexiao():
    #获取请假条id
    id=request.form.get('id')
    ##delete
    leave=Leavel.query.filter(Leavel.id==id).first()
    leave.delete()
    result={'code':10000,'msg':'删除成功'}
    return jsonify(result)     #返回json串


from form import TaskForm
@app.route('/add_task/',methods=['get','post'])
def add_task():
    error = {}
    task = TaskForm()
    if request.method=='POST':
        if task.validate_on_submit():
            FormData=task.data
            # print(FormData.get('public'))
            taskform=Taskform()
            taskform.name=FormData.get('name')
            taskform.public=FormData.get('public')
            taskform.time=FormData.get('time')
            taskform.description=FormData.get('description')
            taskform.save()
        else:
            error=task.errors
            # print(error)
    return render_template('add_task.html',**locals())

