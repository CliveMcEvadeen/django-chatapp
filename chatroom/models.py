from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name=models.CharField(max_length=50)
    # Add additional fields for user profile information
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    handle = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user.username

class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.pk}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in Conversation {self.conversation.pk}"

class AssistantMessage(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assistant's message in Conversation {self.conversation.pk}"

class GroupChat(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='group_chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupMessage(models.Model):
    group_chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in Group Chat {self.group_chat.name}"
