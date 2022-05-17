def sendMail(fromAddr, toAddr, msg):
    import smtplib
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()

    s.login('cheese04@tukorea.ac.kr', 'idnkialnwuzpeirh')
    s.sendmail(fromAddr, [toAddr],msg.as_string())
    s.close()

def sendTrainingMail():
    pass