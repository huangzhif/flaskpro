CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
import os

basedir = os.path.abspath(os.path.dirname(__file__))

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
# email server
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USERNAME = '×××@qq.com' #sender
MAIL_PASSWORD = '***' #授权码

# administrator list
ADMINS = ['942402379@qq.com'] #resp

# pagination
POSTS_PER_PAGE = 1