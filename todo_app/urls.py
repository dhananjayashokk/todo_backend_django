from django.urls import path,include
from  . views import *
from rest_framework import routers



urlpatterns = [
	path('create_bucket', create_bucket	),
	path('get_buckets', get_buckets	),
	path('add_todos', add_todos	),
	path('get_todos', get_todos	),
	path('update_todos', update_todos ),
	path('delete_todos', delete_todos	)
] 