from django.contrib import admin
from .models import User, Conversation,GroupChat, GroupMessage, AssistantMessage, Message, UserProfile


admin.site.register(Conversation)
admin.site.register(GroupChat)
admin.site.register(GroupMessage)
admin.site.register(AssistantMessage)
admin.site.register(Message)
admin.site.register(UserProfile)
