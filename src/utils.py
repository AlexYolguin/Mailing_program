import json
import logging
from dataclasses import dataclass
from typing import Dict
import smtplib
from email.mime.multipart import MIMEMultipart

@dataclass
class Clients:
    """
Содержит информацию о клиентах
    """
    clients_list: list

def load_clients(clients_config: Dict) -> Clients:
    """
Создаёт объект класса Clients
    """
    clients_list = clients_config["clients_list"]

    return Clients(
        clients_list=clients_list
    )


@dataclass
class Sender:
    """
Содержит основную информацию об аккаунте-отправителе
    """
    email_sender: str
    email_password: str

    def __repr__(self):
        return f"""
email_sender: {self.email_sender}
email_password: "{"*" * 12}"
        """

def load_sender(
    source_config: Dict,
    secret_config: Dict
) -> Sender:
    """
Создаёт объект класса Sender
    """
    
    email_sender = source_config["email_sender"]
    email_password = secret_config["email_password"]

    return Sender(
        email_sender=email_sender,
        email_password=email_password
    )


def parse_host(email: str) -> str:
    """
Определяем хост по домену почты-отправителя
    """
    return ("smtp." + email.split("@")[1])

def run(
    sender: Sender,
    clients: Clients,
    message: MIMEMultipart,
) -> None:
    """
Осуществляет рассылку сообщения "message"
Всем клиентам в списке клиентов
    """

    # Для обеспечения закрытия соединения оборачиваем процесс отправки 
    # почты в конструкцию try-except-finally
    try:
        try:
            # пробуем подключиться к стандартным портам
            smtp_server = smtplib.SMTP(parse_host(sender.email_sender), 587)
            logging.info("Connected on port 587")
        
        except Exception as e:
            logging.exception(e)

            smtp_server = smtplib.SMTP(parse_host(sender.email_sender), 465)
            logging.info("Connected on port 465")
        
        smtp_server.starttls()
        smtp_server.ehlo

        smtp_server.login(sender.email_sender, sender.email_password)

        # отправка писем каждому адресату
        for email_getter in clients.clients_list:
            smtp_server.sendmail(sender.email_sender, email_getter, message.as_string())

    except Exception as e:
        logging.exception(e)
    
    finally:
        # закрываем соединение
        smtp_server.quit()
