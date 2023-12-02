from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget ()
window.resize(500,500)
lbl = QLabel("Скільки буде 2+2")
ans1=QRadioButton("4")
ans2=QRadioButton("14")
ans3=QRadioButton("1")
ans4=QRadioButton("2")


mine_line=QVBoxLayout()
mine_line.addWidget(lbl)
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h1.addWidget(ans1)
h1.addWidget(ans2)
h2.addWidget(ans3)
h2.addWidget(ans4)
mine_line.addLayout(h1)
mine_line.addLayout(h2)
window.setLayout(mine_line)

def true_var_1():
    msg=QMessageBox()
    msg.setText("Павильно")
    msg.exec()

def false_var_2():
    msg = QMessageBox()
    msg.setText("Неправилно")
    msg.exec()

ans1.clicked.connect(true_var_1)
ans2.clicked.connect(false_var_2)
ans3.clicked.connect(false_var_2)
ans4.clicked.connect(false_var_2)

window.show()
app.exec()

