# print("Hello World")

#name = input("Wie ist dein Name?") # wartet auf Benutzer eingabe
# variable erstellen und ausgeben
#print(name)
name_list = []

with open('liste.txt', 'a+', encoding='utf8') as file:   #liest aus einer Textdatei, a = ist lesen und schreiben, + = fügt es hinzu
    file.seek(0)      
    #ein zeiler zum öffnen der Datei für for schleife
    name_list = [line.rstrip() for line in file]                
    # for line in file:                 #ohne fängt es unten an, mit seek fängt es von oben an zu lesen
    #     line = line.strip()           #for-schleife verwendet um jede linie in der Datei zu lesen     
    #     name_list.append(line)        #strip = schneidet leerzeichen weg, steuerzeichen werden auch weggeschnitten um reinen Text zu lesen
    file.close


#function in py / auf den einzug achten, zieht nicht automatisch rüber!!!
def print_name(name):
    if name in name_list:
        print('Schön dich zu sehen,', name)
    else:
        print('Hallo', name, 'Du bist neu hier')
        name_list.append(name)
        name_list.sort()        #liste wird alpahbetisch geordnet, mit reverse=true, andersrum
# doppelpunkt ist für {} wie bei js

#für mehrfaches wiederholen eine while schleife! muss aber durch function beendet werden!
while True:
    name = input("Wie ist dein Name? ").capitalize() #erster Buchstabe ist immer groß geschrieben
    if name == 'Q':                #hier wird gesagt, wenn man den Buchstaben Q eingibt soll das programm sich schließen
        break
    elif name == 'L':              #hier wird gesagt bei der eingaben l wird die Liste ausgegeben
        print(name_list)
    elif name == 'S':
        with open('liste.txt', 'w+', encoding='utf8') as file:   #liste wird geöffnet um darin zu schreiben, w+ = liste wird gelöscht und komplett neugeschrieben
            file.write('\n' .join(name_list))   #name wird in die Liste geschrieben, \ = es kommt ein steuerzeichen, n = newLine
        file.close
    elif name == 'D':
        print(name_list)
        del_name = input('Welcher Name?').capitalize()
        if del_name in name_list:  
            name_list.remove(del_name)
    else:
        print_name(name)

#mit dem roten stop punkt kann man sagen wo der code stoppen soll und dann kann man mit debuggen sehen wo was passiert!