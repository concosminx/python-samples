import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b"\xd1v\xc1'J\xa0\xdb\x07\xc8\xbddf\xb5\x8aR&"

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    