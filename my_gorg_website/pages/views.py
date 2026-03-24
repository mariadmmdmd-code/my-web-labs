from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

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