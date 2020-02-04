from golestan import Golestan
username = '96235053'
password = '09389171299'
units = ['350170201', '350170201', '350170201', '350170201']
robot = Golestan(username,password,units)
robot.login().goToPishkhaan().goToMainEntekhaabVahed().fillT01rows()
print('fuck golestan')