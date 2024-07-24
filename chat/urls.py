from django.urls import path
from chat.views import chatbot

urlpatterns = [
    path("", chatbot, name="chat"),
]