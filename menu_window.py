from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel
)
menu_win = QWidget()

lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть правильну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь:')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь:')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь:')

le_quest = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

btn_back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')

lb_header_stat = QLabel('Статистика')
lb_statistic = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_quest)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

vl_final = QVBoxLayout()
vl_final.addLayout(hl_question)
vl_final.addLayout(hl_buttons)
vl_final.addWidget(lb_header_stat)
vl_final.addWidget(lb_statistic)
vl_final.addWidget(btn_back)

menu_win.setWindowTitle('Меню')
menu_win.setLayout(vl_final)
menu_win.resize(350,350)





