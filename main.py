import telebot
import time

TOKEN = '5643623218:AAGrukz0gozB3fIKR73Al7ZLOVCQ20rEJLk'
bot = telebot.TeleBot(TOKEN)
users = {}

# описание месседж-хендлеров

@bot.message_handler(commands=['start'])
def start(message):
    users[message.from_user.id] = {'True'}
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG0BRjmIklyZ-gyX-yI4v_fje1vfmxEgAC1xgAAm4m4UsFYy3CmOv8qywE')
    bot.send_message(message.chat.id, 'Hello, my name is <b>Hazbulla</b>! I\'m from Russia🇷🇺!', parse_mode='html')
    bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}</b>, if you want to know what I can do write word <b>\'Skills\'</b>.', parse_mode ='html')


@bot.message_handler(commands=['help'])
def help(message):
    markup = telebot.types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, 'If you want to give my owner money you should write him in VK:')
    markup.add(telebot.types.InlineKeyboardButton('My owner', url = 'https://vk.com/tussan_pussan'))
    bot.send_message(message.chat.id, 'My owner', reply_markup=markup)


@bot.message_handler(commands=['bot'])
def help(message):
    menu = telebot.types.ReplyKeyboardMarkup()
    bio = telebot.types.KeyboardButton('Biography')
    inst = telebot.types.KeyboardButton('YouTube')
    menu.add(bio, inst)
    bot.send_message(message.chat.id, 'Information about Hazbulla🤙🏽', reply_markup=menu)

@bot.message_handler(content_types=['text'])
def text(message):
    if not users:
        users[message.from_user.id] = True
    if message.text == 'Skills' and users[message.from_user.id]:
        bot.send_message(message.chat.id, 'Choose from following list only one skill (number):')
        bot.send_message(message.chat.id,"""  1️⃣I know how to repeat after you.️🧠
2️⃣You can see my favourite food🍓
3️⃣My enemy🔫
4️⃣Book about UFC rules
5️⃣Advice""")
    elif message.text == '1' and users[message.from_user.id]:
        bot.send_message(message.chat.id, 'Bro, remember: I\'m very strong and you\'re not my rival, because of its if you\'re tired, print word <b>\'Stop\'</b>.', parse_mode ='html')
        users[message.from_user.id] = False
    elif message.text == '2' and users[message.from_user.id]:
        file = open('хасбулла и клубника.jpeg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'I love strawberries😍')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG0DVjmJa9no44Z531nQujXkCWxxhCxQACSRIAAtU86UsZ3n-O8Yj8qCwE')
    elif message.text == '3' and users[message.from_user.id]:
        bot.send_message(message.chat.id,'Abdurozik, you\'re loser, I\'m the best!')
        file = open("хасбулла и абдурозик.jpeg", "rb")
        bot.send_photo(message.chat.id, file)
    elif message.text == '4' and users[message.from_user.id]:
        bot.send_message(message.chat.id,'Bro, please wait a few second. Book is too large!')
        file = open('UFC Rules.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id, 'Bro, be careful on the street:)')
    elif message.text == '5' and users[message.from_user.id]:
        bot.send_message(message.chat.id, 'Strawberry is a bomb, to be honest🍓')
    elif message.text == 'Stop' and not users[message.from_user.id]:
        users[message.from_user.id] = True
    elif not users[message.from_user.id]:
        bot.send_message(message.chat.id, f'{message.text}👅')
    elif message.text == 'YouTube' and users[message.from_user.id]:
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('YouTube', url = 'https://www.youtube.com/watch?v=-aETFLuzMhU&t=34s')
        markup.add(button)
        bot.send_message(message.chat.id, 'Hazbulla\'s YouTube', reply_markup=markup)
    elif message.text == 'Biography' and users[message.from_user.id]:
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Biography', url='https://wikibio.in/hasbulla/')
        markup.add(button)
        bot.send_message(message.chat.id, 'Hazbulla\'s Biography', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'What did you write? Come to your senses🧠')


bot.polling(none_stop = True)