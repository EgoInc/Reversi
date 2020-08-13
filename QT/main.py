import sys
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна

CALCULATOR = [64, 0, 0]
PLAYER = False


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методами т.д. в файле design.py
        super().__init__()

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.startButton.clicked.connect(self.start)
        self.free.display(int(CALCULATOR[0]))



    def main():
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        window = ExampleApp()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        app.exec_()  # и запускаем приложение

    def set_calc(self):
        self.free.display(int(CALCULATOR[0]))
        self.white.display(int(CALCULATOR[2]))
        self.black.display(int(CALCULATOR[1]))

    def button_clicked(self):
        clickedbutton = self.sender()
        print(str(clickedbutton.objectName()))

    def recolor_turn(self):
        clickedbutton = self.sender()
        self.turn_belong.setStyleSheet('background-color: {}'.format('black' if PLAYER == True else 'yellow'))

    def start_turn(self):
        global CALCULATOR, PLAYER
        clickedbutton = self.sender()
        print(str(clickedbutton.objectName()))
        color = clickedbutton.palette().button().color()
        if color.name()=='#e9e9e9':
                clickedbutton.setStyleSheet('background-color: {}'.format('black' if PLAYER == True else 'yellow'))

                CALCULATOR[0] -= 1
                CALCULATOR[1] = CALCULATOR[1] + 1 if PLAYER == True else CALCULATOR[1]
                CALCULATOR[2] = CALCULATOR[2] + 1 if PLAYER == False else CALCULATOR[2]
                if CALCULATOR[0]==0:
                    self.MessageScreen.setText('Конец')

                PLAYER = not PLAYER
                self.set_calc()
                self.recolor_turn()

        else:
            self.MessageScreen.setText('Выбирайте пустую клетку')


    def field_buttons(self):

        self.pushButton_1.clicked.connect(self.start_turn)
        self.pushButton_2.clicked.connect(self.start_turn)
        self.pushButton_3.clicked.connect(self.start_turn)
        self.pushButton_4.clicked.connect(self.start_turn)
        self.pushButton_5.clicked.connect(self.start_turn)
        self.pushButton_6.clicked.connect(self.start_turn)
        self.pushButton_7.clicked.connect(self.start_turn)
        self.pushButton_8.clicked.connect(self.start_turn)
        self.pushButton_9.clicked.connect(self.start_turn)
        self.pushButton_10.clicked.connect(self.start_turn)
        self.pushButton_11.clicked.connect(self.start_turn)
        self.pushButton_12.clicked.connect(self.start_turn)
        self.pushButton_13.clicked.connect(self.start_turn)
        self.pushButton_14.clicked.connect(self.start_turn)
        self.pushButton_15.clicked.connect(self.start_turn)
        self.pushButton_16.clicked.connect(self.start_turn)
        self.pushButton_17.clicked.connect(self.start_turn)
        self.pushButton_18.clicked.connect(self.start_turn)
        self.pushButton_19.clicked.connect(self.start_turn)
        self.pushButton_20.clicked.connect(self.start_turn)
        self.pushButton_21.clicked.connect(self.start_turn)
        self.pushButton_22.clicked.connect(self.start_turn)
        self.pushButton_23.clicked.connect(self.start_turn)
        self.pushButton_24.clicked.connect(self.start_turn)
        self.pushButton_25.clicked.connect(self.start_turn)
        self.pushButton_26.clicked.connect(self.start_turn)
        self.pushButton_27.clicked.connect(self.start_turn)
        self.pushButton_28.clicked.connect(self.start_turn)
        self.pushButton_29.clicked.connect(self.start_turn)
        self.pushButton_30.clicked.connect(self.start_turn)
        self.pushButton_31.clicked.connect(self.start_turn)
        self.pushButton_32.clicked.connect(self.start_turn)
        self.pushButton_33.clicked.connect(self.start_turn)
        self.pushButton_34.clicked.connect(self.start_turn)
        self.pushButton_35.clicked.connect(self.start_turn)
        self.pushButton_36.clicked.connect(self.start_turn)
        self.pushButton_37.clicked.connect(self.start_turn)
        self.pushButton_38.clicked.connect(self.start_turn)
        self.pushButton_39.clicked.connect(self.start_turn)
        self.pushButton_40.clicked.connect(self.start_turn)
        self.pushButton_41.clicked.connect(self.start_turn)
        self.pushButton_42.clicked.connect(self.start_turn)
        self.pushButton_43.clicked.connect(self.start_turn)
        self.pushButton_44.clicked.connect(self.start_turn)
        self.pushButton_45.clicked.connect(self.start_turn)
        self.pushButton_46.clicked.connect(self.start_turn)
        self.pushButton_47.clicked.connect(self.start_turn)
        self.pushButton_48.clicked.connect(self.start_turn)
        self.pushButton_49.clicked.connect(self.start_turn)
        self.pushButton_50.clicked.connect(self.start_turn)
        self.pushButton_51.clicked.connect(self.start_turn)
        self.pushButton_52.clicked.connect(self.start_turn)
        self.pushButton_53.clicked.connect(self.start_turn)
        self.pushButton_54.clicked.connect(self.start_turn)
        self.pushButton_55.clicked.connect(self.start_turn)
        self.pushButton_56.clicked.connect(self.start_turn)
        self.pushButton_57.clicked.connect(self.start_turn)
        self.pushButton_58.clicked.connect(self.start_turn)
        self.pushButton_59.clicked.connect(self.start_turn)
        self.pushButton_60.clicked.connect(self.start_turn)
        self.pushButton_61.clicked.connect(self.start_turn)
        self.pushButton_62.clicked.connect(self.start_turn)
        self.pushButton_63.clicked.connect(self.start_turn)
        self.pushButton_64.clicked.connect(self.start_turn)

    def start(self):
        global CALCULATOR
        # sendr = self.sender()
        # print(str(sendr.objectName()))

        self.MessageScreen.setText('Начало игры')
        self.startButton.setEnabled(False)
        self.pushButton_30.setStyleSheet('background-color: black;')
        self.pushButton_39.setStyleSheet('background-color: black;')
        self.pushButton_31.setStyleSheet('background-color: yellow;')
        self.pushButton_38.setStyleSheet('background-color: yellow;')
        CALCULATOR = [60, 2, 2]

        self.set_calc()
        self.field_buttons()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    ExampleApp.main()  # то запускаем функцию main()
