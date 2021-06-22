from rest_framework import serializers
from .models import Blog

class BlogApi(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = '__all__'