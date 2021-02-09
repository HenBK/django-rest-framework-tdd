from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email"""

        email = 'henrique.kubenda@gmail.com'
        password = '123abc'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        """Tests that the email for a new user gets normalized (lower case)"""
        email = 'henrique.kubenda@GmAiL.COM'
        user = get_user_model().objects.create_user(email, password='123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_with_none_email(self):
        """Tests that the user creation fails if the email provided is None"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password='123456')

    def test_new_superuser_creation(self):
        """
        Tests that the fields is_staff and is_superuser are set to True when
        creating a new superuser from the command line
        """

        superuser = get_user_model().objects.create_superuser(
            'henrique.kubenda@gmail.com',
            '123456',
        )

        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
