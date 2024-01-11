from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Image

class UploadedImage(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('imagename', 'image')

        def get_url(self,obj):
            request=self.context.get('request')
            img_url =obj.fingerprint.url
            return request.Build_absolute_url(img_url)
