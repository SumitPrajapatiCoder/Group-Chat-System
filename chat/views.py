from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Message
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import json
from django.utils.timezone import localtime
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist

@never_cache
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home') 
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            return render(request, 'chat/register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'chat/register.html', {'error': 'Email already exists'})

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    
    return render(request, 'chat/register.html')



@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 
    
    if request.method == "POST":
        identifier = request.POST.get("identifier")  
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=identifier)
            username = user.username
        except User.DoesNotExist:
            username = identifier 

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'chat/login.html')



@login_required
def index(request):
    if request.method == "POST":
        sender = request.user.username
        content = request.POST.get("content")
        Message.objects.create(sender=sender, content=content)
    return render(request, 'chat/index.html')



@login_required
def room(request):
    try:
        profile = Profile.objects.get(user=request.user)
        if profile.is_blocked:
            return render(request, 'chat/room.html', {'blocked': True})
    except Profile.DoesNotExist:
        pass 

    if request.method == "POST":
        content = request.POST.get("content")
        sender = request.user.username
        if content:
            Message.objects.create(sender=sender, content=content)
            return redirect('room')

    return render(request, 'chat/room.html')





@login_required
def get_messages(request):
    try:
        profile = Profile.objects.get(user=request.user)
        if profile.is_blocked:
            return JsonResponse({'messages': [], 'error': 'You are blocked'}, status=403)
    except Profile.DoesNotExist:
        pass  

    messages = Message.objects.all().order_by('timestamp')
    return JsonResponse({
        'messages': [
            {
                'id': msg.id,
                'sender': msg.sender,
                'content': msg.content,
                'timestamp': localtime(msg.timestamp).strftime('%I:%M %p') 
            }
            for msg in messages
        ]
    })



@csrf_exempt
@login_required
def clear_messages(request):
    if request.method == "POST":
        data = json.loads(request.body)
        scope = data.get("scope")

        if request.user.is_superuser and scope == "all":
            Message.objects.all().delete()
            return JsonResponse({"status": "cleared-all"})

        elif scope == "own":
            Message.objects.filter(sender=request.user).delete()
            return JsonResponse({"status": "cleared-own"})

        return JsonResponse({"status": "unauthorized"}, status=403)


def logout_view(request):
    auth_logout(request)
    return redirect('login')

def back(request):
   if request.user.is_authenticated:
        return redirect('home')


@csrf_exempt
@login_required
def edit_message(request, message_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_content = data.get('content')
            msg = Message.objects.get(id=message_id, sender=request.user.username)
            msg.content = new_content
            msg.save()
            return JsonResponse({'status': 'updated'})
        except Message.DoesNotExist:
            return JsonResponse({'error': 'Message not found or permission denied'}, status=403)




User = get_user_model()

@login_required
@user_passes_test(lambda u: u.is_superuser)
def list_users_json(request):
    users = User.objects.filter(is_superuser=False).values('id', 'username', 'email')
    enriched = []
    for user in users:
        try:
            profile = Profile.objects.get(user_id=user['id'])
            user['is_blocked'] = profile.is_blocked
        except ObjectDoesNotExist:
            user['is_blocked'] = False
        enriched.append(user)
    return JsonResponse({'users': enriched})


@require_POST
@login_required
@user_passes_test(lambda u: u.is_superuser)
def toggle_block_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        if user.is_superuser:
            return JsonResponse({'error': 'Cannot block a superuser'}, status=403)

        profile, created = Profile.objects.get_or_create(user=user)
        profile.is_blocked = not profile.is_blocked
        profile.save()
        return JsonResponse({'status': 'success', 'is_blocked': profile.is_blocked})

    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)




