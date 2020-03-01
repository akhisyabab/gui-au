import pyautogui
import time

def click():
	pyautogui.click(clicks=1, button='left')

def pres_down_up(line):
	n = 0
	while(n < line):
		pyautogui.press('down')
		time.sleep(1)
		n += 1
	n = 0
	while(n < line):
		pyautogui.press('up')
		time.sleep(1)
		n += 1

# Function for text_editor
def text_editor(tab):
    text_editor_position = [1263, 128, 2]
    text_editor_up = text_editor_position
    pyautogui.moveTo(*tab)
    click()
    pyautogui.moveTo(*text_editor_up)
    click()
    pres_down_up(50)

# Function for chrome
def chrome(tab):
	def open_site(sites):
		for site in sites:
			time.sleep(2)
			pyautogui.hotkey('ctrl', 't')
			time.sleep(2)
			pyautogui.typewrite(site)
			pyautogui.press('enter')
			time.sleep(5)
			pres_down_up(5)

	pyautogui.moveTo(*tab)
	click()
	sites = [
		'https://realpython.com/python-sockets/',
		'https://stackoverflow.com/questions/23985531/certificate-verify-failed-oauth2',
		'https://requests-mock.readthedocs.io/en/latest/response.html',
		'https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/',
		'https://cloud.google.com/bigquery/docs/tutorials',
	]
	# Open tab
	open_site(sites)

	# Close tab
	n = 0
	while(n < len(sites)):
		pyautogui.hotkey('ctrl', 'w')
		n += 1

def execute():
	all_tab = {}
	input("Hello... Thank's for using simple gui-au."
		  " Make sure your app is opened. Press enter to continue.....")
	tab_count = int(input('How many application tabs have been opened ? (Number): '))
	for tab_item in range(tab_count):
		all_tab['tab{}'.format(tab_item+1)] = ''

	for i in range(tab_count):
		print('point your cursor to tab{}.., wait about 5 seconds'.format(i + 1))
		time.sleep(5)
		x, y = pyautogui.position()
		tab_position = []
		tab_position.append(x)
		tab_position.append(y)
		tab_position.append(2)
		print(tab_position)
		all_tab['tab{}'.format(i + 1)] = tab_position

	print(all_tab)

	chrome_order = input('Chrome tab order? (Number): ')
	text_editor_order = input('Text editore tab order? (Number): ')

	while True:
		chrome(all_tab['tab{}'.format(chrome_order)])
		text_editor(all_tab['tab{}'.format(text_editor_order)])
		# pyautogui.moveTo(*tab2)
		# click()

if __name__ == '__main__':
    execute()
