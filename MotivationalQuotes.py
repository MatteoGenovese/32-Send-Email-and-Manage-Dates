import datetime
import smtplib
from data import password
import random

now = datetime.datetime.now()
day_of_week = now.weekday()
myEmail = "matteo.genovese.91@gmail.com"


def sendquote(quoteToSend):
    # search your smtp information by google it
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # create transport layer security, it protect the connection at our e-mail server
        connection.starttls()
        connection.login(user=myEmail, password=password.myPassword)
        connection.sendmail(from_addr=myEmail, to_addrs="matteo.genovese@icloud.com",
                            msg=f"Subject:Quote\n\n{quoteToSend}")
        connection.close()


# On tuesday, send quote to a provided email
if day_of_week == 1:
    with open("data/quotes.txt") as quotes_file:
        quotesFile = quotes_file.readlines()
        quote = random.choice(quotesFile)
        sendquote(quote)
