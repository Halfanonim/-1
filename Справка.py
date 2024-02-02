

def post_data():
    with open("Справочник.txt",'r+') as file:
        file.seek(0)
        r=file.readlines()
        for x in r:
            print(x)
post_data()

def add_data():
    f=[]
    s=True
    while s==True:
        k=input("Введите через запятую фамилию, имя, отчество и номер телефона: ")
        t=k.split(',')
        f.append(t)
        o=input("Хотите еще что нибудь ввести? Напишите 'Да' или 'Нет': ")
        if o=="Нет":
            s=False
    with open("Справочник.txt",'r+') as file:
        file.seek(0)
        r=file.readlines()
        file.seek(0,2)
        t1=1
        for x in f:
            for x1 in x:
                if x1==x[0]:
                    file.writelines(str((len(r)+t1))+" "+x1+" ")
                    t1=t1+1
                else:
                    file.writelines(x1+" ")
            file.write("\n")
    post_data()
def find_data():
    t=0
    f=[]
    with open("Справочник.txt",'r+') as file:
        file.seek(0)
        r=file.readlines()
        for x in r:
            x2=x.split(" ")
            f.append(x2)    
    s=True
    while s==True:
        k=input("Введите, по какому параметру вы хотите найти запись: ")
        if k=="Порядковый номер записи":
            t=0
        elif k=="Фамилия":
            t=1
        elif k=="Имя":
            t=2
        elif k=="Отчество":
            t=3
        elif k=="Номер телефона":
            t=4
        else:
            print("Введите номер!")
            s=False
        k1=input("Введите данные для поиска записи: ")
        t2=0
        for x in f:
            if x[t]==k1:
                t2=1
                for x4 in x:
                    print(x4,end=" ")
                break
        if t2==0:
            print("Вхождения не найдено")
        k4=input("Хотите найти какую либо еще запись? ")
        if k4=="Нет":
            s=False
def diff_file():
    t=0
    f=[]
    with open("Справочник.txt",'r+') as file:
        file.seek(0)
        r=file.readlines()
        for x in r:
            x2=x.split(" ")
            f.append(x2)    
    k=input("Введите название другого фаила: ")
    k1=input("Введите номер строки: ")
    t2=0
    for x in f:
        if x[0]==k1:
            with open(f"{k}",'w') as file:
                for x1 in x:
                    file.write(x1+" ")
            t2=1
            break
    if t2==0:
        print("Совпадений не найдено")

    


f1=True
while f1==True:
    f2=input("Вы хотите что нибудь сделать с этим справочником? Да или Нет?: ")
    if f2=="Нет":
        f1=False
    else:
        f3=input("""Что вы хотите сделать?
                1-Добавить пользователей?
                2-Найти запись
                3-Копировать строку в другой фаил
                4-Ничего """)
        if f3=="1":
            add_data()
        elif f3=="2":
            find_data()
        elif f3=="3":
            diff_file()

        
