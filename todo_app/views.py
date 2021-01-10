from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from .serializers import *

@api_view(['POST'])
@csrf_exempt
def create_bucket(request):
	request = json.loads(request.body.decode('utf-8'))
	name=request["buckets"]
	serializer = BucketMasterSerializer(data={"name":name})
	if serializer.is_valid():
		BucketMaster.objects.all().delete()
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
def get_buckets(request):
	buckets=BucketMaster.objects.all()
	if buckets:
		serializer = BucketMasterSerializer(buckets, many=True)
		return Response(serializer.data)
	else:
		return Response([])

@api_view(['POST'])
@csrf_exempt
def add_todos(request):
	request = json.loads(request.body.decode('utf-8'))['todo_data']
	name=request["todo_name"]
	bucket_name=request["bucket_name"]
	serializer = TasksSerializer(data={"name":name,"bucket_name":bucket_name,"status":0})
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
def get_todos(request):
	todos=Tasks.objects.filter(bucket_name=request.GET["bucket_name"])
	if todos:
		serializer = TasksSerializer(todos, many=True)
		return Response(serializer.data)
	else:
		return Response([])

@api_view(['PUT'])
@csrf_exempt
def update_todos(request):
	old_todo=Tasks.objects.filter(id=request.GET["todo_id"]).first()
	todos=Tasks.objects.filter(id=request.GET["todo_id"]).first()
	if todos:
		todos.status=int(1 - int(todos.status))
		serializer = TasksSerializer(old_todo,data={"name":todos.name,"status":todos.status,"bucket_name":todos.bucket_name,"id":todos.id})
		if serializer.is_valid():
			print("validddddddddd")
			serializer.save()
			print("saved")
			return Response([serializer.data])
		return Response(serializer.errors)
	else:
		return Response([])

@api_view(['PUT'])
@csrf_exempt
def delete_todos(request):
	todos=Tasks.objects.filter(id=request.GET["todo_id"]).first()
	if todos:
		todos.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	else:
		return Response([])
