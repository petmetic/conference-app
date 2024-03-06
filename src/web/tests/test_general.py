from django.test import TestCase

from .factories import UserFactory


class GeneralTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        The user (Alice) should be able to see `home` page.
        """

        cls.user = UserFactory(
            username="alicejohnson", first_name="Alice", last_name="Johnson"
        )

    def test_index_page_loads_for_unauthorized_user(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="Welcome to the Conference APP!")

    def test_home_page_loads_for_authorized_user(self):
        self.client.force_login(self.user)

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="This is the homepage.")
