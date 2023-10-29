from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, VARCHAR
from parser.models.database import db
from flask_login import UserMixin
from security import flask_bcrypt
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False, default="", server_default="")
    password_ = Column(LargeBinary, nullable=True)
    phone = Column(VARCHAR(13), unique=True, nullable=False, default="")
    is_staff = Column(Boolean, nullable=False, default=False)
#    url = relationship("Url",  uselist=False, back_populates="user")
    comment = relationship("Comment", back_populates="user")

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, value):
        self.password_ = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self.password_, password)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

    def __str__(self):
        return self.user.username

