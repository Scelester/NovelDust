import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login('nabinpauudel664@gmail.com','narayanmobila')
server.sendmail('nabinpauudel664@gmail.com','nabinisgreat53@gmail.com',
				'this is a test mode')


server.quit()