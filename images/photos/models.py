from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.core.validators import FileExtensionValidator

User = get_user_model()


# unique filename
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename


class Photo(models.Model):
    name = models.CharField(max_length=100)
    link = models.ImageField(upload_to=get_file_path, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'], message="Wrong file format!")])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.name
