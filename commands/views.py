from django.shortcuts import render, redirect
from .models import Command
import random
import webbrowser as wb

helloList = ['hi there!', 'What\'s up', 'Hey, How are You?', "Hey what's going on?", 'Hi, I am Jarvis']
Myname = ['I am Jarvis', 'I\'m Jarvis', 'My name is Jarvis', 'People use to call me Jarvis', 'I\'m "Just A Rather Very Intelligent System" so you can call me JARVIS', 'Jarvis', 'Jarvis, what\'s yours?']
def home(request):
    return render(request, 'home.html', {'title':'home'})

def response(request, a):
    a = a.lower()
    r = ''
    if "how are you" in a:
        r = 'I am fine\n'

    if "what time is it" in a:
        r = r + 'its some time\n'

    if "where is" in a:
        r = r + 'somewhere in the world\n'
    if 'hello' in a or 'hi' in a:
        r = r + random.choice(helloList) + '\n'
    print(f"out: {r}")
    context = {'output':r}
    return render(request, 'output.html', context)

def testing(request, a):
    cmds = Command.objects.all()
    for cmd in cmds:
        r = ''
        if cmd.hotword in a or cmd.hotword2 in a:
            r = cmd.output + cmd.output2 + cmd.output3
    context = {'output':r}
    return render(request, 'output.html', context)
            