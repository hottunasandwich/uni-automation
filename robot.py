from golestan import Golestan
username = '_username_'
password = '_password_'
units = ['350170201', '350170201', '350170201', '350170201']
robot = Golestan(username,password,units)
robot.login().goToPishkhaan().goToMainEntekhaabVahed().fillT01rows()
