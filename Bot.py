import config
import telebot
import os
from flask import Flask
from threading import Thread
from random import choice
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)

total = 1
good = ["😎", "🥳", "🤩", "😍", "☺️", "😘", "😉"]
bad = ["😳", "😡", "🤬", "😰", "💩", "☠️", "😵"]

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Поздороваться👋")

    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет👋", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Поздороваться👋")
def play(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Играть🎮"))
    bot.send_message(message.chat.id, 'Что бы начать, нажми "Играть🎮"', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Играть🎮", "Начать заново🎮"])
def question1(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("GNU Linux🐧")
    btn2 = types.KeyboardButton("Windows💩")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Что лучше🤔?\n\nGNU Linux🐧  или  Windows💩", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["GNU Linux🐧", "Windows💩"])
def question2(message):
    global total
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton("Программировать и зарабатывать бабки!😎🤑")
    btn2 = types.KeyboardButton("Учить математику🤢🤮")
    markup.add(btn1, btn2)

    if message.text == "GNU Linux🐧":
        total += 1
        bot.send_message(message.chat.id, choice(good))
        bot.send_message(message.chat.id, "Продолжи фразу😈:\n\nУ меня нет времени на эту фигню, мне надо...", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, choice(bad))
        bot.send_message(message.chat.id, "Продолжи фразу😈:\n\nУ меня нет времени на эту фигню, мне надо...", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Программировать и зарабатывать бабки!😎🤑", "Учить математику🤢🤮"])
def question3(message):
    global total
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("5$")
    btn2 = types.KeyboardButton("67$ 🌝")
    btn3 = types.KeyboardButton("69$ 🌚")
    markup.row(btn1)
    markup.add(btn2, btn3)

    if message.text == "Программировать и зарабатывать бабки!😎🤑":
        total += 1
        bot.send_message(message.chat.id, choice(good))
        bot.send_message(message.chat.id, "Угадай цену🤠:\n\nСколько стоит батончик мисс?🍫🍫", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, choice(bad))
        bot.send_message(message.chat.id, "Угадай цену🤠:\n\nСколько стоит батончик мисс?🍫🍫", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["5$", "67$ 🌝", "69$ 🌚"])
def question4(message):
    global total
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Семён🙈🙉🙊")
    btn2 = types.KeyboardButton("Антон Чигур")
    btn3 = types.KeyboardButton("Ни кого")
    btn4 = types.KeyboardButton("Не убивал!")
    markup.row(btn1)
    markup.row(btn2, btn3, btn4)

    if message.text == "5$":
        total += 1
        bot.send_message(message.chat.id, choice(good))
        bot.send_message(message.chat.id, "Внимание ВОПРОС!\n\nКто украл голду у Толика😮😲", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, choice(bad))
        bot.send_message(message.chat.id, "Внимание ВОПРОС!\n\nКто украл голду у Толика😮😲", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Семён🙈🙉🙊", "Антон Чигур", "Ни кого", "Не убивал!"])
def question5(message):
    global total
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("ДА!")
    btn2 = types.KeyboardButton("Конечно!")
    btn3 = types.KeyboardButton("100%")
    btn4 = types.KeyboardButton("Безусловно!")
    btn5 = types.KeyboardButton("Так точно!")
    btn6 = types.KeyboardButton("Верно!")
    markup.row(btn4)
    markup.row(btn2, btn5)
    markup.row(btn6, btn1, btn3)

    if message.text == "Семён🙈🙉🙊":
        total += 1
        bot.reply_to(message, "🦍")
        bot.send_message(message.chat.id, "И финальный вопрос:\n\nЭто лучший бот на свете🫣🥺🥺?", reply_markup=markup)
    else:
        bot.reply_to(message, "Что😐?")
        bot.send_message(message.chat.id, "И финальный вопрос:\n\nЭто лучший бот на свете🫣🥺🥺?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["ДА!", "Конечно!", "100%", "Безусловно!", "Так точно!", "Верно!"])
def finish(message):
    global total
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Начать заново🎮"))
    if total == 5:
        bot.send_message(message.chat.id, choice(good))
        bot.send_message(message.chat.id, "Ура, у тебя 5/5 правильных ответов🥳🥳!\n\nТы можешь подойти ко мне(ну типа я Ваня😎), и я скажу, что ты молодец🤤🤤.")
        bot.send_message(message.chat.id, 'Если хочешь, можешь пройти ещё раз!\n\nПо кнопке "Начать заново🎮"', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, choice(bad))
        bot.send_message(message.chat.id, f"Ты ответил на {total}/5 вопросов, это не самый лучший результат😏😏")
        bot.send_message(message.chat.id, 'Если хочешь, можешь попробовать ещё раз!\n\nПо кнопке "Начать заново🎮"', reply_markup=markup)
    total = 1


@bot.message_handler(func=lambda message: True)
def delete(message):
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Удалить фото", callback_data="delete")
    markup.add(btn1)
    bot.reply_to(message, "Какое красивое фото!", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)


app = Flask("")

@app.route("/")
@app.route("/health")
def health_check():
    return "bot is on"

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web_server).start()


bot.polling(none_stop=True)
