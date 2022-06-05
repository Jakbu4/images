from .models import Photo
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

class PhotoSerializerBasic(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    thumbnail_200px = serializers.SerializerMethodField()

    def get_thumbnail_200px(self, obj):
        thumbnail_200px = get_thumbnail(obj.link, 'x200', crop='center', progressive=False).url
        return "http://127.0.0.1:8000" + thumbnail_200px
    
    class Meta:
        model = Photo
        fields = ['name', 'link', 'author', 'thumbnail_200px']
        extra_kwargs = {
            'link': {'write_only': True},
        }


class PhotoSerializerPremium(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    thumbnail_200px = serializers.SerializerMethodField()
    thumbnail_400px = serializers.SerializerMethodField()

    def get_thumbnail_200px(self, obj):
        thumbnail_200px = get_thumbnail(obj.link, 'x200', crop='center', progressive=False).url
        return "http://127.0.0.1:8000" + thumbnail_200px

    def get_thumbnail_400px(self, obj):
        thumbnail_400px = get_thumbnail(obj.link, 'x400', crop='center', progressive=False).url
        return "http://127.0.0.1:8000" + thumbnail_400px
    
    class Meta:
        model = Photo
        fields = ['name', 'link', 'author', 'thumbnail_200px', 'thumbnail_400px']


class PhotoSerializerEnterprise(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    thumbnail_200px = serializers.SerializerMethodField()
    thumbnail_400px = serializers.SerializerMethodField()
    # seconds_to_expire = serializers.IntegerField(default=230)

    def get_thumbnail_200px(self, obj):
        thumbnail_200px = get_thumbnail(obj.link, 'x200', crop='center', progressive=False).url
        return "http://127.0.0.1:8000" + thumbnail_200px

    def get_thumbnail_400px(self, obj):
        thumbnail_400px = get_thumbnail(obj.link, 'x400', crop='center', progressive=False).url
        return "http://127.0.0.1:8000" + thumbnail_400px

    # def get_seconds_to_expire(self, obj):
    #     seconds_to_expire = 200
    #     return seconds_to_expire
    

    class Meta:
        model = Photo
        fields = ['name', 'link', 'author', 'thumbnail_200px', 'thumbnail_400px']
        # extra_kwargs = {
        #     'seconds_to_expire': {'write-only': True},
        # }

