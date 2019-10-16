from main import *
from views import *
from models import *
from flask_script import Manager
import sys
manger=Manager(app)
@manger.command
def migrate():
    db.create_all()
if __name__ == '__main__':
    manger.run()


#封装方法
# commend=sys.argv[1]
# commend1=sys.argv[-1]
# print(commend)
#
# if commend=='runserver':
#     if commend1=='0.0.0.0:8000':
#         app.run(host='0.0.0.0',port=8000)
#     else:
#         app.run()
# if commend=='migrate':
#     db.create_all()

