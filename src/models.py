from pydantic import BaseModel

ignoremodels: list = ['basemodel', 'product']

class Product(BaseModel):
    description: str
    currency: str
    price: float
    name: str
    url_image: str
    category: str


class Food(Product):
    availible: bool


class Wear(Product):
    size: list | str


class Furniture(Product):
    material: str


class Sneaker(Product):
    size: list | str


class Electronic(Product):
    brand: str


class Stationery(Product):
    brand: str


class HomeDecoration(Product):
    brand: str


class Boot(Product):
    brand: str
    size: str
