from logging.config import dictConfig
from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='F&+Zw2d:#Ap=vtuM~:V~#zWCHNjDIJ&t',
    url='ls-613246fe400cd9d6633c73899012926ca6a230e2.cclzaajqs5gx.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x05$A\xd7\xd8\x1b\xc4RY\xfd7\xa9\x07\xf7\xc6\xdd'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})