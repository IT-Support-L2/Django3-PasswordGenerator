from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    punc = "!#($%&*+}-/<=)>?@[\]^{|"
    Length = int(request.GET.get('length'))
    uchars = int(Length / 4)
    lchars = int(Length / 4)
    dchars = int(Length / 4)
    schars = int(Length / 4)
    characters = []
    str_uchars, str_lchars, str_dchars, str_schars = '', '', '', ''

    for i in range(lchars):
        if request.GET.get('lowercase'):
            str_lchars += random.SystemRandom().choice(string.ascii_lowercase)
           
    for i in range(uchars):
        if request.GET.get('uppercase'):
            str_uchars += random.SystemRandom().choice(string.ascii_uppercase)
           
    for i in range(dchars):
        if request.GET.get('numbers'):
            str_dchars += random.SystemRandom().choice(string.digits)
        
    for i in range(schars):
        if request.GET.get('special'):
            str_schars += random.SystemRandom().choice(punc)
                 
    random_str = str_uchars + str_lchars + str_dchars + str_schars

    random_str = ''.join(random.sample(random_str, len(random_str)))

    l = list(random_str)

    random.shuffle(l)

    result = ''.join(l)

    characters.extend(result)

    thepassword = ""

    for i in characters:
        thepassword += str(i)
       
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
