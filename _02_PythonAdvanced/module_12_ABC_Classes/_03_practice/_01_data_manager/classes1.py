from abc import ABC, abstractmethod


class DataManager(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass


class FileDataManager(DataManager):

    def save(self, data):
        with open(r'files\data.txt', 'w', encoding='utf-8') as file:
            file.write(data)

    def load(self):
        with open(r'files\data.txt', 'r', encoding='utf-8') as file:
            return file.read()


class DatabaseDataManager(DataManager):
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data

    def load(self):
        return self.data
