# chat/urls.py

from django.urls import path
from .controllers import chatroom_controller

urlpatterns = [
    path('create_chatroom/', chatroom_controller.create_chatroom, name='create_chatroom'),
    path('list_chatrooms/', chatroom_controller.list_chatrooms, name='list_chatrooms'),
    path('enter_chatroom/', chatroom_controller.enter_chatroom, name='enter_chatroom'),
    path('leave_chatroom/', chatroom_controller.leave_chatroom, name='leave_chatroom'),
    # Add other chatroom endpoints here
]
