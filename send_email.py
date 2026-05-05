import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ইমেইল কনফিগারেশন
sender_email = "orders@aihcompany.com"
password = "anamul-mainul"  # আপনার হোস্টিং ইমেইলের পাসওয়ার্ড
smtp_server = "161.248.188.172" # আপনার হোস্টিংয়ের SMTP সার্ভার
smtp_port = 465 # সাধারণত ৪৬৫ বা ৫৮৭ হয়

# প্রাপকের লিস্ট
receivers = ["mdmainul23122003@gmail.com", "mdanamuli699@gmail.com", "mdanamulislam01617963617@gmail.com"]

# HTML বডি (আপনার সেই এলিট প্রপোজালটি এখানে দিন)
# html_content = """
# <html>
#   <body style="font-family: Arial; text-align: center;">
#     <h2 style="color: #2BD5E3;">AIH COMPANY</h2>
#     <img src="https://yourdomain.com/path/to/image.jpg" width="300">
#     <p>Accelerate Growth with AI-Powered Systems.</p>
#     <a href="https://aihcompany.com" style="background: #2BD5E3; color: white; padding: 10px; text-decoration: none;">Contact Us</a>
#   </body>
# </html>
# """

# ১. এইচটিএমএল ফাইলটি ওপেন করে ডেটা রিড করা
try:
    with open("proposal.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    print("Error: proposal.html ফাইলটি খুঁজে পাওয়া যায়নি!")
    exit()

try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender_email, password)
    
    for receiver in receivers:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = "Elite Business Proposal 2026 - AIH Company"
        
        msg.attach(MIMEText(html_content, 'html'))
        server.sendmail(sender_email, receiver, msg.as_string())
        print(f"Sent to {receiver}")

    server.quit()
except Exception as e:
    print(f"Error: {e}")