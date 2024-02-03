from email.message import EmailMessage
from pydantic import EmailStr
from app.config import settings



def tanks_for_registrating_template(reciver: EmailStr):
    email = EmailMessage()

    email['Subject'] = "Подтверждение регистрации"
    email['From'] = settings.SMTP_USER
    email['To'] = reciver

    email.set_content(
        "<h1>Спасибо за регистрацию на платформе PlannerFastAPI!</h1>",
        subtype="html"
    )

    return email






    sender = settings.EMAIL_SENDER 
    password = settings.EMAIL_PASSWORD

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

        return "The message has been sent successefuly!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"