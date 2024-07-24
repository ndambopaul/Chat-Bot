from django.shortcuts import render

# Create your views here.
# chat/views.py
from django.shortcuts import render
import requests
from chat.models import Message
from django.utils import timezone
from django.http import JsonResponse

def chatbot(request):
    messages = request.session.get("chat_history", [])
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": user_message})
        bot_response = response.json()

        # Save the user's message
        message = Message.objects.create(user='user', content=user_message, timestamp=timezone.now())
        
        # Save the bot's response
        if bot_response:
            bot_text = bot_response[0].get('text', '')
            message.response = bot_text
            message.save()

            messages_list = []
            if isinstance(messages, dict):
                messages_list.append(messages)

                new_chat_data = {
                    "text": user_message,
                    "response": bot_text
                }     
                messages_list.append(new_chat_data)

                request.session["chat_history"] = messages_list
            else:
                new_chat_data = {
                    "text": user_message,
                    "response": bot_text
                } 
                messages.append(new_chat_data)
                request.session["chat_history"] = messages

        # Fetch all messages
    # Fetch all messages
    return render(request, 'chat.html', {'messages': messages})
