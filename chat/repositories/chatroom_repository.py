# chat/repository/chat_repository.py

from ..entities.models import ChatRoom, Message
from django.contrib.auth.models import User

class ChatRepository:
    def create_chatroom(self, name, max_members):
        # Create a new chatroom in the database
        chatroom = ChatRoom.objects.create(name=name, max_members=max_members)
        return chatroom

    def list_chatrooms(self):
        # Retrieve a list of all chatrooms from the database
        chatrooms = ChatRoom.objects.all()
        return chatrooms

    def add_user_to_chatroom(user_id, chatroom_id):
        # Retrieve user and chatroom objects from the database
        user = User.objects.get(id=user_id)
        chatroom = ChatRoom.objects.get(id=chatroom_id)

        # Add the user to the chatroom
        chatroom.members.add(user)

    def remove_user_from_chatroom(user_id, chatroom_id):
        # Retrieve user and chatroom objects from the database
        user = User.objects.get(id=user_id)
        chatroom = ChatRoom.objects.get(id=chatroom_id)

        # Remove the user from the chatroom
        chatroom.members.remove(user)

    def send_message(self, sender_id, chatroom_id, content):
        # Send a message to a chatroom, and save it in the database
        chatroom = ChatRoom.objects.get(pk=chatroom_id)
        sender = User.objects.get(pk=sender_id)

        message = Message.objects.create(
            chat_room=chatroom,
            sender=sender,
            content=content
        )

        

        return message

    def list_messages(self, chatroom_id):
        # Retrieve a list of messages for a specific chatroom from the database
        chatroom = ChatRoom.objects.get(pk=chatroom_id)
        messages = Message.objects.filter(chat_room=chatroom)
        return messages
