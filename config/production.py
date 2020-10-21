from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x05$A\xd7\xd8\x1b\xc4RY\xfd7\xa9\x07\xf7\xc6\xdd'
