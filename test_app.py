from main_test import MainTest


class TestViews(MainTest):
    def test_login(self):
        response = self.client.get("/get_meals")
        self.assert200()
        self.assertTrue("ash", )


