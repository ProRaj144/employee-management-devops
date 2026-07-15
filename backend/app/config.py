
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "employee_db")
    MYSQL_USER = os.getenv("MYSQL_USER", "employee")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "employee123")

settings = Settings()
