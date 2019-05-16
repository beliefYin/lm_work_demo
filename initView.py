import globalVar as g_
from login import Login
from addNewContrView import AddNewContrView
from homePage import HomePage
from contractView import ContractView


g_.theViewManager.register('Login', Login)
g_.theViewManager.register('HomePage', HomePage)
g_.theViewManager.register('AddNewContrView', AddNewContrView)
g_.theViewManager.register('ContractView', ContractView)