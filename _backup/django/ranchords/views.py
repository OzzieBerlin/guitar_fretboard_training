from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def funk(request):
    return render(request, 'ranchords/funky_website.html')

def home(request):

    notes = ["A", "B", "C", "D", "E", "F", "G"]
    accidentals = ["", "b", "#"]
    chord_characters = ["", "min", "aug", "dim"]
    random_chords = []

    def get_random_chord(chord, accidental, chord_character):
        chord = random.choice(notes)
        accidental = random.choice(accidentals)
        chord_character = random.choice(chord_characters)
        return chord + accidental + chord_character

    num_of_chords = 12
    user_choice = int(request.GET.get('range', 16))

    for num in range(user_choice):
        random_chords.append(get_random_chord(notes, accidentals, chord_characters))

    return render(request, 'ranchords/index.html', {'ranchords': random_chords, 'num_chords': num_of_chords, 'user_choice': user_choice})
