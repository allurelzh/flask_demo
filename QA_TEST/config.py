#数据库的连接设置
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'qa'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SECRET_KEY = 'adhudhudfgdf'

#邮箱配置，暂时使用QQ邮箱进行测试

MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG =  True
MAIL_USERNAME = "1059630415@qq.com"
MAIL_PASSWORD = "linauwjepximbeeh"
MAIL_DEFAULT_SENDER = "1059630415@qq.com"
