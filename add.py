import pyautogui, time


with open("songlist.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

time.sleep(30)    

for x in range(len(array)):
    print(array[x])
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.typewrite(array[x])
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(582, 297)
    time.sleep(1)
    pyautogui.click(1820, 21)

