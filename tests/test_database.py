class TestDatabase:

    def test_available_buns_get_list(self, database):

        assert type(database.available_buns()) == list and len(database.available_buns()) == 3

    def test_available_ingredients_get_list(self, database):

        assert type(database.available_ingredients()) == list and len(database.available_ingredients()) == 6
