words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard   = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

words = {}
answers = {}


def choose_difficulty():
    global words
    difficulty_level = str(input("Выберите уровень: "))
    difficulty_level = difficulty_level.lower()
    if difficulty_level  == "легкий":
        words = words_easy
    elif difficulty_level  == "средний":
        words = words_medium
    elif difficulty_level  == "сложный":
        words = words_hard
    else:
        words = words_medium
    print(f"Выбран {difficulty_level} уровень. Мы предложим {len(words)} слов, подберите перевод.")


def play_game():
    for key, value in words.items():
        print(f"{key}, {len(value)} букв, начинается на  {value[0]}...")
        slovo = input()
        if slovo == value:
            print(f"Верно. {key} - это {value}.")
            answers[key] = "True"
        else:
            print(f"Неверно. {key} - это {value}.")
            answers[key] = "False"
    return answers


def display_results():
    spisok_true = ""
    spisok_false = ""
    for key, value in answers.items():
        if value == "True":
            spisok_true += f"{key}\n"
        elif value == "False":
            spisok_false += f"{key}\n"
    print("Правильно отвечены слова:")
    print(spisok_true)
    print("Неправильно отвечены слова:")
    print(spisok_false)

def calculate_rank(answers):
    level = 0
    for key, value in answers.items():
        if value == "True":
            level += 1
    print(f"Ваш ранг:\n{levels[level]} ")


choose_difficulty()
play_game()
display_results()
calculate_rank(answers)




