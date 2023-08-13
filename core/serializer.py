from rest_framework import serializers

from .models import File
from .utils import check_file_name_exists_or_not

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file_name','created_at', 'update_at']

    
    def create(self, validated_data):
        file_name = validated_data.pop('file_name')
        name = check_file_name_exists_or_not(file_name)
        print(f"name after checking ...:--> {name}")
        validated_data['file_name'] = name
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

    