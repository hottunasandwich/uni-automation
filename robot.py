from golestan import Golestan
username = '__your-username__'
password = '__your-password__'
units = ['350170201', '350170201', '350170201', '350170201']
robot = Golestan(username,password,units)
robot.login().goToPishkhaan().goToMainEntekhaabVahed().fillT01rows()
print('fuck golestan')