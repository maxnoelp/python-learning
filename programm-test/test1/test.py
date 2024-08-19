name_list = []

with open('test1.txt', 'a+', encoding='utf8') as file:
    file.seek(0)
    name_list = [line.rstrip() for line in file]
    file.close

def print_name(name):
    if name in name_list:
        print('Moinsen', name)
    else:
        print('kenn ich nicht', name)
        name_list.append(name)
        

while True:
    name = input("Wie heist du? ").capitalize()
    if name == 'Q':
        break
    elif name == 'L':
        print(name_list)
    elif name == 'S':
        with open('test1.txt', 'w+', encoding='utf8') as file:
            file.write('\n' .join(name_list))
        file.close
    elif name == 'D':
        print(name_list)
        del_name = input('Wer darfs denn sein?').capitalize()
        if del_name in name_list:
            name_list.remove(del_name)
    else:
        print_name(name)