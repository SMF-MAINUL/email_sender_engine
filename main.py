


# import smtplib
# import time
# import random
# import csv
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # ইমেইল কনফিগারেশন
# sender_email = "orders@aihcompany.com"
# password = "anamul-mainul"
# smtp_server = "161.248.188.172"
# smtp_port = 465

# # প্রাপকের লিস্ট (আপনার লিডগুলো এখানে দিন)
# # receivers = ["mdmainul23122003@gmail.com", "mdanamuli699@gmail.com",]
# receivers = [
#   "JohnPetersen.Realtor@Gmail.com",
#   "reginhomes@gmail.com",
#   "HelloHomeAZ@gmail.com",
#   "guptapropertygroup@gmail.com",
#   "brian.s.brennan@gmail.com",
#   "jchandlerrealty@gmail.com",
#   "phoenixrealtorservice@gmail.com",
#   "katemyhan@gmail.com",
#   "EricSellsSATX@gmail.com",
#   "mikepettayhomes@gmail.com",
#   "jennypettayhomes@gmail.com",
#   "kpsellshome@yahoo.com",
#   "jadouds@aol.com",
#   "clau.bolo@gmail.com",
#   "MYLESMINNS@GMAIL.COM",
#   "bob1monaco@yahoo.com",
#   "orchardcresttutoring@gmail.com",
#   "topseller@aol.com",
#   "brucebhill566@gmail.com",
#   "chrispitts1000@gmail.com",
#   "quinlan@gmail.com",
#   "joeybates@aol.com",
#   "Randeebstolar@gmail.com",
#   "shelleyacostello@gmail.com",
#   "setupglobal@yahoo.com",
#   "jamesashcraft@gmail.com"
#   "joliremax@gmail.com",
#   "EricSellsSATX@gmail.com",
#   "cindymavrak11@gmail.com",
#   "isabelfine622@gmail.com",
#   "gavinpemberton24@gmail.com",
#   "katemyhan@gmail.com",
#   "mainstproperty@gmail.com",
#   "klink@gmail.com",
#   "relotproperties@gmail.com",
#   "jamilalshmailawi@gmail.com",
#   "tammyhenderson@gmail.com",
#   "nicolebrown@gmail.com",
#   "nicholaselg@gmail.com",
#   "garcia@gmail.com",
#   "tgavitticosta@gmail.com",
#   "jmnicksmith@gmail.com",
#   "comfortolugbami@gmail.com",
#   "prakhararora@gmail.com"
# ]




# # র্যান্ডম টাইমিং কনফিগারেশন (সেকেন্ডে)
# MIN_DELAY = 180   # সর্বনিম্ন ৬০ সেকেন্ড (3 মিনিট)
# MAX_DELAY = 300  # সর্বোচ্চ ১৮০ সেকেন্ড (5 মিনিট)

# # ১. এইচটিএমএল ফাইলটি রিড করা
# try:
#     with open("proposal.html", "r", encoding="utf-8") as f:
#         html_content = f.read()
# except FileNotFoundError:
#     print("Error: proposal.html খুঁজে পাওয়া যায়নি!")
#     exit()

# success_file = "sent_emails.csv"
# failed_file = "failed_emails.csv"

# def write_to_csv(file_name, email):
#     with open(file_name, mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow([email])

# try:
#     server = smtplib.SMTP_SSL(smtp_server, smtp_port)
#     server.login(sender_email, password)

#     for index, receiver in enumerate(receivers):
#         try:
#             msg = MIMEMultipart()
#             msg['From'] = f"AIH Company <{sender_email}>"
#             msg['To'] = receiver
#             msg['Subject'] = "Elite Business Proposal 2026 - AIH Company"
#             msg.attach(MIMEText(html_content, 'html'))

#             server.sendmail(sender_email, receiver, msg.as_string())
#             print(f"[{index+1}] Sent to {receiver}")
#             write_to_csv(success_file, receiver)

