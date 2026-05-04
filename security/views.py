from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import json  
import hashlib
import bcrypt
import hashlib
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import PasswordSerializer, RainbowChallengeSerializer
from .utils import process_password, get_attack_info


COMMON_PASSWORDS = [
    "password", "123456", "admin", "qwerty", "12345678", 
    "football", "welcome", "shadow", "dragon", "baseball"
]


def home(request):
    return render(request, "index.html")

def lab_page(request):
    return render(request, "lab.html")

def strength_page(request):
    return render(request, "strength.html")

def rainbow_page(request):
    
    target = random.choice(COMMON_PASSWORDS)
    request.session['rainbow_target'] = target
    
   
    target_hash = hashlib.sha256(target.encode()).hexdigest()
    
    return render(request, "rainbow.html", {"target_hash": target_hash})

@csrf_exempt
def process_lab(request):
    if request.method == "POST":
        data = json.loads(request.body)
        password = data.get("password", "").strip().lower()
        method = data.get("method", "plain")
        
        
        is_common = password in COMMON_PASSWORDS
        
        result = {}
        
        attack = {"status": "VULNERABLE", "time": "Hesablanır..."}

       
        if method == "plain":
            h_val = password
            time = "0.00001 ms"
            status = "LEAKED"
            
        elif method == "sha256":
            h_val = hashlib.sha256(password.encode()).hexdigest()
            time = "5 saniyə" if not is_common else "0.001 ms"
            status = "CRACKED" if is_common else "VULNERABLE"
            
        elif method == "salted":
            salt = "cyber_lab_salt_"
            h_val = hashlib.sha256((salt + password).encode()).hexdigest()
            time = "24 saat" if not is_common else "0.1 ms"
            status = "MEDIUM RISK" if not is_common else "CRACKED"
            
        elif method == "bcrypt":
            h_val = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            time = "300+ İl" if not is_common else "0.5 ms"
            status = "SECURED" if not is_common else "BYPASSED"

        
        if is_common:
            attack["time"] = "Dərhal (Lüğət hücumu)"
            attack["status"] = "LEAKED (Common Password)"
            attack["is_popular"] = True
        else:
            attack["time"] = time
            attack["status"] = status
            attack["is_popular"] = False

        result["hash"] = h_val

        return JsonResponse({
            "result": result,
            "attack": attack
        })
        
def try_it(request):
    return render(request, "try.html")

# --- API Məntiqi ---
class PasswordProcessView(APIView):
    def post(self, request):
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data["password"]
            method = serializer.validated_data["method"]
            
            result = process_password(password, method)
            attack_info = get_attack_info(method)

            return Response({
                "input_password": password,
                "method": method.upper(),
                "result": result,
                "attack": attack_info
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RainbowChallengeView(APIView):
    def post(self, request):
        serializer = RainbowChallengeSerializer(data=request.data)
        if serializer.is_valid():
            guess = serializer.validated_data["guess"].strip().lower()
            
           
            current_target = request.session.get('rainbow_target')
            
           
            if not current_target:
                current_target = random.choice(COMMON_PASSWORDS)
                request.session['rainbow_target'] = current_target
                request.session['attempt_count'] = 0

            current_target_hash = hashlib.sha256(current_target.encode()).hexdigest()
            
            
            if guess == current_target:
               
                request.session['rainbow_target'] = None
                request.session['attempt_count'] = 0
                return Response({
                    "success": True, 
                    "message": f"TƏBRİKLƏR! PAROL '{current_target}' İDİ."
                })

            
            attempts = request.session.get('attempt_count', 0) + 1
            request.session['attempt_count'] = attempts
            
            
            revealed_part = current_target[:attempts]
            
            return Response({
                "success": False, 
                "message": "ACCESS DENIED!",
                "new_hash": current_target_hash,
                "hint": {
                    "length": len(current_target),
                    "revealed": revealed_part,
                    "next_char_index": attempts
                }
            })