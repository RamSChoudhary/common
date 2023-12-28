from django.shortcuts import render
from django.http import HttpResponse
import string
import random

def print_hello(request):
    # return HttpResponse('Hello App')
    random = generate_random(15)
    context = {'random' : random}
    return render(request, 'hello.html', context)

def generate_random(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string