#             # শেষ ইমেইল পাঠানোর পর আর অপেক্ষার দরকার নেই
#             if index < len(receivers) - 1:
#                 wait_time = random.randint(MIN_DELAY, MAX_DELAY)
#                 print(f"Waiting for {wait_time} seconds before next email...")
#                 time.sleep(wait_time)

#         except Exception as e:
#             print(f"Failed to send to {receiver} | Error: {e}")
#             write_to_csv(failed_file, receiver)

#     server.quit()
#     print("All emails processed successfully!")

# except Exception as e:
#     print(f"Server Error: {e}")

import smtplib
import time
import random
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ইমেইল কনফিগারেশন
sender_email = "orders@aihcompany.com"
password = "anamul-mainul"
smtp_server = "161.248.188.172"
smtp_port = 465

receivers = [
  "JohnPetersen.Realtor@Gmail.com", "reginhomes@gmail.com", "HelloHomeAZ@gmail.com",
  "guptapropertygroup@gmail.com", "brian.s.brennan@gmail.com", "jchandlerrealty@gmail.com",
  "phoenixrealtorservice@gmail.com", "katemyhan@gmail.com", "EricSellsSATX@gmail.com",
  "mikepettayhomes@gmail.com", "jennypettayhomes@gmail.com", "kpsellshome@yahoo.com",
  "jadouds@aol.com", "clau.bolo@gmail.com", "MYLESMINNS@GMAIL.COM", "bob1monaco@yahoo.com",
  "orchardcresttutoring@gmail.com", "topseller@aol.com", "brucebhill566@gmail.com",
  "chrispitts1000@gmail.com", "quinlan@gmail.com", "joeybates@aol.com", "Randeebstolar@gmail.com",
  "shelleyacostello@gmail.com", "setupglobal@yahoo.com", "jamesashcraft@gmail.com",
  "joliremax@gmail.com", "cindymavrak11@gmail.com", "isabelfine622@gmail.com",
  "gavinpemberton24@gmail.com", "mainstproperty@gmail.com", "klink@gmail.com",
  "relotproperties@gmail.com", "jamilalshmailawi@gmail.com", "tammyhenderson@gmail.com",
  "nicolebrown@gmail.com", "nicholaselg@gmail.com", "garcia@gmail.com", "tgavitticosta@gmail.com",
  "jmnicksmith@gmail.com", "comfortolugbami@gmail.com", "prakhararora@gmail.com"
]

MIN_DELAY = 180  # ৩ মিনিট
MAX_DELAY = 300  # ৫ মিনিট

try:
    with open("proposal.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    print("Error: proposal.html খুঁজে পাওয়া যায়নি!")
    exit()

def write_to_csv(file_name, email):
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([email])

# লুপের ভেতরে কানেকশন ম্যানেজমেন্ট (সবচেয়ে নিরাপদ)
for index, receiver in enumerate(receivers):
    try:
        # প্রতিবার নতুন করে সার্ভারে লগইন করা যাতে টাইম-আউট না হয়
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, password)

        msg = MIMEMultipart()
        msg['From'] = f"Anamul - AIH Company <{sender_email}>"
        msg['To'] = receiver
        msg['Subject'] = "Elite Business Proposal 2026 - AIH Company"
        msg.attach(MIMEText(html_content, 'html'))

        server.sendmail(sender_email, receiver, msg.as_string())
        print(f"[{index+1}] Sent to {receiver}")
        write_to_csv("sent_emails.csv", receiver)
        
        server.quit() # পাঠানো শেষে কানেকশন বন্ধ

        if index < len(receivers) - 1:
            wait_time = random.randint(MIN_DELAY, MAX_DELAY)
            print(f"Waiting for {wait_time} seconds before next email...")
            time.sleep(wait_time)

    except Exception as e:
        print(f"Failed to send to {receiver} | Error: {e}")
        write_to_csv("failed_emails.csv", receiver)

print("Process Complete!")