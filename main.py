import time
import pyautogui as pg

def main():
    number = pg.prompt("Amount of times you wanna spam..", "SPAMBOT")
    spam = pg.prompt("Type something (You'll have 5 seconds): ", "SPAMBOT")
    time.sleep(5)

    for i in range(int(number)):
        pg.write(str(spam))
        pg.press("enter")

main()
