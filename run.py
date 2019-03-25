import pyautogui
import time

# get mouse position : pyautogui.position()
# example = (x, y,  duration)
tab1 = [114, 1064, 2]
tab2 = [456, 1064, 2]
tab3 = [747, 1064, 2]
tab4 = [919, 1064, 2]
tab5 = [1129, 1064, 2]
tab6 = [1500, 1064, 2]

text_editor_position = [1446, 125, 3]

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

def open_site(sites):
	for site in sites:
		time.sleep(2)
		pyautogui.hotkey('ctrl', 't')
		time.sleep(2)
		pyautogui.typewrite(site)
		pyautogui.press('enter')
		time.sleep(5)
		pres_down_up(3)

# Function for text_editor
def text_editor(tab):
	text_editor_up = text_editor_position

	pyautogui.moveTo(*tab)
	click()
	pyautogui.moveTo(*text_editor_up)
	click()
	pres_down_up(3)

# Function for chrome
def chrome(tab):
	pyautogui.moveTo(*tab)
	click()

	sites = [
		'https://en.wikipedia.org/wiki/Main_Page'
	]
	# Open tab
	open_site(sites)

	# Close tab
	n = 0
	while(n < len(sites)):
		pyautogui.hotkey('ctrl', 'w')
		n += 1

while True:
	chrome(tab1)
	text_editor(tab2)
