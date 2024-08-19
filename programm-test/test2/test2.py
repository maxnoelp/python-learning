import random

name_list = []
mittelalterliche_beleidigungen = [
    "Schandmaul",
    "Ruchloser Schelm",
    "Schuftiger Bauer",
    "Feiger Wicht",
    "Dummkopf",
    "Schurkischer Narr",
    "Geckenhafter Gimpel",
    "Wankelmütiger Tropf",
    "Törichter Tölpel",
    "Nichtsnutziger Knecht",
    "Trügerischer Gaukler",
    "Schändlicher Betrüger",
    "Ungeschlachter Lümmel",
    "Ehrloser Laffe",
    "Niederträchtiger Galgenstrick",
    "Müßiggänger",
    "Widerwärtiger Schurke",
    "Langweiliger Schwätzer",
    "Hinterhältiger Scharlatan",
    "Dreckiger Strolch"
]


def random_string():
    return random.choice(mittelalterliche_beleidigungen)

with open('test2.txt', 'a+', encoding='utf8') as file:
    file.seek(0)
    name_list = [line.rstrip() for line in file]
    file.close

def print_name(name):
    if name in name_list:
        print('Hallo,', name )
    else:
        print('schön dich zu sehen,', name)
        name_list.append(name)
        name_list.sort()

while True:
    name = input('Sprich rasch!').capitalize()
    if name == 'Q':
        break
    elif name  == 'L':
        print(name_list)
    elif name == 'Fynn':
        print(random_string())
    elif name == 'S':
        with open('test2.txt', 'w+', encoding='utf8') as file:
            file.write('\n' .join(name_list))
            file.close
    elif name == 'D':
        print(name_list)
        del_name = input('Für Gondor').capitalize()
        if del_name in name_list:
            name_list.remove(del_name)
    else:
        print_name(name)