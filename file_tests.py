from file_classes import JsonFile, CsvFile, TxtFile

def main():
    # Создание объектов для работы с файлами
    json_file = JsonFile("data.json")
    csv_file = CsvFile("data.csv")
    txt_file = TxtFile("data.txt")

    print(json_file.file_path)

    # Тест на чтение данных из несуществующего файла

    # json_file.read()
    # csv_file.read()
    # txt_file.read()

    result = json_file.read()
    print(result)
    result = csv_file.read()
    print(result)
    result = txt_file.read()
    print(result)

    test_string = "Hello, world!"
    test_list_of_lists = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    test_list_of_dicts = [{"name": "John", "age": 30, "city": "New York"}, {"name": "Jane", "age": 25, "city": "Los Angeles"}]
    test_dict = {"name": "John", "age": 30, "city": "New York"}
    test_dict_2 = {"gender": "male", "hobby": "programming"}

    # Тест на запись данных в файл
    json_file.write(test_dict)
    csv_file.write(test_list_of_lists)
    txt_file.write(test_string)

    # Тест на чтение данных из файла после записи
    result = json_file.read()
    print(result)
    result = csv_file.read()
    print(result)
    result = txt_file.read()
    print(result)
    # Тест на добавление данных в файл
    json_file.append(test_dict_2)
    csv_file.append(test_list_of_lists)
    txt_file.append(test_string)

    result = json_file.read()
    print(result)
    result = csv_file.read()
    print(result)
    result = txt_file.read()
    print(result)



if __name__ == "__main__":
    main()