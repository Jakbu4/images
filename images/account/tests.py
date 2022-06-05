from django.contrib.auth import get_user_model
from django.test import TestCase


class AccountsTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='qwerty', email='qwerty@user.com', password='zaq1@WSX')
        self.assertEqual(user.email, 'qwerty@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertIsNotNone(user.username)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.password)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='qwerty', email='', password="zaq1@WSX")


    def test_create_superuser(self):
        User = get_user_model()
        staff_user = User.objects.create_superuser(username='qwertyuiop', email='qwertyuiop@user.com', password='zaq1@WSX')
       
        self.assertEqual(staff_user.email, 'qwertyuiop@user.com')
        self.assertTrue(staff_user.is_active)
        self.assertTrue(staff_user.is_staff)
        self.assertTrue(staff_user.is_superuser)
        self.assertIsNotNone(staff_user.username)
        self.assertIsNotNone(staff_user.email)
        self.assertIsNotNone(staff_user.password)


        with self.assertRaises(TypeError):
            User.objects.create_superuser()
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email='')
        with self.assertRaises(ValueError):
            User.objects.create_superuser(username='qwerty', email='', password="zaq1@WSX")

