import random

return_dictionary = {
    "notes": ["A", "B", "C", "D", "E", "F", "G"], 
    "accidentals": "", 
    "chords": [""]
    }

accidentals = ["", "b", "#"]
chords_maj_min = ["min"]
chords_aug_dim = ["aug", "dim"]

return_dictionary["accidentals"] = accidentals
return_dictionary["chords"].extend(chords_maj_min)
return_dictionary["chords"].extend(chords_aug_dim)

num_of_chords = 20

def get_random_chord_django():
    note = random.choice(return_dictionary.get("notes"))
    accidental = random.choice(return_dictionary.get("accidentals"))
    chord = random.choice(return_dictionary.get("chords"))
    return note + accidental + chord

random_chords = []

for num in range(num_of_chords):
    random_chords.append(get_random_chord_django())

print(random_chords)
