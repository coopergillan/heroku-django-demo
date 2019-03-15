import os
import random

from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Greeting

GREETING_NOUNS = (
    'Friend', "Buddy ol' pal", 'Companion', 'Boon companion', 'Best friend',
    'Close friend', 'Intimate', 'Confidante', 'Confidant', 'Familiar', 'Soul mate',
    'Alter ego', 'Second self', 'Shadow', 'playmate', 'Playfellow',
    'Classmate', 'Schoolmate', 'Workmate', 'Ally', 'Comrade', 'Associate',
    'Sister', 'Brother', 'Pal', 'Bosom pal', 'Buddy', 'Bosom buddy', 'Chum',
    'Spar', 'Sidekick', 'Cully', 'Crony', 'Main man', 'Bezzie', 'Mate', 'Oppo',
    'China', 'Mucker', 'Butty', 'Bruvver', 'Bruv', 'Marrow', 'Marrer', 'Marra',
    'Amigo', 'Compadre', 'Paisan', 'Homie', 'Bro', 'Homeboy', 'Homegirl',
    'Gabba', 'Offsider',
)

def get_greeting_noun():
    return random.choice(GREETING_NOUNS)


# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Hello! ' * times)


def db(request):
    greeting = Greeting(noun=get_greeting_noun())
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"current_greeting": greeting, "greetings": greetings})
