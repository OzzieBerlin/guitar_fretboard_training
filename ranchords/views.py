from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def funk(request):
    return render(request, 'ranchords/funky_website.html')

def home(request):
    return render(request, 'ranchords/index.html')

    # notes = ["A", "B", "C", "D", "E", "F", "G"]
    # accidentals = ["", "b", "#"]
    # chord_characters = ["", "min", "aug", "dim"]
    # random_chords = []

    # def get_random_chord(chord, accidental, chord_character):
    #     chord = random.choice(notes)
    #     accidental = random.choice(accidentals)
    #     chord_character = random.choice(chord_characters)
    #     return chord + accidental + chord_character

    # num_of_chords = 12
    # user_choice = int(request.GET.get('range', 16))

    # for num in range(user_choice):
    #     random_chords.append(get_random_chord(notes, accidentals, chord_characters))

    # return render(request, 'ranchords/index.html', {'ranchords': random_chords, 'num_chords': num_of_chords, 'user_choice': user_choice})



def random_chords(request):

    return_dictionary = {
        "notes": ["A", "B", "C", "D", "E", "F", "G"],
        "accidentals": " ",
        "chords": [""]
    }

    chords_aug_dim = ["aug", "dim"]

    if request.GET.get("accidentals"):
        return_dictionary["accidentals"] = ["", "b", "#"]

    if request.GET.get("chords-maj-min"):
        return_dictionary["chords"].append("min")

    if request.GET.get("chords-aug-dim"):
        return_dictionary["chords"].extend(chords_aug_dim)
    
    def get_random_chord():
        note = random.choice(return_dictionary.get("notes"))
        accidental = random.choice(return_dictionary.get("accidentals"))
        chord = random.choice(return_dictionary.get("chords"))
        return note + accidental + chord

    random_chords = []

    # num_of_chords = 20
    num_of_chords = int(request.GET.get('range'))
    for num in range(num_of_chords):
        ranchord = get_random_chord()
        cleaned_ranchord = ranchord.replace(" ", "")
        random_chords.append(cleaned_ranchord)

    return render(request, 'ranchords/random_chords.html', {'ranchords': random_chords, 'user_choice_of_num': num_of_chords})
