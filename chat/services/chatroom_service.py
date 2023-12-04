# chat/service/chatroom_service.py

from chat.repositories import chatroom_repository
from chat.entities.models import ChatRoom, User

repo = chatroom_repository.ChatRepository()

def create_chatroom(name, max_members, creator_username):
    # Check if the creator user exists
    try:
        creator_user = User.objects.get(username=creator_username)
    except User.DoesNotExist:
        # Handle the case where the creator user does not exist
        raise ValueError("Creator user does not exist.")

    # Create the chatroom
    chatroom = ChatRoom(name=name, max_members=max_members)
    chatroom.save()

    # Add the creator user as a member
    chatroom.members.add(creator_user)

    return chatroom

def list_chatrooms():
    # Retrieve a list of chatrooms from the repository
    chatrooms = repo.list_chatrooms()

    return chatrooms

def enter_chatroom(user_id, chatroom_id):
    # Call the repository to add the user to the chatroom
    repo.add_user_to_chatroom(user_id, chatroom_id)

def leave_chatroom(user_id, chatroom_id):
    # Call the repository to remove the user from the chatroom
    repo.remove_user_from_chatroom(user_id, chatroom_id)

def send_message(self, sender_id, chatroom_id, content):
        # Call the repository to send a message
    return chatroom_repository.send_message(sender_id, chatroom_id, content)

def list_messages(self, chatroom_id):
    # Call the repository to list messages
    return chatroom_repository.list_messages(chatroom_id)
