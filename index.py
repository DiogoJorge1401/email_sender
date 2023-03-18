import ssl
import smtplib
from configparser import ConfigParser
from email.message import EmailMessage


class EmailConfig:
    def __init__(self, file_path: str):
        self.config = self.read_config(file_path)

    def read_config(self, file_path: str):
        config = ConfigParser()
        config.read(file_path)
        return config

    def get_email_password(self):
        return self.config.get("email", "email_password")

    def get_email_sender(self):
        return self.config.get("email", "email_sender")


class EmailSender:
    def __init__(self, app_password: str, sender: str):
        self.app_password = app_password
        self.sender = sender

    def send_email(self, receiver: str, subject: str, body: str):
        email_msg = self.create_email_message(receiver, subject, body)
        self.send_email_message(email_msg, receiver)

    def create_email_message(self, receiver: str, subject: str, body: str):
        email_msg = EmailMessage()
        email_msg["From"] = self.sender
        email_msg["To"] = receiver
        email_msg["subject"] = subject
        email_msg.set_content(body)
        return email_msg

    def send_email_message(self, email_msg, receiver):
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(self.sender, self.app_password)
                smtp.sendmail(self.sender, receiver, email_msg.as_string())
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar o e-mail {e}")


def main():
    email_config = EmailConfig("./config.ini")
    app_password = email_config.get_email_password()
    email_sender = email_config.get_email_sender()
    email_receiver = ""
    subject = ""
    body = ""

    while True or condition:
        email_receiver = input("Enviar email para: ") or "rojex15834@huvacliq.com"
        subject = input("Assunto: ") or "Teste?"
        body = (
            input("Mensagem: ")
            or """
            Teste
        """
        )
        if (input("Tudo ok? (s/N)").lower() or "n") == "s":
            break
        else:
            print()

    email_sender_obj = EmailSender(app_password, email_sender)
    email_sender_obj.send_email(email_receiver, subject, body)


if __name__ == "__main__":
    main()
