from .db_config import db
from sqlalchemy import Column, Integer, String, Table, ForeignKey


freeway_business = db.Table(
    "freeway_business",
    Column("freeway_id", Integer, ForeignKey("freeway.id")),
    Column("business_entity_id", Integer, ForeignKey("business_entity.id")),
)
