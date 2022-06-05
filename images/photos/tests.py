from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Photo
from django.core.files.temp import NamedTemporaryFile


class PhotosTestCase(TestCase):

    def test_adding_image(self):
        User = get_user_model()
        user = User.objects.create_user(username='qwerty', email='qwerty@user.com', password='zaq1@WSX')
        temp_file = NamedTemporaryFile(suffix='.jpg').name
        image = Photo(name='dupa', link=temp_file, author=user)
        image.save()

        self.assertEqual(Photo.objects.count(), 1)
        self.assertEqual(image.name, 'dupa')
        self.assertEqual(image.author, user)
        self.assertEqual(image.link, temp_file)

