from django.shortcuts import render, redirect
from django.http import JsonResponse
import os
import json

# 1. Home View
def home_view(request):
    return render(request, 'home.html')

# 2. CV View
def CV_view(request):
    return render(request, 'cv.html')

# 3. Research View
def Research_view(request):
    return render(request, 'research.html')

# 4. Teaching View
def Teaching_view(request):
    return render(request, 'teaching.html')

# 5. Home View
def Contact_view(request):
    return render(request, 'contact.html')
