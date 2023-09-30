import ssl
import smtplib # simple mail  transfer protocol

kullanici = "20060888@stu.omu.edu.tr"
sifre = "selserhat01!"

alici = kullanici
baslik = "Pythondan email yollamak"
mesaj= "dusuk guvenlik yap ve pythondan mesaj gonder"


context = ssl.create_default_context()

port = 465

host = "smtp.gmail.com"

eposta_sunucu = smtplib.SMTP_SSL(host = host, port = port, context = context)
eposta_sunucu.login(kullanici, sifre)
eposta_sunucu.sendmail(kullanici, alici, mesaj)

# Eklentili posta gönderimi

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

posta = MIMEMultipart()
posta["From"] = kullanici
posta["To"] = alici
posta["Subject"] = baslik

posta.attach(MIMEText(mesaj, "plain"))

eklenti_dosya_ismi = "C:\\Users\\serhat\\Desktop\\plc.jpeg"
with(open(eklenti_dosya_ismi , "rb")) as eklenti_dosyasi:
    payload = MIMEBase("application", "octate_stream")

    payload.set_payload((eklenti_dosyasi).read())
    encoders.encode_base64(payload)
    payload.add_header("Content-Decomposition","attachment", filename = eklenti_dosya_ismi)
    posta.attach(payload)

    posta_str = posta.as_string()

port = 465

host = "smtp.gmail.com"

eposta_sunucu = smtplib.SMTP_SSL(host = host, port = port, context = context)
eposta_sunucu.login(kullanici, sifre)
eposta_sunucu.sendmail(kullanici, alici, posta_str)

# mail okuma

from imap_tools import MailBox

posta_kutusu = MailBox("imap.gmail.com")
posta_kutusu.login(kullanici,sifre,initial_folder="INBOX")

from imap_tools import AND
import datetime

kriter = AND(date_gte= datetime.date(2023,9,1), from_=kullanici)
for msg in posta_kutusu.fetch(kriter):
    print(msg.text)