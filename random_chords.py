# Function of this project will be: Create random Chords to practice triads on the guitar. This way a practicing, advancing guitarist will become better very quick by getting better command of the guitar fretboard.
# This project is intended for: My first own commit on Github, practicing code and putting knowledge into practice.

#since the chords are going to be generated randomly, this project needs the random module.

import random

# There are seven notes represented by a letter in music theory
notes = ["A", "B", "C", "D", "E", "F", "G"]

# Each letter may have a # (sharp) or a b (flat) as an accidental, which alters the pitch
accidentals = ["", "b", "#"]

# Each chord can either be major (no additional text), minor (represented with a "min" (or "-")), augmented ("aug" or "+") or diminished ("dim" or "0").

chord_characters = ["", "min", "aug", "dim"]

# In the next step I want to prepare a list which I can print to the console / where I will add the randomly generated chords.

random_chords = []

# My next step is creating a function which will generate a random chord.

def get_random_chord(chord, accidental, chord_character):
    chord = random.choice(notes)
    accidental = random.choice(accidentals)
    chord_character = random.choice(chord_characters)
    return chord + accidental + chord_character

# The next variable will determine how many chords are going to be in the "random_chords"-list, thus how intense my practice session (as a burst) is going to be.

num_of_chords = 12

# Now I need to add the number of chords into the "random_chords"-list. I will do that with a loop.

for num in range(num_of_chords):
    random_chords.append(get_random_chord(notes, accidentals, chord_characters))



# Now my generator should work with a print-statement! :)

print(random_chords)


# Further ideas:
# Would it make sense to add a class? (to apply OOP)
# Instead of three lists I could also use a dictionary with three "key: value"-pairs!
# Add logic of exceptions such as avoiding Cb or E#
# change output so that it prints on a website or alike e.g. with Django Framework
