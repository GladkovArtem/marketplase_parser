from sqlalchemy import Table, Column, Integer, ForeignKey
from parser.models.database import db


comment_tag_association_table = Table(
    "comment_tag_association",
    db.metadata,
    Column("comment_id", Integer, ForeignKey("comment.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tag.id"), nullable=False),
)
