import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(email, login, passwd):
    """
    Arguments : Login, password and email
    Send mail to user
    """

    fromaddr = "binomejoetfab@gmail.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Vos identifiants"
    body = "Bonjour, \nVous être à présent enregistré dans la base de \
        l'entreprise et pouvez accéder aux différents services.\nLogin \
        : " + login + "\nMot de passe : " + passwd + "\nCordialement"
    msg.attach(MIMEText(body, 'plain'))

    # Connexion Serveur SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Login et Mot de Passe du compte Gmail
    server.login(fromaddr, "Azertyuiop")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
server.quit()
