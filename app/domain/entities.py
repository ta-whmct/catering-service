from collections.abc import Sequence, Set
from dataclasses import dataclass
from uuid import UUID

from app.domain.value_objects import OrderState


@dataclass
class Entity:
    uuid: UUID


@dataclass
class Category(Entity):
    name: str


@dataclass
class Item(Entity):
    name: str
    category: Category
    short_name: str | None = None


@dataclass
class Menu(Entity):
    name: str
    items: Set[Item]


@dataclass
class Room(Entity):
    name: str
    menu: Menu


@dataclass
class Order(Entity):
    number: str
    state: OrderState
    room: Room
    items: Sequence[Item]


@dataclass
class OrderPoint(Entity):
    number: str
    room: Room
    description: str


@dataclass
class Operator(Entity):
    name: str
