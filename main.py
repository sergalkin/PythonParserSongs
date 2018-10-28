import sys  # sys нужен для передачи argv в QApplication
import os  # методы для отображения содержимого директорий
import songNameFixer

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore

import design  # конвертированный файл дизайна
import modal


class ModalWindow(QtWidgets.QMainWindow, modal.Ui_MainWindow1):
    def __init__(self, parent):
        super(ModalWindow, self).__init__(parent)
        self.setupU(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.pushButton.clicked.connect(self.closeAndReturn)


    def closeAndReturn(self):
        self.close()
        self.parent().show()


class ParserApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
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
        countSongs = 0
        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for f in os.listdir(directory):  # для каждого файла в директории
                file_name, file_ext = os.path.splitext(f)
                if(songNameFixer.SongNameFixer().audioFormatChecker(file_ext)):
                    self.listWidget.addItem(f)   # добавить файл в listWidget
                    countSongs+=1
            if(countSongs>0):
                print(countSongs)
                song = songNameFixer.SongNameFixer(directory).stripAll()
                for f in os.listdir(directory):
                    file_name, file_ext = os.path.splitext(f)
                    if(songNameFixer.SongNameFixer().audioFormatChecker(file_ext)):  
                        self.listWidgetAfter.addItem(f)   # добавить измененный файл в listWidgetAfter
                        self.statusBar.showMessage('Парсинг завершен')
            else:
                self.hide()
                self.ModalWindow = ModalWindow(self)
                self.ModalWindow.show()
                self.statusBar.showMessage('Песни не найдены')
    


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ParserApp()  # Создаём объект класса ParserApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

