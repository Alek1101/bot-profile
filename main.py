import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup
import os
from dotenv import load_dotenv
from functions import save_progress, load_progress
from game import survey

load_dotenv()
token = os.getenv('API_KEY')
if token is None:
    raise ValueError('в файле .env отсутствует API_KEY')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Это бот SeoMatrix!'
                                      '\nЧтобы узнать, что он может, напиши /help')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Тут есть команды:'
                                      '\n1. /start - запуск бота'
                                      '\n2. /help - узнать возможности бота'
                                      '\n3. /start_game - запустить анкету'
                                      '\n4. /end - остановить игру')


question = -1


def base_questions(m: types.Message):
    global question
    user_id = m.from_user.id
    message = m.text
    if survey[question]['choice'] == -1:
        bot.send_message(m.chat.id, 'Игра окончена.'
                                    '\nСпасибо за прохождение!', reply_markup=types.ReplyKeyboardRemove())
        save_progress(user_id, -1)
        return
    if message == '/end':
        print('end')
        bot.send_message(m.chat.id, 'Прохождение прекращено',
                         reply_markup=types.ReplyKeyboardRemove())
        question = -1
        save_progress(user_id, -1)
        return
    if question == 0 and message == 'Активация':
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for key in survey[question]['choice'].keys():
            markup.add(key)
        bot.send_message(m.chat.id, survey[question]["text"], reply_markup=markup)
        bot.register_next_step_handler(m, base_questions)
    else:
        try:

            question = survey[question]['choice'][message]

            if survey[question]['choice'] == -1:
                print('-1, end')
                bot.send_message(m.chat.id, survey[question]['text'])
                return
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            for key in survey[question]['choice'].keys():
                markup.add(key)
            bot.send_message(m.chat.id, survey[question]["text"], reply_markup=markup)
            bot.register_next_step_handler(m, base_questions)
        except:
            print('exc')
            bot.send_message(m.chat.id, 'Вводите ответ с клавиатуры')
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            for key in survey[question]['choice'].keys():
                markup.add(key)
            bot.send_message(m.chat.id, survey[question]["text"], reply_markup=markup)
            bot.register_next_step_handler(m, base_questions)


@bot.message_handler(commands=['start_game'])
def profile_output(m: types.Message):
    global question
    bot.send_message(m.from_user.id, 'Запускаем игру')
    user_id = m.from_user.id
    question = load_progress(user_id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if question != -1 and question is not None:
        for key in survey[question]['answers'].keys():
            markup.add(key)
        bot.send_message(m.chat.id, survey[question]["text"], reply_markup=markup)
    if question == -1 and question is not None:
        bot.send_message(m.chat.id, survey[question]['text'])
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add('Активация')
        bot.send_message(m.chat.id, survey[-1]['text'], reply_markup=markup)
        question = 0
    bot.register_next_step_handler(m, base_questions)


bot.infinity_polling()
