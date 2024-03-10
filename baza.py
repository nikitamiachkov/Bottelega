import telebot as tb
import webbrowser

bot = tb.TeleBot("6893260117:AAFvAB_kO3ZZHs8NLx-yFyuT5CxtiCY1Cv4") #подключаем бота

@bot.message_handler(commands = ["start", "skazi_hi"]) #подключаем декоратор, соединяем старт
def start(message): #message хранит всю переписку
    bot.send_message(message.chat.id, f"Привет качок {message.from_user.first_name}!") #отправляем сообщение

@bot.message_handler(commands = ["help"]) 
def start(message): 
    bot.send_message(message.chat.id, "<u>Всё</u> <b>нормуль</b>", parse_mode="html") #добавляем редактирование с помощью штмл

@bot.message_handler(commands = ["info"]) 
def start(message): 
    bot.send_message(message.chat.id, message) #вся информация о чате в виде объекта

@bot.message_handler(commands = ["site"]) 
def site(message): 
    webbrowser.open("https://vk.com/im")
    bot.send_message(message.chat.id, "Сайт открыт!")

@bot.message_handler() #обрабатывает любой текст. Писать всегда внизу, так как верхние команды не отправляются
def text(message):
    if message.text.lower() == "как дела":
        bot.reply_to(message, f"Отлично {message.from_user.last_name}")
    elif message.text.lower() == "погода":
         bot.send_message(message.chat.id, f"Снег {message.from_user.last_name}")

#setcommands в Фазер бот нужен для создания функций в менюшке

bot.polling(none_stop = True) #Бот работает, только если программа запущена. Эта команда делаем программу бесконечной
# bot.infinity_polling() #то же самое 


