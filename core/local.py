PROJECT_NAME = "AM - Blog FastAPI"
SERVER_HOST = 'http://127.0.0.1:8000'

# Data Base
POSTGRES_SERVER = "localhost"
POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "admin"
POSTGRES_DB = "blog"

# Email
SMTP_TLS = True
SMTP_PORT = 587
SMTP_HOST = 'smtp.gmail.com'
SMTP_USER = 'test@gmail.com'
SMTP_PASSWORD = "F00dz!#0"
EMAILS_FROM_EMAIL = "test@gmail.com"
EMAILS_FROM_NAME = "AM - Blog FastAPI"
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "/src/email-templates/build"
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL
