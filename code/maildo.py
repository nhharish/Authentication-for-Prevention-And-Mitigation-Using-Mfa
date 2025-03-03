import smtplib
class Mail:
    # before you run the main.py you need to change the below mentioned mail id and password
    my_email = "_____________--->Admin_mail_Id"
    password = "_____________--->Admin_App_Passkey"
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
