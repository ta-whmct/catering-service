from uuid import UUID, uuid4
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


def generate_string_uuid() -> str:
    return str(uuid4())


class Base(DeclarativeBase):
    pass


class DefaultBase(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[UUID] = mapped_column(default_factory=generate_string_uuid, unique=True)


class Category(DefaultBase):
    __tablename__ = "category"
    name: Mapped[str]
    # items: Mapped[Set["Item"]] = relationship(back_populates="category")


# menu_item_table = Table(
#     "menu_item",
#     Base.metadata,
#     Column("menu_id", ForeignKey("menu.id")),
#     Column("item_id", ForeignKey("item.id")),
# )


# order_item_table = Table(
#     "order_item",
#     Base.metadata,
#     Column("item_id", ForeignKey("item.id")),
#     Column("order_id", ForeignKey("order.id")),
# )


# class Item(DefaultBase):
#     __tablename__ = "item"
#     name: Mapped[str]
#     short_name: Mapped[str | None] = mapped_column(nullable=True)
#     category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
#     category: Mapped[Category] = relationship(back_populates="items", lazy="subquery")


# class Menu(DefaultBase):
#     __tablename__ = "menu"
#     name: Mapped[str]
#     items: Mapped[Set[Item]] = relationship(secondary=menu_item_table)


# class Room(DefaultBase):
#     __tablename__ = "room"
#     name: Mapped[str]
#     menu_id: Mapped[int] = mapped_column(ForeignKey("menu.id"))
#     orders: Mapped[Set["Order"]] = relationship(back_populates="room", lazy="subquery")


# class OrderState(DefaultBase):
#     __tablename__ = "order_state"
#     value: Mapped[str]


# class Order(DefaultBase):
#     __tablename__ = "order"
#     number: Mapped[str]
#     state_id: Mapped[int] = mapped_column(ForeignKey("order_state.id"))
#     room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
#     room: Mapped[Room] = relationship(back_populates="orders")
#     items: Mapped[Sequence[Item]] = relationship(secondary=order_item_table)


# class OrderPoint(DefaultBase):
#     __tablename__ = "order_point"
#     number: Mapped[str]
#     room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
#     room: Mapped[Room] = relationship(back_populates="order_points")
# class Operator(DefaultBase):
#     __tablename__="operator"
#     name: Mapped[str]
#     menu_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
