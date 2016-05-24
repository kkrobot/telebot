import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


import sqlite3
import telegram
from telegram.ext import Updater
updater = Updater(token='197782591:AAEq_qIHwk4m2pLoyUW3FwI0n4_cRQxq5bI')
dispatcher = updater.dispatcher

from random import randrange,randint
import os


bot = telegram.Bot(token='197782591:AAEq_qIHwk4m2pLoyUW3FwI0n4_cRQxq5bI')

update = bot.getUpdates()
#if updates.message.text[-1] == '/ajooj':
 #   bot.sendMessage(chat_id=-34431666,text="Aya Ajooj Mikhahid Bekeshid?")





conn = sqlite3.connect('bot.db',check_same_thread=False)
# conn.execute('''CREATE TABLE ADVICE
#        (ID INT PRIMARY KEY     NOT NULL,
#        MESSAGE        TEXT    NOT NULL);''')
#
# conn.execute('''CREATE TABLE KIRKOLOFTI
#        (ID INT PRIMARY KEY     NOT NULL,
#        MESSAGE        TEXT    NOT NULL);''')
#

#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (1, 'لطفا پس از استفاده از کاندوم ، آن را در سطل آشغال بیندازید')");
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (2, ' قبل از سکس حتما کیر خود را بشویید')");
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (3, ' پس از مصرف تریاک ، وافور خود را تمیز کنید')");
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (4, ' لطفا پس از ریدن ، کان خود را به دقت آب بکشید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (5, ' پس از مصرف حشیش ، از رانندگی خودداری نمایید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (6, ' از سکس مقعدی مداوم خودداری نمایید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (7, ' لطفا با مردان غریبه همبستر نشوید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (8, ' در هنگام لیسیدن کس ، از بهداشتی بودن آن اطمینان حاصل کنید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (9, 'لطفا در جمع نگوزید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (10, ' برای کسب موفقیت در عرصه های علمی ، از مصرف وید ، عجوج، کوکایین و ال اس دی و برای موفقیت در عرصه سیاست داخلی ایران از مصرف تریاک غافل نشوید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (11, ' پشم کون خود را اصلاح نمایید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (12, ' در وعده های استعمال مواد مخدر خود فاصله ایجاد نمایید')");
#
#
#
#
# conn.execute("INSERT INTO ADVICE (ID,MESSAGE) \
#       VALUES (13, ' پس از خوردن مشروب تریاک نکشید')");
#
#
#
# conn.commit()






def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Man Amade Am Ta Kirkolofti Konam")

dispatcher.addTelegramCommandHandler('start', start)
updater.start_polling()

def ajooj(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Ajooj Mikhahid?")


global dic_kirkolofti
global dic_advice
dic_advice = {


        0 : """ لطفا پس از استفاده از کاندوم ، آن را در سطل آشغال بندازید""",
        1 : """ قبل از سکس حتما کیر خود را بشویید""",
        2 : """ پس از مصرف تریاک ، وافور خود را تمیز کنید""",
        3 : """ لطفا پس از ریدن ، کان خود را به دقت آب بکشید""",
        4 : """ پس از مصرف حشیش ، از رانندگی خودداری نمایید""",
        5 : """ از سکس مقعدی مداوم خودداری نمایید""",
        6 : """ لطفا با مردان غریبه همبستر نشوید""",
        7 : """ در هنگام لیسیدن کس ، از بهداشتی بودن آن اطمینان حاصل کنید""",
        8 : """ لطفا در جمع نگوزید""",
        9 : """ برای کسب موفقیت در عرصه های علمی ، از مصرف وید ، عجوج، کوکایین و ال اس دی و برای موفقیت در عرصه سیاست داخلی ایران از مصرف تریاک غافل نشوید """,
        10: """ پشم کون خود را اصلاح نمایید""",
        11: """ در وعده های استعمال مواد مخدر خود فاصله ایجاد نمایید""",
        12: """ پس از خوردن مشروب تریاک نکشید""",

    }
dic_kirkolofti =  {
        0 : """ کیرکلفتی باید کرد
        چربلندی باید نمود
        """,

        1 : """ جق ورزیم
                کس بورزیم
        جق ورزیم
        کس بورزیم
        """,
        2 : """ ما مردمان حشیش پرستیم
        ما مردمان حشیش پرستیم
        """ ,

        3 : """ بوی کان خوب است """,
        4 : """ من کس را دوست دارم """

    }

print(dic_advice)



def kirkolofti(bot,update):
    dic = dic_kirkolofti

    bot.sendMessage(chat_id=update.message.chat_id, text=dic[randrange(len(dic))])



dispatcher.addTelegramCommandHandler('kirkolofti', kirkolofti)



dispatcher.addTelegramCommandHandler('ajooj', ajooj)



def calc(bot,update,args):
    txt = ''.join(args)
    result = eval(txt)
    bot.sendMessage(chat_id=update.message.chat_id, text=result)



dispatcher.addTelegramCommandHandler('calc', calc)



def no_leave(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="@Parham_Dormiani لیو نده کسکش")



dispatcher.addTelegramCommandHandler('leave', no_leave)



def WordsOfWisdom(bot,update):
    dic= {

        0: """ کسی که کیرکلفت نباشد کیرکلفت نیست
        امام خمینی"""


    }

    bot.sendMessage(chat_id=update.message.chat_id, text=dic[randrange(len(dic))])


dispatcher.addTelegramCommandHandler('WordsOfWisdom', WordsOfWisdom)



def porn(bot,update):
    os.chdir('C:\\Users\\Faraz\\Desktop\\Robot\\pics')
    random_num = randint(16,157)
    fh = open(str(random_num)+'.jpg','rb')
    bot.sendPhoto(chat_id=update.message.chat_id , photo=fh)


dispatcher.addTelegramCommandHandler('porn', porn)



def teach(bot,update,args):

    text = ' '.join(args)
    cursor = conn.execute("SELECT ID  from ADVICE")
    a = list(cursor)
    max_num = a[-1][0]
    print(max_num)
    values = (max_num+1,text)
    conn.execute("INSERT INTO ADVICE VALUES (?,?)",values);
    conn.commit()
    bot.sendMessage(chat_id=update.message.chat_id , text = text)

dispatcher.addTelegramCommandHandler('teach', teach)





def advice(bot,update):
     cursor = conn.execute("SELECT ID  from ADVICE")
     a = list(cursor)
     max = a[-1][0]
     random_num = randint(1,max)
     cursor2 = conn.execute("SELECT MESSAGE  from ADVICE WHERE ID={}".format(random_num))
     for i in cursor2:
         message = i[0]
     bot.sendMessage(chat_id=update.message.chat_id, text=message )

dispatcher.addTelegramCommandHandler('advice', advice)




def policy(bot,update):
    text = """ برادران خواهشمندم دروغ نگویید
    لواط نکنید
    بچه بازی نفرمایید
    با تشکر
    """
    bot.sendMessage(chat_id=update.message.chat_id, text=text)



dispatcher.addTelegramCommandHandler('policy', policy)





def echo(bot, update):
    print(update.message.text)
    if update.message.text == '/ajooj':
        bot.sendMessage(chat_id=update.message.chat_id, text="Ajooj Mikhahid?")

dispatcher.addTelegramMessageHandler(echo)