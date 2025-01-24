from abc import ABC, abstractmethod
import json, csv

class AbstractFile(ABC):
    """
    Родительский класс для работы с файлами.
    """

    def __init__(self, file_path: str)->None:
        """
        Конструктор родительского класса.
        """
        self.file_path = file_path

        
    @abstractmethod
    def read(self):
        """
        Абстрактный метод для чтения данных из файла.
        """
        pass

    @abstractmethod
    def write(self, data):
        """
        Абстрактный метод для записи данных в файл.
        """
        pass

    @abstractmethod
    def append(self, data):
        """
        Абстрактный метод для добавления данных в файл.
        """
        pass


class JsonFile(AbstractFile):
    """
    Метод-наследник для работы с файлами формата JSON.
    """

    def __init__(self, file_path: str)->None:
        """
        Конструктор класса JsonFile.
        :param file_path: Путь к файлу.
        """
        super().__init__(file_path)

    def read(self)->dict:
        """
        Метод для чтения данных из файла формата JSON.
        :return: Словарь с данными из файла.
        """
        try:
            with open(self.file_path, 'r',encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        
    def write(self, data)->None:
        """
        Метод для записи данных в файл формата JSON.
        :param data: Данные для записи в файл.
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def append(self, data)->None:
        """
        Метод для добавления данных в файл формата JSON.
        :param data: Данные для добавления в файл.
        """
        # Создаём пустой словарь или список на случай если файл пустой или не существует
        json_data = {} if isinstance(data, dict) else []
        
        # пытаемся загрузить данные из файла
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                
            # проверяем что данные в файле и данные для записи одного типа
            if isinstance(json_data, dict) and not isinstance(data, dict):
                raise TypeError("Можно добавлять только словарь к существующему словарю")
            if isinstance(json_data, list) and not isinstance(data, list):
                raise TypeError("Можно добавлять только список к существующему списку")
                
        except FileNotFoundError:
            pass
            
        if isinstance(data, dict):
            json_data.update(data)
        elif isinstance(data, list):
            json_data.extend(data)
        
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

class CsvFile(AbstractFile):
    """
    Метод-наследник для работы с файлами формата CSV.
    """
    def __init__(self, file_path: str)->None:
        """
        Конструктор класса CsvFile.
        :param file_path: Путь к файлу.
        """
        super().__init__(file_path)
    
    def read(self)->list:
        """
        Метод для чтения данных из файла формата CSV.
        :return: Список с данными из файла.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def write(self, data: list)->None:
        """
        Метод для записи данных в файл формата CSV.
        :param data: Данные для записи в файл.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            if isinstance(data[0], dict):
                # Если данные - список словарей
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames,lineterminator='\n',delimiter=';')
                writer.writeheader()
                writer.writerows(data)
            elif isinstance(data[0], list):
                # Если данные - список списков
                writer = csv.writer(file, delimiter=';', lineterminator='\n')
                writer.writerows(data)

    def append(self, data: list)->None:
        """
        Метод для добавления данных в файл формата CSV.
        :param data: Данные для добавления в файл.
        """
        with open(self.file_path, 'a', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\n')
            writer.writerows(data)


class TxtFile(AbstractFile):
    """
    Метод-наследник для работы с файлами формата TXT.
    """
    def __init__(self, file_path: str)->None:
        """
        Конструктор класса TxtFile.
        :param file_path: Путь к файлу.
        """
        super().__init__(file_path)
    
    def read(self)->str:
        """
        Метод для чтения данных из файла формата TXT.
        :return: Строка с данными из файла.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""
        
    def write(self, data)->None:
        """
        Метод для записи данных в файл формата TXT.
        :param data: Данные для записи в файл.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    def append(self, data)->None:
        """
        Метод для добавления данных в файл формата TXT.
        :param data: Данные для добавления в файл.
        """
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(data)

