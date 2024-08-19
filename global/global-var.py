my_string = 'global' # eine globale Variable

def my_function(my_string):  #eine function mit einem Parameter der übergeben wird
    my_string += 'local' #die globale Variable wird 'verheiratet' mit 'local'
    return my_string #die globale variable gibt bei ausegeben jetzt 'gloablloval' aus

print(my_function(my_string)) #ausgabe auf der Console


#Mutable / Imutable
#mit 'id' den Speicherort anzeigen
#Die Variable 'string' wird an einem neuen Ort gespeichert
#liste aber nicht

# def check_id():
#     my_string = 'Hallo'     #neue String variable
#     print(id(my_string))    #zeigt nicht den inhalt sondern die ID/memoryID

#     my_string += 'Welt'     #zur gleichen variable etwas hinzugefügt
#     print(id(my_string))

#     my_list = ['Hallo']     #neue Liste
#     print(id(my_list))

#     my_list[0] += ('Welt')  #etwas in dem ersten eintrag hinzugefügt
#     print(id(my_list))
#     print(my_list)

#     my_list += ['Max']
#     print(my_list)

#     my_list2 = my_list.copy #erstellt eine Copy von my_list, somit kann man die neue var anpassen ohne dass sich was im original ändert
#     print(id(my_list2))

# check_id()


def greet():
    return print("hello World!")

greet()