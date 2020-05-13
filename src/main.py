import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from src.convert import convert
from dotenv import load_dotenv
import os

load_dotenv()

from_email = os.getenv("from_email")
pssw = os.getenv("pssw")

def crearConexion():
  # Conexión segura con el servidor

  server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
  try:
      server.login(from_email, pssw)
      print("Successful connection! Cooking up your book...")
      return server
  except Exception as e:
      print(e)


def crearMIME(file, to_email):
  # Creo objeto

  mail = MIMEMultipart()
  mail["From"] = from_email
  mail["To"] = to_email
  mail["Subject"] = "convert"

  # De mi objeto Multipart voy añadiéndole cada una de las partes
  part1 = MIMEText("text", "html")
  content = "Follow me <a href='https://github.com/ireneisdoomed'>here</a> for more projects!"
  part1.set_payload(content)
  mail.attach(part1)

  # Compruebo formato archivo

  supportedFormats = ["doc", "docx", "html", "htm", "rtf", "jpeg", "jpg", "mobi", "azw", "gif", "png", "bmp", "pdf"]

  
  if file.endswith(tuple(supportedFormats)) == False:
    convertedFormat = "convertedBook.mobi"
    convert(file, convertedFormat)
    file = convertedFormat


  # Adjunto archivo

  with open(file, "rb") as attachment:
    # Creo otro objeto MIME con el formato predeterminado para mandar un archivo binario
    part2 = MIMEBase("application", "octet-stream")
    part2.set_payload(attachment.read())

  # Codifico el archivo en caracteres ASCII

  encoders.encode_base64(part2)

  # Añado nombre al archivo

  part2.add_header(
      "Content-Disposition",
      "attachment; filename= {}".format(file),
  )

  # Añado el objeto a mi objeto multiparte como antes

  mail.attach(part2)

  return mail

def mandar(to_email, mail, server):
  # Envío e-mail
  try:
    server.sendmail(
      from_email,
      to_email,
      mail.as_string()) # Sólo admite string
  except Exception:
    print("El envío ha fallado.")

def cerrarConexion(server):
  # Cierro la conexión con el servidor
  server.quit()
  print("Done! You can find you ebook in your Kindle in a few minutes. If not, check your e-mail for any problems.")
