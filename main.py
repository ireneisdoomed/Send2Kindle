import smtplib

# Conexión segura con el servidor

from_email = "sendtokindle.py@gmail.com"
pssw = "Youtube2020"

server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
try:
    server.login(from_email, pssw)
    print("Successful connection.")
except Exception as e:
    print(e)

# Mando el email
server.sendmail(
  from_email,
  #input("Please, write your Kindle e-mail: "),
  "sendtokindle.py@gmail.com",
  "This message is from python") # Sólo admite string

# Cierro la conexión con el servidor
server.quit()


"""
Para mandar HTML. En sendmail en mensaje: msg.as_string()

from email.mime.text import MIMEText

msg = MIMEText(u'<a href="xxx">abc</a>','html')
"""