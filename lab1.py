def Help():
    return "--------Введите номер ответа, который Вы считаете правильным, чтобы продолжить тестирование.--------" \
           "\n--------Введите exit, для выхода из программы.------------------------------------------------------" \
           "\n--------Введите start, для того, чтобы начать сначала.----------------------------------------------"

def start():
    question_1()

def exit():
    raise SystemExit

def question_1():
    question = "В каком году произошло восстание декабристов в Петербурге?"
    choice_1 = "1825+"
    choice_2 = "1812"
    choice_3 = "1819"
    choice_4 = "1846"
    return True

def question_2():
    question = "Какой из этих городов не является столицей?"
    choice_1 = "Богота"
    choice_2 = "Панама+"
    choice_3 = "Бишкек"
    choice_4 = "Гаага"
    return True

def question_3():
    question = "Назовите автора этих строк: “В раннем детстве верил я, что от всех болезней капель Датского короля не найти полезней”."
    choice_1 = "Илья Эренбург"
    choice_2 = "Булат Окуджава+"
    choice_3 = "Александр Блок"
    choice_4 = "Иван Крылов"
    return True

def question_4():
    question = "Как называется энергия, сосредоточенная в основании позвоночника человека?"
    choice_1 = "Джаграт"
    choice_2 = "Кундалини+"
    choice_3 = "Даршана"
    choice_4 = "Умари"
    return True

def question_5():
    question = 'Какое из этих слов написано правильно?'
    choice_1 = "Суббстанция"
    choice_2 = "Полемика+"
    choice_3 = "Дедактика"
    choice_4 = "Колизия"
    return True

def question_6():
    question = 'В какой стране находится древний город Эфес?'
    choice_1 = "ОАЭ"
    choice_2 = "Египет"
    choice_3 = "Греция"
    choice_4 = "Турция+"
    return True

def question_7():
    question = 'Из чего делают манку?'
    choice_1 = "Из овса"
    choice_2 = "Из рапса"
    choice_3 = "Из манки"
    choice_4 = "Из пшена+"
    return True

def question_8():
    question = 'Как называется прямая, проходящая через вершину угла и делящая его пополам?'
    choice_1 = "Гипотенуза"
    choice_2 = "Биссектриса+"
    choice_3 = "Высота"
    choice_4 = "Просто прямая"
    return True

def question_9():
    question = 'Самое глубокое в мире озеро?'
    choice_1 = "Восток"
    choice_2 = "Каспийское море"
    choice_3 = "Байкал+"
    choice_4 = "Сан-Мартин"
    return True

def question_10():
    question = 'Сколько градусов в белом вине?'
    choice_1 = "9-12+"
    choice_2 = "13-16"
    choice_3 = "17-19"
    choice_4 = "5-8"
    return True

print(Help())
