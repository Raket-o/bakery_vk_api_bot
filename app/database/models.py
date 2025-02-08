"""the module for creating tables"""

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from app.database.connect import Base


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    products = relationship(
        "Product",
        cascade="all, delete",
        backref="categories",
        passive_deletes=True,
        lazy=True,
    )

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    description = Column(String(400), nullable=True)
    category_id = Column(
        Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
