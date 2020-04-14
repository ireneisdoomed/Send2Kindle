import smtplib
from login import from_email, pssw
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Conexión segura con el servidor

server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
try:
    server.login(from_email, pssw)
    print("Successful connection.")
except Exception as e:
    print(e)


# Creo objeto

mail = MIMEMultipart()
mail["From"] = from_email
mail["To"] = from_email
mail["Subject"] = "Convert"

# De mi objeto Multipart voy añadiéndole cada una de las partes
part1 = MIMEText("text", "plain")
content = "This message is from Python."
part1.set_payload(content)
mail.attach(part1)

# Adjunto archivo

# Mando el email

file = "GWAS.mobi"

with open(file, "rb") as attachment:
  # Creo otro objeto MIME con el formato predeterminado para mandar un archivo binario
  part2 = MIMEBase("application", "octet-stream")
  part2.set_payload(attachment.read())

# Codifico el archivo en caraceres ASCII

encoders.encode_base64(part2)


# Añado el objeto a mi objeto multiparte como antes

mail.attach(part2)


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