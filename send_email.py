import smtplib, ssl
import os


def send_mai(message):
    host = "smtp.gmail.com"
    port = 465

    username = "csoni1243@gmail.com"
    password = "ggzq sokb jzjq jhsj"

    reciecer = "sonichimman@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciecer, message)