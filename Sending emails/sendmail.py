import smtplib

myEmailID = 'myemail@gmail.com'
myPassword = 'Your Email Password'
receiverEmailId = 'receiver@gmail.com'
emailSubject = 'Your subject here'
emailBody = 'Your Email body here'


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()#test
smtpObj.starttls()
smtpObj.login(myEmailID, myPassword)
smtpObj.sendmail(myEmailID, receiverEmailId, 'Subject: {}\n{}'.format(emailSubject,emailBody))
smtpObj.quit()


#smtp.gmail.com
#Outlook.com/Hotmail.com smtp-mail.outlook.com
#Yahoo Mail smtp.mail.yahoo.com
#smpt.mail.att.net(port 465)
#Comcast smtp.comcast.net
#Verizon smtp.verizon.net(port 465)
