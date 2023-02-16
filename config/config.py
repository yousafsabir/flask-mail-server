
from decouple import config


class Settings():
    API = "/api"
    MAIL = config("MAIL", cast=str)
    MAIL_PASS = config("MAIL_PASS", cast=str)
    MAIL_SERVER = config("MAIL_SERVER", cast=str)
    MAIL_PORT = config("MAIL_PORT", cast=int)
    RECIEVER_MAIL = config("RECIEVER_MAIL", cast=str)
    BACKEND_CORS_ORIGINS = [
        "https://theyummyservings.co.uk",  # add yuor cors here
        "http://127.0.0.1:5500/",
    ]
    PROJECT_NAME = "TheYummyServings"


settings = Settings()
