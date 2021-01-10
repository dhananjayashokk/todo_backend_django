from rest_framework import serializers
from .models import *

class BucketMasterSerializer(serializers.ModelSerializer):
	class Meta:
		model=BucketMaster
		fields=('name')
		fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tasks
		fields=('id','name','status','bucket_name')

