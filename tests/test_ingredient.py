import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_create_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'new_ingredient', 100.0)

        assert ingredient.type == INGREDIENT_TYPE_SAUCE and type(ingredient.type) == str
        assert ingredient.name == 'new_ingredient' and type(ingredient.name) == str
        assert ingredient.price == 100.0 and type(ingredient.price) == float

    @pytest.mark.parametrize('type, name, price', [[1, 'new_ingredient', 100.0], ['type', 1, 100.0], ['type', 'new_ingredient', '100.0']])
    def test_create_ingredient_with_uncorrect_data_error(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.type != str or ingredient.name != str or ingredient.get_price() != float

    @pytest.mark.parametrize('type, name, price', [[None, 'new_ingredient', 100.0], ['type', None, 100.0], ['type', 'new_ingredient', None]])
    def test_create_ingredient_without_required_field_error(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.type != str or ingredient.name != str or ingredient.get_price() != float

    def test_get_type_of_ingredient(self, ingredient):

        assert ingredient.type == INGREDIENT_TYPE_SAUCE and type(ingredient.type) == str

    def test_get_name_of_ingredient(self, ingredient):

        assert ingredient.name == 'new_ingredient' and type(ingredient.type) == str

    def test_get_price_of_ingredient(self, ingredient):

        assert ingredient.price == 100.0 and type(ingredient.price) == float
