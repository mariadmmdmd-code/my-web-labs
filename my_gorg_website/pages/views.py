from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .forms import UserLoginForm, UserRegisterForm

def login_css(request):
    login_form = UserLoginForm()
    register_form = UserRegisterForm()
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('main')
            else:
                login_form = form
                
        elif action == 'register':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('main')
            else:
                register_form = form
    
    return render(request, 'pages/login_css.html', {
        'login_form': login_form,
        'register_form': register_form
    })


def login_js(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        action = data.get('action')
        
        if action == 'login':
            user = authenticate(
                username=data.get('username'),
                password=data.get('password')
            )
            if user:
                login(request, user)
                return JsonResponse({'status': 'ok', 'redirect': '/'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Неверные данные'}, status=400)
                
        elif action == 'register':
            # Создаём объект формы из данных
            form = UserRegisterForm(data)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return JsonResponse({'status': 'ok', 'redirect': '/'})
            else:
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = error_list[0]
                return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    
    return render(request, 'pages/login_js.html')

def main_page(request):
    return render(request, 'pages/main.html')

def page1(request):
    return render(request, 'pages/page1.html')

def page2(request):
    return render(request, 'pages/page2.html')

def page3(request):
    return render(request, 'pages/page3.html')

def login_page(request):
    return render(request, 'pages/login.html')

def login_css(request):
    return render(request, 'pages/login_css.html')

def login_js(request):
    return render(request, 'pages/login_js.html')

@csrf_exempt
def send_feedback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            
            if not message.strip():
                return JsonResponse({'status': 'error', 'error': 'Empty message'}, status=400)
            
            telegram_message = f"new message from my website:\n\n{message}"
            
            url = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage'
            payload = {
                'chat_id': settings.TELEGRAM_CHAT_ID,
                'text': telegram_message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'status': 'error', 'error': 'Telegram API error'}, status=500)
                
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'error': 'Method not allowed'}, status=405)