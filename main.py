import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('API_KEY')
if token is None:
    raise ValueError('в файле .env отсутствует API_KEY')
bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Это бот SeoMatrix!'
                                      '\nЧтобы узнать, что он может, напиши /help')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Тут есть команды:'
                                      '\n1. /start запуск самого бота'
                                      '\n2. /help узнать возможности бота'
                                      '\n3. /start_test запустить анкету')


def base_questions(m: types.Message):
    global question
    message = m.text
    if message == '/end':
        bot.send_message(m.chat.id, 'Прохождение остановлено',
                         reply_markup=types.ReplyKeyboardRemove())
        return
    user_id = m.from_user.id
    try:
        for season, scores in survey[question]["answers"][message].items():
            total_score[season] += scores
        user_data[user_id] = dict(user_score=total_score)
        question += 1
        if question >= len(survey):
            question = 0
            bot.send_message(m.chat.id, 'Итоги анкеты:', reply_markup=types.ReplyKeyboardRemove())
            max_score = 0
            your_season = ''
            for season, scores in total_score.items():
                bot.send_message(m.chat.id, f"{season} - {scores}")
                if scores > max_score:
                    max_score = scores
                    your_season = season
            print(user_data)
            for count in total_score:
                total_score[count] = 0
            bot.send_message(m.chat.id, f"Наибольшее количество баллов у времени года: {your_season}")
            return
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for key in survey[question]['answers'].keys():
            markup.add(key)
        bot.send_message(m.chat.id, survey[question]["question"], reply_markup=markup)
        bot.register_next_step_handler(m, base_questions)
    except:
        bot.reply_to(m, 'Что-то сломалось... Попробуйте ещё раз')
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for key in survey[question]['answers'].keys():
            markup.add(key)
        bot.send_message(m.chat.id, survey[question]["question"], reply_markup=markup)
        bot.register_next_step_handler(m, base_questions)


@bot.message_handler(commands=['start_game'])
def profile_output(m: types.Message):
    bot.send_message(m.from_user.id, 'Запускаем игру')
    user_id = m.from_user.id
    user_name = m.from_user.first_name

    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for key in survey[question]['answers'].keys():
        markup.add(key)
    bot.send_message(m.chat.id, survey[question]["question"], reply_markup=markup)
    bot.register_next_step_handler(m, base_questions)


bot.polling()
