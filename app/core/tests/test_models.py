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
