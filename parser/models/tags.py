from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from parser.models.comment_tag import comment_tag_association_table
from parser.models.database import db


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")

    comment = relationship(
        "Comment",
        secondary=comment_tag_association_table,
        back_populates="tag",
    )

    def __str__(self):
        return self.name
