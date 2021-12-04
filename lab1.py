from colorama import init
init()
from colorama import Fore, Back, Style

def check_choice(letter):
    check_letter = letter.replace('.', '')
    return int(check_letter)

def Help():
    return "--------Введите номер ответа, который Вы считаете правильным, чтобы продолжить тестирование.--------" \
           "\n --------Введите exit, для выхода из программы.------------------------------------------------------" \
           "\n --------Введите start, для того, чтобы начать сначала.----------------------------------------------"

def start():

    question1 = "Есть ли изображение на экране?(y/n)"
    question2 = "Подключены ли к сети монитор и системный блок?(y/n)"
    question3 = "Работает ли системный блок?(y/n)"
    question4 = "Исправен ли блок питания?(y/n)"
    question5 = "Подключен ли блок питания к материнской плате?(y/n)"
    question6 = "Подключен ли монитор к системному блоку?(y/n)"
    question7 = "Исправен ли монитор?(y/n)"
    question8 = "Исправна ли видеокарта?(y/n)"
    question9 = "Загружается ли операционная система?(y/n)"
    question10 = "Подключен ли жесткий диск к материнской плате?(y/n)"
    question11 = "Есть ли возможность войти в настройку BIOS?(y/n)"
    question12 = "Отображатся ли жесткий диск в BIOS?(y/n)"
    question13 = "Работают ли устройства ввода-вывода?(y/n)"
    question14 = "Работают ли переферийные устройства?(y/n)"

    answer4 = "Компьютер исправен"
    answer3 = "Требуется замена переферийного устройства"
    answer2 = "Требуется замена устройства ввода-вывода"
    answer9 = "Требуется переустановка операционной системы"
    answer8 = "Необходимо заменить жесткий диск"
    answer7 = "Требуется очистить CMOS"

    answer5 = "Требуется подключить жесткий диск к материнской плате"
    answer1 = "Требуется подключить к сети монитор и системный блок"
    answer6 = "Требуется замена блока питания"
    answer10 = "Требуется подключить блок питания"
    answer11 = "Требуется подключить монитор к системному блоку"
    answer12 = "Требуется замена монитора"
    answer13 = "Требуется замена видеокарты"
    answer14 = "Требуется замена материнской платы"

    print(question1)
    result1 = input()
    count = 0
    if result1 == "y":
        count = count + 1
        count = count + line1(question14,question13,question9,question10,question11,question12)
        if count == 2:
            print(answer2)
        elif count == 3:
            print(answer3)
        elif count == 4:
            print(answer4)
        elif count == 5:
            print(answer5)
        elif count == 7:
            print(answer7)
        elif count ==8:
            print(answer8)
        elif count == 9:
            print(answer9)
    elif result1 == "n":
        count = count + 0
        count = count + line2(question2,question3,question4,question5,question6,question7,question8)
        if count == 1:
            print(answer1)
        elif count == 6:
            print(answer6)
        elif count == 10:
            print(answer10)
        elif count == 14:
            print(answer14)
        elif count == 13:
            print(answer13)
        elif count == 12:
            print(answer12)
        elif count == 11:
            print(answer11)
    elif result1 == "start":
        start()
    elif result1 == "exit":
        exit()
    else:
        print(Fore.RED,"Неверный ввод!")
        start()




