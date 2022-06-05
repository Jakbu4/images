from .models import Photo
from rest_framework import viewsets
from .serializer import PhotoSerializerBasic, PhotoSerializerPremium, PhotoSerializerEnterprise
from django.contrib.auth.mixins import LoginRequiredMixin


class PhotoViewset(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Photo.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


    def get_serializer_class(self):
        if self.request.user.tier == "Basic":
            return PhotoSerializerBasic
        if self.request.user.tier == "Premium":
            return PhotoSerializerPremium
        if self.request.user.tier == "Enterprise":
            return PhotoSerializerEnterprise
    
 
