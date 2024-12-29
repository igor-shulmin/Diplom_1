import pytest
from unittest.mock import Mock, patch


class TestBurger:

    @patch('praktikum.bun.Bun.__init__', return_value=None)
    def test_set_buns(self, mock_bun, burger):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_set_buns_uncorrect_data_error(self, burger):

        assert bool(burger.set_buns('bun')) == False

    @patch('praktikum.ingredient.Ingredient.__init__', return_value=None)
    def test_add_ingredient(self, mock_ingredient, burger):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_add_ingredient_uncorrect_data_error(self, burger):

        assert bool(burger.add_ingredient('ingredient')) == False

    @patch('praktikum.ingredient.Ingredient.__init__', return_value=None)
    def test_remove_ingredient(self, mock_ingredient, burger):
        burger.add_ingredient(mock_ingredient)
        index_mock_ingredient = burger.ingredients.index(mock_ingredient)
        burger.remove_ingredient(index_mock_ingredient)

        assert len(burger.ingredients) == 0

    @pytest.mark.parametrize('index', [0, '0'])
    def test_remove_ingredient_uncorrect_data_error(self, burger, index):
        try:
            burger.remove_ingredient(index)
        except (IndexError, TypeError) as e:

            assert isinstance(e, (IndexError, TypeError))

    @patch('praktikum.ingredient.Ingredient.__init__', return_value=None)
    @patch('praktikum.ingredient.Ingredient.__init__', return_value=None)
    def test_move_ingredient(self, mock_ingredient_1, mock_ingredient_2, burger):
        burger.add_ingredient(mock_ingredient_1)
        index_mock_ingredient_1 = burger.ingredients.index(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        index_mock_ingredient_2 = burger.ingredients.index(mock_ingredient_2)
        burger.move_ingredient(index_mock_ingredient_2, index_mock_ingredient_1)

        assert burger.ingredients.index(mock_ingredient_1) == index_mock_ingredient_2

    @patch('praktikum.ingredient.Ingredient.__init__', return_value=None)
    @patch('praktikum.ingredient.Ingredient.__init__', return_value=None)
    @pytest.mark.parametrize('new_index', [0, '0'])
    def test_move_ingredient_uncorrect_data_error(self, mock_ingredient_1, mock_ingredient_2, new_index, burger):
        try:
            burger.add_ingredient(mock_ingredient_1)
            index_mock_ingredient_1 = burger.ingredients.index(mock_ingredient_1)
            burger.move_ingredient(index_mock_ingredient_1, new_index)
        except (IndexError, TypeError) as e:

            assert isinstance(e, (IndexError, TypeError))

    def test_get_price_get_float(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100.0

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]

        assert burger.get_price() == 300.0 and type(burger.get_price()) == float

    def test_get_receipt_get_string(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'bun'
        mock_bun.get_price.return_value = 100.0

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'ingredient'
        mock_ingredient.get_price.return_value = 100.0
        mock_ingredient.get_type.return_value = 'type'

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]

        assert burger.get_receipt() == '\n'.join([f'(==== {burger.bun.get_name()} ====)',
                                                   f'= {str(burger.ingredients[0].get_type()).lower()} {burger.ingredients[0].get_name()} =',
                                                   f'(==== {burger.bun.get_name()} ====)\n',
                                                   f'Price: {burger.get_price()}'])
        assert type(burger.get_receipt()) == str
