import pytesseract
from PIL import Image
from PIL import ImageGrab
from mss import mss
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

quantity = 70

for i in range(int(quantity)):
    time.sleep(2)
    image = ImageGrab.grab(bbox=(320, 539, 720, 640))
    image.save('screen.png')
    img = Image.open('screen.png')
    problemm = pytesseract.image_to_string(img)
    print(problemm)
    problem = list(problemm)
    print(len(problem))
    print(problem)
            if str(problem[i]) == str(4):
            if (str(problem[i-1]) == str(1) or str(problem[i-1]) == str(2) or str(problem[i-1]) == str(3)) and(str(problem[i+1]) == str(1) or str(problem[i+1]) == str(2) or str(problem[i+1]) == str(3)):
                problem[i] = "+"
            elif str(problem[i - 1]) == "3" or str(problem[i - 1]) == "5" or str(problem[i - 1]) == "2" or str(problem[i - 1]) == "1":
                problem.pop(i)
            else:
                problem[i] = 1
        elif str(problem[i]) == str(5):
            if (str(problem[i-1]) == str(1) or str(problem[i-1]) == str(2) or str(problem[i-1]) == str(3)) and(str(problem[i+1]) == str(1) or str(problem[i+1]) == str(2) or str(problem[i+1]) == str(3)):
                problem[i] = "+"
            elif str(problem[i-1]) == "3" or str(problem[i-1]) == "5":
                problem.pop(i)
            else:
                problem[i] = 3
    print(problem)
    for i in range(len(problem) - 3):
        # if int(problem[i]) == 14:
        #     problem[i] = 1
        try:
            if i == 0:
                ans = int(problem[i])
            else:
                # if str(problem[i+1]) == str(4) or str(problem[i+1]) == str(5):
                #     problem.pop(i)
                if i % 2 == 0:
                    # print(problem[i])
                    if problem[i - 1] == "-":
                        ans -= int(problem[i])
                    else:
                        ans += int(problem[i])
        except:
            pass
    print(ans)
    if ans == 1:
        pyautogui.click(x=565, y=633)
    elif ans == 2:
        pyautogui.click(x=644, y=711)
    else:
        pyautogui.click(x=629, y=770)