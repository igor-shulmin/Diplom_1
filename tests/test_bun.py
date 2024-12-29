import pytest
from praktikum.bun import Bun


class TestBun:

    def test_create_bun(self):
        bun = Bun('new_bun', 100.0)

        assert bun.name == 'new_bun' and type(bun.name) == str
        assert bun.price == 100.0 and type(bun.price) == float

    @pytest.mark.parametrize('name, price', [[['new_bun'], 100.0], ['new_bun', 'сто']])
    def test_create_bun_with_uncorrect_data_error(self, name, price):
        bun = Bun(name, price)

        assert type(bun.name) != str or type(bun.price) != float

    @pytest.mark.parametrize('name, price', [['new_bun', None], [None, 100.0]])
    def test_create_bun_without_required_field_error(self, name, price):
        bun = Bun(name, price)

        assert type(bun.name) != str or type(bun.price) != float

    def test_get_name_of_bun(self, bun):

        assert bun.get_name() == 'new_bun' and type(bun.get_name()) == str

    def test_get_price_of_bun(self, bun):

        assert bun.get_price() == 100.0 and type(bun.get_price()) == float
