from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from parser.models.database import db


class Url(db.Model):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
#    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    link = Column(String(512), unique=True, nullable=False, default="")
#    user = relationship("User", back_populates="url")

    def __str__(self):
        return self.link
