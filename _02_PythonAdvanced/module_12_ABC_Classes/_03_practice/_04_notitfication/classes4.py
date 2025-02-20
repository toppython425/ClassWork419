from abc import ABC, abstractmethod
import random


class Notification(ABC):

    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message
        self.status = 'Pending'

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def retry(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print(f'Отправляем письмо в адрес: {self.recipient}. С сообщением: {self.message}')
        if random.choice([True, False]):
            self.status = 'Sent'
            print(f'Письмо успешно отправлено в адрес: {self.recipient}')
            return True
        else:
            self.status = 'Failed'
            print(f'Ошибка! Письмо не было отправлено в адрес: {self.recipient}')
            return False

    def get_details(self):
        return f'EmailNotification: Получатель: {self.recipient}. Сообщение: {self.message}. Статус: {self.status}'

    def retry(self):
        if self.status == 'Failed':
            print(f'Попытка повторной отправки в адрес: {self.recipient}. С сообщением: {self.message}')
            self.send()
