import os
os.system("pip install pyqt5")
import sys

import smtplib
from PyQt5.QtWidgets import QWidget , QApplication , QLabel , QVBoxLayout 
from PyQt5.QtWidgets import QHBoxLayout , QPushButton , QCheckBox , QLineEdit 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#from selenium import webdriver

class Pencere(QWidget):
    def __init__(self):
        
        super().__init__()

        self.init_ui()
        

    def init_ui(self):
        self.username = QLineEdit("2003emirkanesme@gmail.com")
        
        self.passwd = QLineEdit("")
        self.passwd.setEchoMode(QLineEdit.Password)
        
        self.to     = QLineEdit("2003emirkanesme@gmail.com")
        self.title = QLineEdit("Başlık")
        self.mail = QLineEdit("Yazı")
        self.yazi = QLabel("Hoşgeldin root@ebby:~#")
        self.yazi2 = QLabel("Mail Yollamadan Bir Defaya Mahsus Daha Az Güvenli Uygulama Erişimini Aktif Ediniz !!!\nhttps://myaccount.google.com/lesssecureapps ")
        #self.buton_app = QPushButton("Less Secure Apps")
        self.buton_yolla = QPushButton("Yolla")
        self.buton_temizle = QPushButton("Temizle")
        
        
        
        h_box = QHBoxLayout()        
        h_box.addStretch()
        h_box.addWidget(self.buton_temizle)
        h_box.addWidget(self.buton_yolla)
        #h_box.addWidget(self.buton_app)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.username)
        v_box.addWidget(self.passwd)
        v_box.addWidget(self.to)
        v_box.addWidget(self.title)
        v_box.addStretch()               
        v_box.addWidget(self.mail)
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.yazi2)
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.buton_yolla.clicked.connect(self.mailyolla)
        self.buton_temizle.clicked.connect(self.clear)
        #self.buton_app.clicked.connect(self.lesssec)


        self.setWindowTitle("root@ebby:~# Mail Automation")
        self.setLayout(v_box)

            
        self.show()

    def mailyolla(self):
        
        try:

            usr_mail = self.username.text()  
            usr_passwd =  self.passwd.text()  
            msg_to  = self.to.text()       
            ImgFileName = "root.png" 
            subject = self.title.text()  #input("Title : ")
            body = self.mail.text()  #input("Text : ")
            img_data = open(ImgFileName, 'rb').read()
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = usr_mail
            msg["To"]   = msg_to


            text = MIMEText(body)
            msg.attach(text)
            image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            msg.attach(image)

            s = smtplib.SMTP("smtp.gmail.com",587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(usr_mail,usr_passwd)
            s.sendmail(msg["From"],msg["To"],msg.as_string())        
            self.yazi.setText("Mail Başarıyla Gönderildi !")   
            s.quit()
        
        except:
            self.yazi.setText("Mail Gönderilemedi !!!!")
    
    def clear(self):
        self.mail.clear()
"""
    def lesssec(self):
        url = "https://myaccount.google.com/lesssecureapps"
        browser = webdriver.Firefox()
        browser.get(url)
        dfsgsdf = input("Devam Etmek İçin Enter'a basınız ! ")
        browser.close()
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec_())