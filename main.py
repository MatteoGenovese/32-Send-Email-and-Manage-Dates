##################### Hard Starting Project ######################
# 1. Update the birthdays.csv with your friends & family's details.

import datetime
import smtplib
from data import password
import random
import json
import pandas

now = datetime.datetime.now()
day_of_week = now.weekday()
myEmail = "matteo.genovese.91@gmail.com"
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt", ]


def sendhappybirthday(quoteToSend):
    # search your smtp information by google it
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # create transport layer security, it protect the connection at our e-mail server
        connection.starttls()
        connection.login(user=myEmail, password=password.myPassword)
        connection.sendmail(from_addr=myEmail, to_addrs="matteo.genovese@icloud.com",
                            msg=f"Subject:Happy Birthday!!!\n\n{''.join(quoteToSend)}")
        connection.close()


with open("data/birthday.csv") as date_file:
    dateFile = pandas.read_csv(date_file)
    date_dict = dateFile.to_dict(orient="records")
    print(date_dict)
    for person in date_dict:
        # 2. Check if today matches a birthday in the birthdays.csv
        if now.month == person["month"] and now.day == person["day"]:
            letter = random.choice(letters)
            # 3. If step 2 is true, pick a random letter from
            # letter templates and replace the [NAME] with the
            # person's actual name from birthdays.csv
            # HINT: https://www.w3schools.com/python/ref_string_replace.asp
            with open(f"letters/{letter}") as lettertxt:
                bodyLines = lettertxt.readlines()
                body = []
                for row in bodyLines:
                    if "[NAME]" in row:
                        row = row.replace("[NAME]", person["name"])
                    body.append(row)
            # 4. Send the letter generated in step 3 to that
            # person's email address.
            # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com),
            # Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
            sendhappybirthday(body)
