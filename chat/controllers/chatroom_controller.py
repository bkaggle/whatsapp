# chat/controller/chatroom_controller.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chat.services import chatroom_service
import json

@csrf_exempt
def create_chatroom(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            
            # Extract relevant information
            name = data.get('name')
            max_members = data.get('max_members')
            creator_username = data.get('creator_username')

            # Call the service to create the chatroom
            chatroom = chatroom_service.create_chatroom(name, max_members, creator_username)

            # Return a JSON response with the created chatroom details
            return JsonResponse({
                'status': 'success',
                'message': 'Chatroom created successfully',
                'chatroom': {
                    'id': chatroom.id,
                    'name': chatroom.name,
                    'max_members': chatroom.max_members,
                    # Add other chatroom fields as needed
                }
            })

        except ValueError as e:
            # Handle the case where the creator user does not exist
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def list_chatrooms(request):
    if request.method == 'GET':
        # Call the service to get a list of chatrooms
        chatrooms = chatroom_service.list_chatrooms()

        # Serialize the chatrooms data
        serialized_chatrooms = [{
            'id': chatroom.id,
            'name': chatroom.name,
            'max_members': chatroom.max_members,
            # Add other chatroom fields as needed
        } for chatroom in chatrooms]

        # Return a JSON response with the list of chatrooms
        return JsonResponse({
            'status': 'success',
            'message': 'Chatrooms retrieved successfully',
            'chatrooms': serialized_chatrooms
        })

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@csrf_exempt
def enter_chatroom(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            
            # Extract relevant information
            user_id = data.get('user_id')
            chatroom_id = data.get('chatroom_id')

            # Call the service to add the user to the chatroom
            chatroom_service.enter_chatroom(user_id, chatroom_id)

            # Return a JSON response indicating success
            return JsonResponse({'status': 'success', 'message': 'User entered the chatroom'})

        except ValueError as e:
            # Handle the case where the user or chatroom does not exist
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def leave_chatroom(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            
            # Extract relevant information
            user_id = data.get('user_id')
            chatroom_id = data.get('chatroom_id')

            # Call the service to remove the user from the chatroom
            chatroom_service.leave_chatroom(user_id, chatroom_id)

            # Return a JSON response indicating success
            return JsonResponse({'status': 'success', 'message': 'User left the chatroom'})

        except ValueError as e:
            # Handle the case where the user or chatroom does not exist
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            
            # Extract relevant information
            sender_id = data.get('sender_id')
            chatroom_id = data.get('chatroom_id')
            content = data.get('content')

            # Call the service to send a message
            message = chatroom_service.send_message(sender_id, chatroom_id, content)

            # Return a JSON response with the sent message details
            return JsonResponse({
                'status': 'success',
                'message': 'Message sent successfully',
                'message_details': {
                    'id': message.id,
                    'sender_id': message.sender.id,
                    'content': message.content,
                    'timestamp': message.timestamp
                }
            })

        except ValueError as e:
            # Handle the case where there is an error in sending the message
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@csrf_exempt
def list_messages(request, chatroom_id):
    if request.method == 'GET':
        try:
            # Call the service to list messages
            messages = chatroom_service.list_messages(chatroom_id)

            # Serialize the messages data
            serialized_messages = [{
                'id': message.id,
                'sender_id': message.sender.id,
                'content': message.content,
                'timestamp': message.timestamp
            } for message in messages]

            # Return a JSON response with the list of messages
            return JsonResponse({
                'status': 'success',
                'message': 'Messages retrieved successfully',
                'messages': serialized_messages
            })

        except ValueError as e:
            # Handle the case where there is an error in listing messages
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})