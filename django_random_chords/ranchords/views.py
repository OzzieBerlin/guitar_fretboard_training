from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

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

    for num in range(num_of_chords):
        random_chords.append(get_random_chord(notes, accidentals, chord_characters))

    return render(request, 'ranchords/index.html', {'ranchords': random_chords})

def funk(request):
    return HttpResponse('WHAT THE FUNK!!!')



