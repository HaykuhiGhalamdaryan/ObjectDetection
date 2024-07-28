import telebot
from telebot import types


API_TOKEN = '' #Your Token
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    f = open('C:\\Users\\User\\OneDrive\\Рабочий стол\\projects\\telebot\\nkar.jpeg', 'rb')
    bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}․ I am your assistant, how can I help you?')    

@bot.message_handler(commands=['language'])
def language(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    python = types.InlineKeyboardButton('Python', callback_data='python')
    javascript = types.InlineKeyboardButton('JavaScript', callback_data='javascript')
    c_sharp = types.InlineKeyboardButton('C#', callback_data='c_sharp')
    java = types.InlineKeyboardButton('Java', callback_data='java')
    
    markup.add(python, javascript, c_sharp, java)
    
    bot.send_message(message.chat.id, 'Choose your favorite language.', reply_markup=markup)
     
@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.message:
        if callback.data == 'python':
            bot.send_message(callback.message.chat.id, "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.")
        elif callback.data == 'javascript':
            bot.send_message(callback.message.chat.id, "JavaScript was initially created to “make web pages alive”.The programs in this language are called scripts. They can be written right in a web page’s HTML and run automatically as the page loads. Scripts are provided and executed as plain text. They don’t need special preparation or compilation to run.")
        elif callback.data == 'c_sharp':
            bot.send_message(callback.message.chat.id, "C#, pronounced 'C-sharp,' is an object-oriented programming language from Microsoft that enables developers to build applications that run on the .NET platform. C# has its roots in the C family of programming languages and shares many of the same characteristics as those found in C and C++, as well as in Java and JavaScript.")
        elif callback.data == 'java':
            bot.send_message(callback.message.chat.id, "Java is a programming language and computing platform first released by Sun Microsystems in 1995. It has evolved from humble beginnings to power a large share of today’s digital world, by providing the reliable platform upon which many services and applications are built. New, innovative products and digital services designed for the future continue to rely on Java, as well.")                             

bot.polling()