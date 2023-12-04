# tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from chat.entities.models import ChatRoom

class ChatroomViewTests(TestCase):
    def test_list_chatrooms_view(self):
        # Create a test chatroom
        chatroom = ChatRoom.objects.create(name="Test Chatroom", max_members=10)

        # Fetch the list_chatrooms URL
        url = reverse('list_chatrooms')

        # Make a GET request to the list_chatrooms view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the test chatroom is present in the response content
        self.assertContains(response, "Test Chatroom")
