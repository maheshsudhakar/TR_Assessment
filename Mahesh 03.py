import pyautogui, time

class saplogonBOT(object):
	def __init__(self,usr,pw,inst,tc):
		self.userid=usr
		self.password=pw
		self.instance=inst
		self.tco=tc

	def activate_preinvoke(self):
		pyautogui.hotkey('win', 'd')


	def activate_saplogon(self):
		try:
			pyautogui.hotkey('win','r')
			pyautogui.typewrite('saplogon')
			pyautogui.press('enter')

			return True
		except:
			return False

	def activate_postinvoke(self):
		pyautogui.hotkey('win','up')

	def open_instance(self):
		try:
			pyautogui.hotkey('ctrl','f')
			pyautogui.typewrite(self.instance)
			pyautogui.press('enter')
			return True
		except:
			return False
	def sap_login(self):
		pyautogui.typewrite(self.userid)
		pyautogui.press('tab')
		pyautogui.typewrite(self.password)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.press('tab')
		pyautogui.press('enter')
		pyautogui.press('enter')
	def sap_tc(self):
		time.sleep(1)
		pyautogui.press('tab')
		time.sleep(1)
		pyautogui.hotkey('shiftright','tab')
		time.sleep(1)
		pyautogui.typewrite(self.tco)
		pyautogui.press('enter')	


############################################

if __name__=='__main__':
	mysap=saplogonBOT('username','password','instance','transaction_code')

	mysap.activate_preinvoke()
	time.sleep(2)
	mysap.activate_saplogon()
	time.sleep(4)
	mysap.activate_postinvoke()
	time.sleep(5)
	mysap.open_instance()
	time.sleep(5)
	mysap.sap_login()
	time.sleep(7)
	mysap.sap_tc()