def line1(question14,question13,question9,question10,question11,question12):
    # -----------------------------------------------------
    print(question9)
    result1 = input()
    count = 0
    if result1 == "y":
        count += 1
        # -----------------------------------------------------
        print(question13)
        result2 = input()
        if result2 == "y":
            count += 1
            # -----------------------------------------------------
            print(question14)
            result3 = input()
            if result3 == "y":
                count += 1
                return count
            elif result3 == "n":
                count += 0
                return count
            if result3 == "start":
                start()
            elif result3 == "exit":
                exit()
            else:
                print(Fore.RED, "Неверный ввод!")
                start()
        elif result2 == "n":
            count += 0
            return count
        elif result2 == "start":
            start()
        elif result2 == "exit":
            exit()
        else:
            print(Fore.RED, "Неверный ввод!")
            start()
    elif result1 == "n":
        count += 2
        # -----------------------------------------------------
        print(question10)
        result4 = input()
        if result4 == "y":
            count += 2
            # -----------------------------------------------------
            print(question11)
            result5 = input()
            if result5 == "y":
                count += 2
                # -----------------------------------------------------
                print(question12)
                result6 = input()
                if result6 == "y":
                    count += 2
                    return count
                elif result6 == "n":
                    count += 1
                    return count
                elif result6 == "start":
                    start()
                elif result6 == "exit":
                    exit()
                else:
                    print(Fore.RED, "Неверный ввод!")
                    start()
            elif result5 == "n":
                count += 2
                return count
            elif result5 == "start":
                start()
            elif result5 == "exit":
                exit()
            else:
                print(Fore.RED, "Неверный ввод!")
                start()
        elif result4 == "n":
            count += 2
            return count
        elif result4 == "start":
            start()
        elif result4 == "exit":
            exit()
        else:
            print(Fore.RED, "Неверный ввод!")
            start()
    if result1 == "start":
        start()
    elif result1 == "exit":
        exit()
    else:
        print(Fore.RED, "Неверный ввод!")
        start()

def line2(question2,question3,question4,question5,question6,question7,question8):
    # -----------------------------------------------------
    print(question2)
    result1 = input()
    count = 0
    if result1 == "y":
        count += 2
        # -----------------------------------------------------
        print(question3)
        result2 = input()
        if result2 == "y":
            count += 2
            # -----------------------------------------------------
            print(question6)
            result3 = input()
            if result3 == "y":
                count += 2
                # -----------------------------------------------------
                print(question7)
                result4 = input()
                if result4 == "y":
                    count += 2
                    # -----------------------------------------------------
                    print(question8)
                    result5 = input()
                    if result5 == "y":
                        count += 6
                        return count
                    elif result5 == "n":
                        count += 5
                        return count
                    elif result5 == "start":
                        start()
                    elif result5 == "exit":
                        exit()
                    else:
                        print(Fore.RED, "Неверный ввод!")
                        start()
                elif result4 == "n":
                    count += 6
                    return count
                elif result4 == "start":
                    start()
                elif result4 == "exit":
                    exit()
                else:
                    print(Fore.RED, "Неверный ввод!")
                    start()
            elif result3 == "n":
                count += 7
                return count
            elif result3 == "start":
                start()
            elif result3 == "exit":
                exit()
            else:
                print(Fore.RED, "Неверный ввод!")
                start()
        elif result2 == "n":
            count += 2
            # -----------------------------------------------------
            print(question4)
            result6 = input()
            if result6 == "y":
                count += 2
                # -----------------------------------------------------
                print(question5)
                result7 = input()
                if result7 == "y":
                    count += 8
                    return count
                elif result7 == "n":
                    count += 4
                    return count
                elif result7 == "start":
                    start()
                elif result7 == "exit":
                    exit()
                else:
                    print(Fore.RED, "Неверный ввод!")
                    start()
            elif result6 == "n":
                count += 2
                return count
            elif result6 == "start":
                start()
            elif result6 == "exit":
                exit()
            else:
                print(Fore.RED, "Неверный ввод!")
                start()
        elif result2 == "start":
            start()
        elif result2 == "exit":
            exit()
        else:
            print(Fore.RED, "Неверный ввод!")
            start()
    elif result1 == "n":
        count += 1
        return count
    elif result1 == "start":
        start()
    elif result1 == "exit":
        exit()
    else:
        print(Fore.RED, "Неверный ввод!")
        start()


def exit():
    raise SystemExit


print(Fore.RED, Help())
start()


