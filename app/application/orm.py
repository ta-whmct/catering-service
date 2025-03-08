from collections.abc import Sequence, Set
from datetime import datetime
import re
from uuid import UUID, uuid4
from sqlalchemy import Column, ForeignKey, Table, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, declared_attr


def generate_string_uuid() -> str:
    return str(uuid4())


class Base(DeclarativeBase):
    pass


class DefaultBase(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uuid: Mapped[UUID] = mapped_column(default=generate_string_uuid, unique=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return "_".join(_.lower() for _ in re.findall("[A-Z][^A-Z]*", cls.__name__))


class Category(DefaultBase):
    name: Mapped[str]
    # items: Mapped[Set["Item"]] = relationship(back_populates="category")


menu_item_table = Table(
    "menu_item",
    Base.metadata,
    Column("menu_id", ForeignKey("menu.id")),
    Column("item_id", ForeignKey("item.id")),
)


order_item_table = Table(
    "order_item",
    Base.metadata,
    Column("item_id", ForeignKey("item.id")),
    Column("order_id", ForeignKey("order.id")),
)


class Item(DefaultBase):
    name: Mapped[str]
    short_name: Mapped[str | None] = mapped_column(nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped[Category] = relationship(back_populates="items", lazy="subquery")


class Menu(DefaultBase):
    name: Mapped[str]
    items: Mapped[Set[Item]] = relationship(secondary=menu_item_table)


class Room(DefaultBase):
    name: Mapped[str]
    menu_id: Mapped[int] = mapped_column(ForeignKey("menu.id"))
    orders: Mapped[Set["Order"]] = relationship(back_populates="room", lazy="subquery")


class OrderState(DefaultBase):
    value: Mapped[str]


class Order(DefaultBase):
    number: Mapped[str]
    state_id: Mapped[int] = mapped_column(ForeignKey("order_state.id"))
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    room: Mapped[Room] = relationship(back_populates="orders")
    items: Mapped[Sequence[Item]] = relationship(secondary=order_item_table)


class OrderPoint(DefaultBase):
    number: Mapped[str]
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    room: Mapped[Room] = relationship(back_populates="order_points")

class Operator(DefaultBase):
    __tablename__="operator"
    name: Mapped[str]
    menu_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
