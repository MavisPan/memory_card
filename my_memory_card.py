from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox,
    QPushButton, QHBoxLayout, 
    QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup)
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

questions_list = []
questions_list.append(Question('Какое название дано главному злодею Моей Геройской Академии?',
'Все за одного', 'Один за всех', 'Всемогущий', 'Хитоши Шинсо'))
questions_list.append(Question('Сколько учеников учится на геройском курсе в Моей Геройской Академии?',
'20', '30', '18', '23'))
questions_list.append(Question('Сколько факультетов существует в Хогвартсе?',
'4', '2', '5', '1'))
questions_list.append(Question('На каком клипе Stray Kids больше всего просмотров?',
'Gods menu', 'Thunderous', 'Maniac', 'Miroh'))
questions_list.append(Question('Кто занял 1 место на Спортивном фестивале UA в Моей Геройской Академии?',
'Кацуки Бакуго', 'Изуку Мидория', 'Иида Тенья', 'Тодороки Шото'))
questions_list.append(Question('Со скольки лет должна проявляться причуда?',
'с 4', 'с 10', 'с 8', 'с 5'))
questions_list.append(Question('Любимое блюдо Мидории?',
'Кацудон', 'Том Ям', 'Рамен', 'Тодороки Шото'))
questions_list.append(Question('Сколько участниц в K-pop группе ITZY?',
'5', '4', '12', '7'))
questions_list.append(Question('Почему Виктор Петрович занижает всем оценки?',
 'Столбняк - это не болезнь','Просто так', 'Плохо выполнена работа', 'Oshiete, oshiete yo'))
questions_list.append(Question('Какой цвет волос у Рэм?',
'Голубой', 'Розовый', 'Фиолетовый', 'Оранжевый'))
questions_list.append(Question('Какого цвета Папус?',
'Зелёный', 'Синий', 'Красный', 'Оранжевый'))
questions_list.append(Question('Какое максимальное количество баллов даётся в Впр по Русскому языку за 8 класс?',
'52', '48', '55', '37'))
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400,300)
btn_OK = QPushButton ('Ответить')
lb_Question = QLabel ('В каком году была основана Москва?')
RadioGroupBox = QGroupBox ('Варианты ответов')


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

rbtn_1 = QRadioButton ('1147')
rbtn_2 = QRadioButton ('1242')
rbtn_3 = QRadioButton ('1861')
rbtn_4 = QRadioButton ('1943')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1= QHBoxLayout()
layout_line2= QHBoxLayout()
layout_line3= QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch (1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout ()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addSpacing(5)
layout_card.addLayout(layout_line3, stretch=8)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

window.score = 0
window.total = 0    
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\nВсего вопросов:', window.total,'\nПравильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[2].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')
def next_question():
    '''window.cur_question = window.cur_question + 1'''
    window.total += 1
    print('Статистика\nВсего вопросов:', window.total,'\nПравильных ответов:', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    '''if cur_question >= len(questions_list):
        cur_question = 0
    q = questions_list[cur_question]'''
    ask(q)
    
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.cur_question = -1

btn_OK.clicked.connect(click_OK)
window.setLayout(layout_card)
next_question()

window.show()
app.exec()

