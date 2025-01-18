from PyQt6.QtWidgets import QApplication
import time

app = QApplication([])
from main_window import *
from menu_window import *
from random import choice, shuffle
class Question():
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', '1', '2', '3')
q2 = Question('Дім', 'house', '1', '2', '3')
q3 = Question('Миша', 'mouse', '1', '2', '3')
q4 = Question('Клавіатура', 'keybord', '1', '2', '3')

questions = [q1, q2, q3, q4]
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
cur_q = ''
def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
new_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == cur_q.answer:
                cur_q.got_right()
                lb_result.setText('Вірно!')
                answer.setChecked(False)
                break
            else:
                cur_q.got_wrong()
                lb_result.setText('Не вірно!')
                answer.setChecked(False)
def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText('Відповісти')

def rest():
    window.hide()
    n = sp_rest.value() * 60
    time.sleep(n)
    window.show()

def menu_generation():
    menu_win.show()
    window.hide()

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)
btn_menu.clicked.connect(menu_generation)
btn_rest.clicked.connect(rest)
btn_next.clicked.connect(click_ok)



window.show()
app.exec()