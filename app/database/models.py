"""Модуль с таблицами и полями базы данных"""

from typing import Dict

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, LargeBinary

from app.database.connect import Base


class Category(Base):
    """Таблица с полями Category"""
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

    def get_name(self) -> dict[str, str]:
        """
        Метод возвращает словарь {"название": "название категории"}
        """
        return {"name": self.name}

    def to_json(self) -> dict:
        """
        Метод возвращает всю информацию объекта для сериализации
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Product(Base):
    """Таблица с полями Product"""
    __tablename__ = "products"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    description = Column(String(400), nullable=True)
    image = Column(LargeBinary)
    category_id = Column(
        Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )

    def get_name(self) -> dict[str, str]:
        """
        Метод возвращает словарь {"название": "название продукта"}
        """
        return {"name": self.name}

    def to_json(self) -> dict:
        """
        Метод возвращает всю информацию объекта для сериализации
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
