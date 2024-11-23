from utils.db import db
from flask_login import UserMixin

class Usuario(UserMixin):
     
     def __init__(self, user_id: int, username: str, password: str, is_admin: bool) -> None :
        self.id = user_id
        self.username = username
        self.password = password
        self.is_admin = is_admin

users = [
      Usuario(1,'Fabian','12345', is_admin=True),
      Usuario(2,'Pilar','123456', is_admin=False),
      Usuario(3,'Mario','1234567', is_admin=False),
]

