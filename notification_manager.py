import os
import smtplib



class SendingEmail:

    def sending_email(self,title,price,url):
        my_email = os.environ['MY_EMAIL']
        password = os.environ['PASSWORD']

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs='t.muzeffer.1998@gmail.com',msg=f"Subject:Amazon Price Alert\n\n{title} is now ${price}\n{url}".encode("utf-8"))




