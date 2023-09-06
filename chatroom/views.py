from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import UserProfile, Conversation, Message, AssistantMessage, GroupChat, GroupMessage,
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def group_chat(request, group_id):
    '''get group chat'''
    group = get_object_or_404(GroupChat, id=group_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            GroupMessage.objects.create(group_chat=group, sender=request.user, content=content)
            return JsonResponse({"status": "Message sent successfully"})
        else:
            return JsonResponse({"status": "Message content is empty"}, status=400)
    group_messages = GroupMessage.objects.filter(group_chat=group)
    return render(request, 'group_chat.html', {"group": group, "group_messages": group_messages})

@login_required
def delete_group_chat(request, group_id):
    group = get_object_or_404(GroupChat, id=group_id)
    if request.method == 'POST':
        group.delete()
        return JsonResponse({"status": "Group chat deleted successfully"})
    else:
        return HttpResponse(status=405)  # Method Not Allowed

@login_required
def create_group_chat(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            group = GroupChat.objects.create(name=name)
            group.members.add(request.user)
            return redirect('group_chat', group_id=group.id)
        else:
            return JsonResponse({"status": "Group chat name is required"}, status=400)
    return render(request, "create_group_chat.html")

@login_required
def retrieve_group_chat(request):
    user = request.user
    group_chats = user.group_chats.all()
    return render(request, "retrieve_group_chat.html", {"group_chats": group_chats})

@login_required
def group_profile(request, group_id):
    group = get_object_or_404(GroupChat, id=group_id)
    return render(request, "group_profile.html", {"group": group})

@login_required
def single_chat(request, username):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            other_user = get_object_or_404(User, username=username)
            conversation = Conversation.get_or_create_private_conversation(request.user, other_user)
            Message.objects.create(conversation=conversation, sender=request.user, content=content)
            return JsonResponse({"status": "Message sent successfully"})
        else:
            return JsonResponse({"status": "Message content is empty"}, status=400)
    other_user = get_object_or_404(User, username=username)
    conversation = Conversation.get_or_create_private_conversation(request.user, other_user)
    messages = Message.objects.filter(conversation=conversation)
    return render(request, 'single_chat.html', {"other_user": other_user, "messages": messages})

@login_required
def delete_single_chat(request, username):
    other_user = get_object_or_404(User, username=username)
    conversation = Conversation.get_or_create_private_conversation(request.user, other_user)
    if request.method == 'POST':
        conversation.delete()
        return JsonResponse({"status": "Private chat deleted successfully"})
    else:
        return HttpResponse(status=405)  # Method Not Allowed

@login_required
def create_single_chat(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            other_user = get_object_or_404(User, username=username)
            conversation = Conversation.get_or_create_private_conversation(request.user, other_user)
            return redirect('single_chat', username=other_user.username)
        else:
            return JsonResponse({"status": "Username is required"}, status=400)
    return render(request, "create_single_chat.html")

@login_required
def retrieve_single_chat(request, username):
    other_user = get_object_or_404(User, username=username)
    conversation = Conversation.get_or_create_private_conversation(request.user, other_user)
    messages = Message.objects.filter(conversation=conversation)
    return render(request, "retrieve_single_chat.html", {"other_user": other_user, "messages": messages})

@login_required
def assistant_connect(request):
    # Implement the logic to connect to the GPT engine using the provided API
    if request.method == 'POST':
        api_key = request.POST.get('api_key')
        if api_key:
            # Implement the connection logic here
            return JsonResponse({"status": "Connected to GPT engine successfully"})
        else:
            return JsonResponse({"status": "API key is required"}, status=400)
    return render(request, "assistant_connect.html")

@login_required
def monitor_chat(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    assistant_messages = AssistantMessage.objects.filter(conversation=conversation)
    return render(request, "monitor_chat.html", {"assistant_messages": assistant_messages})

@login_required
def get_request(request, request_id):
    # Implement logic to retrieve a specific request made to the assistant
    return render(request, "get_request.html")

@login_required
def send_request(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            AssistantMessage.objects.create(conversation=conversation, content=content)
            return JsonResponse({"status": "Request sent successfully"})
        else:
            return JsonResponse({"status": "Request content is empty"}, status=400)
    return render(request, "send_request.html")

@login_required
def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, "user_profile.html", {"user_profile": user_profile})

@login_required
def logout_user(request):
    # Implement logic to log the user out
    # You can use Django's built-in logout function
    from django.contrib.auth import logout
    logout(request)
    return redirect('logout_success')

@login_required
def update_profile(request):
    if request.method == 'POST':
        # Implement logic to update user profile information
        user_profile = get_object_or_404(UserProfile, user=request.user)
        user_profile.bio = request.POST.get('bio', user_profile.bio)
        user_profile.profile_picture = request.FILES.get('profile_picture', user_profile.profile_picture)
        user_profile.save()
        return redirect('profile_updated')  # Redirect to a profile updated confirmation page
    return render(request, "update_profile.html")

