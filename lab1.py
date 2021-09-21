import random


def check_choice(letter):
    check_letter = letter.replace('.', '')
    return int(check_letter)

def Help():
    return "--------Введите номер ответа, который Вы считаете правильным, чтобы продолжить тестирование.--------" \
           "\n--------Введите exit, для выхода из программы.------------------------------------------------------" \
           "\n--------Введите start, для того, чтобы начать сначала.----------------------------------------------"

def start():
    number = random.randint(1,10)
    if number == 1:
        print(question_1())
    elif number == 2:
        print(question_2())
    elif number == 3:
        print(question_3())
    elif number == 4:
        print(question_4())
    elif number == 5:
        print(question_5())
    elif number == 6:
        question_6()
    elif number == 7:
        question_7()
    elif number == 8:
        question_8()
    elif number == 9:
        question_9()
    elif number == 10:
        question_10()


def exit():
    raise SystemExit

def question_1():
    question = "\nВ каком году произошло восстание декабристов в Петербурге?"
    choice_1 = " 1. 1825+\n"
    choice_2 = "2. 1812\n"
    choice_3 = "3. 1819\n"
    choice_4 = "4. 1846"
    print(question)
    print(choice_1,choice_2,choice_3,choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 1
    elif letter == 2:
        return 0
    elif letter == 3:
        return 0
    elif letter == 4:
        return 0

def question_2():
    question = "\nКакой из этих городов не является столицей?"
    choice_1 = " 1. Богота\n"
    choice_2 = "2. Панама+\n"
    choice_3 = "3. Бишкек\n"
    choice_4 = "4. Гаага"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 1
    elif letter == 3:
        return 0
    elif letter == 4:
        return 0
    return True

def question_3():
    question = "\nНазовите автора этих строк: “В раннем детстве верил я, что от всех болезней капель Датского короля не найти полезней”."
    choice_1 = " 1. Илья Эренбург\n"
    choice_2 = "2. Булат Окуджава+\n"
    choice_3 = "3. Александр Блок\n"
    choice_4 = "4. Иван Крылов"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 1
    elif letter == 3:
        return 0
    elif letter == 4:
        return 0
    return True

def question_4():
    question = "\nКак называется энергия, сосредоточенная в основании позвоночника человека?"
    choice_1 = " 1. Джаграт\n"
    choice_2 = "2. Кундалини+\n"
    choice_3 = "3. Даршана\n"
    choice_4 = "4. Умари"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 1
    elif letter == 3:
        return 0
    elif letter == 4:
        return 0
    return True

def question_5():
    question = '\nКакое из этих слов написано правильно?'
    choice_1 = " 1. Суббстанция\n"
    choice_2 = "2. Полемика+\n"
    choice_3 = "3. Дедактика\n"
    choice_4 = "4. Колизия"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 1
    elif letter == 3:
        return 0
    elif letter == 4:
        return 0
    return True

def question_6():
    question = '\nВ какой стране находится древний город Эфес?'
    choice_1 = " 1. ОАЭ\n"
    choice_2 = "2. Египет\n"
    choice_3 = "3. Греция\n"
    choice_4 = "4. Турция+"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 0
    elif letter == 3:
        return 0
    elif letter == 4:
        return 1
    return True

def question_7():
    question = '\nИз чего делают манку?'
    choice_1 = " 1. Из овса\n"
    choice_2 = "2. Из рапса\n"
    choice_3 = "3. Из манки\n"
    choice_4 = "4. Из пшена+"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 0
    elif letter == 3:
        return 0
    elif letter == 4:
        return 1
    return True

def question_8():
    question = '\nКак называется прямая, проходящая через вершину угла и делящая его пополам?'
    choice_1 = " 1. Гипотенуза\n"
    choice_2 = "2. Биссектриса+\n"
    choice_3 = "3. Высота\n"
    choice_4 = "4. Просто прямая"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 1
    elif letter == 3:
        return 0
    elif letter == 4:
        return 0
    return True

def question_9():
    question = '\nСамое глубокое в мире озеро?'
    choice_1 = " 1. Восток\n"
    choice_2 = "2. Каспийское море\n"
    choice_3 = "3. Байкал+\n"
    choice_4 = "4. Сан-Мартин"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 0
    elif letter == 2:
        return 0
    elif letter == 3:
        return 1
    elif letter == 4:
        return 0
    return True

def question_10():
    question = '\nСколько градусов в белом вине?'
    choice_1 = " 1. 9-12+\n"
    choice_2 = "2. 13-16\n"
    choice_3 = "3. 17-19\n"
    choice_4 = "4. 5-8"
    print(question)
    print(choice_1, choice_2, choice_3, choice_4)
    letter_to_check = input("Номер ответа: ")
    letter = check_choice(letter_to_check)
    if letter == 1:
        return 1
    elif letter == 2:
        return 0
    elif letter == 3:
        return 0
    elif letter == 4:
        return 0
    return True

print(Help())
start()
