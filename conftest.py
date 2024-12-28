import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def bun():
    bun = Bun('new_bun', 100.0)

    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'new_ingredient', 100.0)

    return ingredient

@pytest.fixture
def database():
    database = Database()

    return database

@pytest.fixture
def burger():
    burger = Burger()

    return burger
