class FileReader:
    """Класс чтения из файла"""

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Прочитать файл и вернуть его содержимое"""

        try:
            with open(self.filename, 'r') as f:
                text = f.read()
                return text
        except FileNotFoundError:
            print('Файл не найден')
            return ''
