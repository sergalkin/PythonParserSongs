import sys  # sys нужен для передачи argv в QApplication
import os  # методы для отображения содержимого директорий
import songNameFixer

from PyQt5 import QtWidgets

import design  # конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # инициализация дизайна
        self.btnBrowse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder

    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        self.listWidgetAfter.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)   # добавить файл в listWidget
            song = songNameFixer.songNameFixer(directory).stripAll()
            for file_name in os.listdir(directory):  
                self.listWidgetAfter.addItem(file_name)   # добавить измененный файл в listWidgetAfter

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()