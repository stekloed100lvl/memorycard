from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QRadioButton, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup

class Question():
    def __init__(self, quest, right_answ, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answ =right_answ
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []

q1 = Question("Когда закончилась Вторая Мировая Война?", '1945', '1982', '1913', '1944')
q = Question("Сколько лет Бухаре?", '2500', '1200', '3000', '2100')
q2 = Question('Самая дорогая машина', 'крутая машинка', 'чуть менее крутая машинка', 'ведро с болтами', 'рухлядь')
q3 = Question('Тип вопрос', 'otvet', 'otvet', 'otvet', 'otvet')

question_list.append(q)
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)

app = QApplication([])
wind = QWidget()
wind.setWindowTitle("Memory Card")
wind.resize(400, 200)
question = QLabel()
rbtn1 = QRadioButton()
rbtn2 = QRadioButton()
rbtn3 = QRadioButton()
rbtn4 = QRadioButton()
btn = QPushButton("Ответить")

RadioGroup = QGroupBox("Варианты ответов:")


hline_group = QHBoxLayout()
wline_group1 = QVBoxLayout()
wline_group2 = QVBoxLayout()

wline_group1.addWidget(rbtn1)
wline_group1.addWidget(rbtn2)

wline_group2.addWidget(rbtn3)
wline_group2.addWidget(rbtn4)
hline_group.addLayout(wline_group1)
hline_group.addLayout(wline_group2)
RadioGroup.setLayout(hline_group)
puinstaller --nocnsole
AnsGroupBox = QGroupBox('Правильный ответ')
result = QLabel("Прав ты или нет")
correct = QLabel("ответ будет здесь ")
ans_v_line = QVBoxLayout()
ans_v_line.addWidget(result, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
ans_v_line.addWidget(correct, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(ans_v_line)

#группа с кнопками
ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn1)
ButtonGroup.addButton(rbtn2)
ButtonGroup.addButton(rbtn3)
ButtonGroup.addButton(rbtn4)

hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()
vline = QVBoxLayout()

hline1.addWidget(question, alignment = (Qt.AlignVCenter | Qt.AlignHCenter))
hline2.addWidget(RadioGroup)
hline2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
hline3.addWidget(btn)


vline.addLayout(hline1)
vline.addLayout(hline2)
vline.addLayout(hline3)

wind.setLayout(vline)
def show_ans():
    RadioGroup.hide()
    AnsGroupBox.show()
    btn.setText("Следующий вопрос")
def show_question():
    ButtonGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    ButtonGroup.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroup.show()
    btn.setText("Ответить")
def nextquest():
    wind.cur_question += 1
    if wind.cur_question == len(question_list):
        wind.cur_question = 0
    qt = question_list[wind.cur_question]
    ask(qt)
def text():
    if btn.text() == 'Ответить':
        check_answ()
    else:
        nextquest()
from random import shuffle
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q):
    shuffle(answers)
    question.setText(q.quest)
    answers[0].setText(q.right_answ)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    correct.setText(q.right_answ)
    show_question()
def show_correct(res):
    result.setText(res)
    show_ans()   
def check_answ():
    if answers[0].isChecked():
        show_correct("Правильно!")
    else:
        show_correct('Не правильно!')


ask(q)
btn.clicked.connect(text)
wind.cur_question = -1
nextquest()
wind.show()
app.exec_()
