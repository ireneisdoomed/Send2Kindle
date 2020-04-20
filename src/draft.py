import smtplib
from src.login import from_email, pssw
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
#mail["To"] = from_email
mail["Subject"] = "Convert"

# De mi objeto Multipart voy añadiéndole cada una de las partes
part1 = MIMEText("text", "html")
content = "You can follow me <a href='www.elpais.es'>here</a> for more projects."
part1.set_payload(content)
mail.attach(part1)

# Adjunto archivo

# Mando el email

# file = input("Enter path of the file. Supported formats: .mobi")
file = "GWAS.mobi"

with open(file, "rb") as attachment:
  # Creo otro objeto MIME con el formato predeterminado para mandar un archivo binario
  part2 = MIMEBase("application", "octet-stream")
  part2.set_payload(attachment.read())

# Codifico el archivo en caraceres ASCII

encoders.encode_base64(part2)

# Añado nombre al archivo

part2.add_header(
    "Content-Disposition",
    "attachment; filename= {}".format(file),
)

# Añado el objeto a mi objeto multiparte como antes

mail.attach(part2)


# Envío e-mail

server.sendmail(
  from_email,
  to_email,
  mail.as_string()) # Sólo admite string

# Cierro la conexión con el servidor
server.quit()
print("Done! Your ebook is in your e-mail awaiting authorization.")


"""
Para mandar HTML. En sendmail en mensaje: msg.as_string()

from email.mime.text import MIMEText

msg = MIMEText(u'<a href="www.elpais.es">Link</a>','html')
"""