from conf.database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, Text, DateTime, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200), unique=True, index=True)
    first_name = Column(String(200), index=True)
    last_name = Column(String(200), index=True)
    email = Column(String(500), unique=True)
    password = Column(Text)

    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    # order = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"user_id: {self.id} | user: {self.username}"


# class Category(Base):
#     __tablename__ = "categories"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(200), index=True)
#
#     product = relationship("Product", back_populates="category")
#
#     def __repr__(self):
#         return f"category_id: {self.id} | category: {self.name}"
#
#
# class Product(Base):
#     __tablename__ = "products"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(200), index=True)
#     price = Column(Float)
#     category_id = Column(Integer, ForeignKey("categories.id"))
#
#     category = relationship("Category", back_populates="product")
#     order = relationship("Order", back_populates="product")
#
#     def __repr__(self):
#         return f"product_id: {self.id} | product: {self.name}"
#
#
# class Order(Base):
#     __tablename__ = "orders"
#
#     ORDER_STATUS = (
#         ("PENDING", "pending"),
#         ("IN_TRANSIT", "in_transit"),
#         ("DELIVERED", "delivered")
#     )
#     id = Column(Integer, primary_key=True)
#
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="order")
#
#     product_id = Column(Integer, ForeignKey("products.id"))
#     product = relationship("Product", back_populates="order")
#
#     quantity = Column(Integer, nullable=False)
#     status = Column(ChoiceType, default="PENDING")
#     created_at = Column(DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"order_id: {self.id} | user: {self.user_id.username} | product: {self.product_id.name} | created_at: {self.created_at}"