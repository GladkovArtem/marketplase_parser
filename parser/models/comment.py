from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from parser.models.database import db
from datetime import datetime
from parser.models.comment_tag import comment_tag_association_table


class Comment(db.Model):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="comment")
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(String(1000), nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tag = relationship(
        "Tag",
        secondary=comment_tag_association_table,
        back_populates="comment",
    )

    def __str__(self):
        return self.title
