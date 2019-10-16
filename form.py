import wtforms
from flask_wtf import FlaskForm
from wtforms import  validators
from wtforms import ValidationError

def keywords_valid(form,field):
    data=field.data
    keywords=['admin','1111']
    if data in keywords:
        raise ValidationError('不可以为敏感词汇')

class TaskForm(FlaskForm):
    # name=wtforms.StringField(label='任务的名字')
    # description=wtforms.TextField(label='任务描述')
    # time=wtforms.DateField(label='任务的时间')
    # public=wtforms.StringField(label='任务的发布人')
        ## 属性
    name = wtforms.StringField(
        render_kw={
            "class": "form-control",
            "placeholder": "任务的名字"
        },
        validators=[
            validators.DataRequired('任务名字不可为空'),
            validators.Email('不符合email格式'),
            keywords_valid
        ]
    )
    description = wtforms.TextField(render_kw={
        "class": "form-control",
        "placeholder": "任务的描述"
    })
    time = wtforms.DateField(render_kw={
        "class": "form-control",
        "placeholder": "任务的时间"
    })
    public = wtforms.StringField(render_kw={
        "class": "form-control",
        "placeholder": "任务的发布人"
    })