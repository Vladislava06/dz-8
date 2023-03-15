# r - только чтение файла 
# a - дозапись файла 
# w - перезапись файла

#file_name = 'data.txt'

def show_data(): # Содержимое
    with open('data.txt', 'r', encoding ='utf-8') as file:
       return file.read().split('\n')

def new_data(): # Новая инфа
    with open('data.txt', 'a', encoding ='utf-8') as file:
        file.write(input('Введите данные: ') + '\n')

def find_data(): # Поиск
    with open('data.txt', 'r', encoding ='utf-8') as file:
        book = file.read().split('\n')
        temp = input()
        for i in book:
            if temp in i:
                print(i)

def delete_data(): #Удаление
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        find = input('Введите данные контакта, который хотите удалить: ')
        index = 0
        temp = list()
        for i in book:
            if find.lower() in i.lower():
                print(f'Ведитете "{index}" чтобы удалить контакт "{i}"')
                temp.append(i)
            index +=1
        if bool(temp):
            del_index = int(input(""))
            book.pop(del_index)    
            with open('data.txt', 'w', encoding='utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('Такого контакта нет')

def modi_data(): # Изменение 
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        find = input('Введите данные контакта который хотите изменить: ')
        index = 0
        temp = list()
        for i in book:
            if find.lower() in i.lower():
                print(f'Ведитете "{index}" чтобы удалить контакт "{i}"')
                temp.append(i)
            index +=1
        if bool(temp):
            remake_index = int(input(""))
            book[remake_index] = new_data()    
            with open('data.txt', 'w', encoding='utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('Такого контакта нет')

while True:
    mode = input('Выберите режим работы справочника: ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '4':
        delete_data()
    elif mode == '5':
        modi_data()
    elif mode == '0':
        break
    else:
        print('No mode')