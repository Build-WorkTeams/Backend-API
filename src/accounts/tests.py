from django.test import TestCase
from .models import User, UserManager

# Create your tests here.
class UserManagerTest(TestCase):

    def test_objects_class(self):
        self.assertIsInstance(User.objects, UserManager)

    def test_user_creation(self):
        User.objects.create_user(email="example@mail.com", password="abc123")
        self.assertEqual(User.objects.count(), 1)


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("example@mail.com")

    def test_username_field(self):
        username = self.user.get_username()
        self.assertEqual(username, self.user.email)