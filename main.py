import smtplib
from login import from_email, pssw
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

# Conexión segura con el servidor

server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
try:
    server.login(from_email, pssw)
    print("Successful connection.")
except Exception as e:
    print(e)


# Adjunto

file = "GWAS.mobi"

mail = MIMEMultipart()
mail["From"] = from_email
mail["To"] = from_email
mail["Subject"] = "Convert"

#De mi objeto Multipart voy añadiéndole cada una de las partes
body = MIMEText("text", "plain")
content = "This message is from python"
body.set_payload("")
mail.attach(body)

# Mando el email

server.sendmail(
  from_email,
  #input("Please, write your Kindle e-mail: "),
  from_email,
  mail.as_string()) # Sólo admite string

# Cierro la conexión con el servidor
server.quit()


"""
Para mandar HTML. En sendmail en mensaje: msg.as_string()

from email.mime.text import MIMEText

msg = MIMEText(u'<a href="xxx">abc</a>','html')
"""