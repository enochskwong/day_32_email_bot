##################### Extra Hard Starting Project ######################
import random
import pandas
import csv
import datetime as dt
import smtplib

my_mail = 'nockudemy@gmail.com'
my_pass = '**************'
to_mail = 'enochskwong@yahoo.com'

fin_letter_to_send = "fail fail fail fail"
persons_name = "bob bob bob bob bob bob bob"


# 1. Update the birthdays.csv
bday_csv = pandas.read_csv("birthdays.csv")
bday_df = bday_csv.to_dict(orient='records')
print(bday_df)
print(bday_csv)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
this_year = now.year
this_day = now.day
this_hour = now.hour
this_min = now.min
this_sec = now.second
birthday = None


def generate_letter():
    pass

def send_bday_mail():
    gmail_connection = smtplib.SMTP("smtp.gmail.com", port=587)
    gmail_connection.starttls()
    gmail_connection.login(user=my_mail, password=my_pass)
    gmail_connection.sendmail(from_addr=my_mail, to_addrs=to_mail, msg=f"Subject: Happy Birthday {persons_name}\n\n {fin_letter_to_send}")

machine_on = True

while machine_on:


    letter_choice = random.randint(1, 3)
    now = dt.datetime.now()
    this_year = now.year
    this_day = now.day
    this_hour = now.hour
    birthday = None
    for each in bday_df:
        if each["day"] == this_day:
            if this_hour == 7:
                if this_min == 0:
                    if this_sec == 0:
                        with open(file="./letter_templates/letter_%s.txt" % letter_choice, mode="r") as letter_data:
                            data = letter_data.read()
                            fixed_data = data.replace("[NAME]", each["name"]).replace("Angela", "Enoch")
                            persons_name = each['name']
                            fin_letter_to_send = fixed_data

                            print(fixed_data)
                            print(letter_data)
                            print(now)
                            send_bday_mail()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.







