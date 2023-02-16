import pyautogui as pg
import time, keyboard, cv2
import numpy as np


def confirm():
    start_time = time.time()
    while True:
            template = cv2.imread('confirm.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val >= 0.8:
                x, y = max_loc
                w, h = template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Confirm Button Found")
                pg.moveTo(x,y)
                time.sleep(0.5)
                pg.click(x, y)
                time.sleep(1)
                pg.moveTo(1090, 500)
                break # exit the loop
            else:
                print("Confirm Button Not Found")
                time.sleep(0.01)
                elapsed_time = time.time() - start_time
                print(elapsed_time, "Second and If not Found In 30 Seconds Closing The Loop")
                if elapsed_time >= 30:
                    print("Elapsed time exceeded 30 seconds, exiting the loop")
                    break # exit the loop  


def nested_loop_Twitter_fallow():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://www.like4like.org/user/earn-twitter.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    time.sleep(0.5)
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
              print("Exiting the program...")
              break  # finishing the loop
        time.sleep(1)
        start_time = time.time()
        while True:
                button1_template = cv2.imread('tfnomore.png', cv2.IMREAD_GRAYSCALE)
                button2_template = cv2.imread('twfb1.png', cv2.IMREAD_GRAYSCALE)
                screenshot = np.array(pg.screenshot())
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
                button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
                button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
                button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
                if button1_max_val >= 0.8:
                    x, y = button1_max_loc
                    w, h = button1_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Twitter Earnings No More Button Found")
                    time.sleep(0.5)
                    nested_loop_Insta_fallow()

                elif button2_max_val >= 0.8:
                    x, y = button2_max_loc
                    w, h = button2_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Twitter Earing Button Found")
                    time.sleep(1)
                    pg.click(x, y)
                    pg.moveTo(1090, 500)
                    time.sleep(1)
                    break                   
                else:
                    print("Buttons are Not Found Please Check The Images Or check The Program")
                    time.sleep(0.1)
                    elapsed_time = time.time() - start_time
                    print(start_time)
                    print(elapsed_time)
                    if elapsed_time >= 20:
                        print("Elapsed time exceeded 20 seconds, exiting the loop")
                        nested_loop_Insta_fallow()
                        break # exit the loop
        start_time = time.time()
        while True:
            template = cv2.imread('twfb2.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val >= 0.8:
                x, y = max_loc
                w, h = template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Twitter Fallow Button Found")
                time.sleep(0.5)
                pg.click(x, y)
                time.sleep(1)
                pg.moveTo(1090, 500)
                pg.hotkey("ctrl", "w")
                break # exit the loop
            else:
                print("Twitter Fallow Button Not Found")
                time.sleep(0.01)
                elapsed_time = time.time() - start_time
                print(elapsed_time, "Second and If not Found In 30 Seconds Closing The Loop")
                if elapsed_time >= 30:
                    print("Elapsed time exceeded 30 seconds, exiting the loop")
                    pg.hotkey("ctrl", "w")
                    break # exit the loop     
        confirm()

def nested_loop_Insta_fallow():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://www.like4like.org/user/earn-instagram-follow.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    time.sleep(3)
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
              print("Exiting the program...")
              break  # finishing the loop
        time.sleep(1)
        start_time = time.time()
        while True:
            button1_template = cv2.imread('tfnomore.png', cv2.IMREAD_GRAYSCALE)
            button2_template = cv2.imread('instafollow1.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
            button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
            button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
            button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
            if button1_max_val >= 0.8:
                x, y = button1_max_loc
                w, h = button1_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Instagram Earnings No More Found")
                time.sleep(0.5)
                nested_loop_Youtube_subs()
            elif button2_max_val >= 0.8:
                x, y = button2_max_loc
                w, h = button2_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Instagram Earing Button Found")
                time.sleep(1)
                pg.click(x, y)
                pg.moveTo(1090, 500)
                time.sleep(1)
                break                   
            else:
                print("Buttons are Not Found Please Check The Images Or check The Program")
                time.sleep(0.1)
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                if elapsed_time >= 30:
                    print("Elapsed time exceeded 20 seconds, exiting the loop")
                    nested_loop_Youtube_subs() 
        start_time = time.time()       
        while True:
                button1_template = cv2.imread('instafollow2.png', cv2.IMREAD_GRAYSCALE)
                button2_template = cv2.imread('instafollow3.png', cv2.IMREAD_GRAYSCALE)
                screenshot = np.array(pg.screenshot())
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
                button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
                button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
                button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
                if button1_max_val >= 0.8:
                    x, y = button1_max_loc
                    w, h = button1_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Insta Follow Button Found")
                    pg.click(x, y)
                    time.sleep(3)
                    pg.moveTo(1090, 500)
                    pg.hotkey("ctrl", "w")
                    break # exit the loop
                elif button2_max_val >= 0.8:
                    x, y = button2_max_loc
                    w, h = button2_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Insta Unfallow Button Found")
                    time.sleep(1)
                    pg.click(x, y)
                    pg.moveTo(1090, 500)
                    time.sleep(1)
                    pg.hotkey("ctrl", "w")
                    break # exit the loop
                else:
                    print("Insta Fallow Unfallow Button Not Found")
                    time.sleep(0.1)
                    elapsed_time = time.time() - start_time
                    print(elapsed_time)
                    if elapsed_time >= 20:
                        print("Elapsed time exceeded 20 seconds, exiting the loop")
                        pg.hotkey("ctrl", "w")
                        break # exit the loop

        confirm()


def nested_loop_Youtube_subs():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://www.like4like.org/user/earn-youtube-subscribe.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    time.sleep(3)
    
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
            print("Exiting the program...")
            break  # finishing the loop
        time.sleep(0.5)
        start_time = time.time() 
        while True:
            button1_template = cv2.imread('ytsubsnomore.png', cv2.IMREAD_GRAYSCALE)
            button2_template = cv2.imread('ytsb1.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
            button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
            button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
            button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
            if button1_max_val >= 0.8:
                x, y = button1_max_loc
                w, h = button1_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Youtube Earnings No More Found")
                time.sleep(0.5)
                nested_loop_Twitter_fallow()
            elif button2_max_val >= 0.8:
                x, y = button2_max_loc
                w, h = button2_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Youtube Earing Button Found")
                time.sleep(1)
                pg.click(x, y)
                pg.moveTo(1090, 500)
                time.sleep(1)
                break                   
            else:
                print("Buttons are Not Found Please Check The Images Or check The Program")
                time.sleep(0.1)
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                if elapsed_time >= 30:
                    print("Elapsed time exceeded 20 seconds, exiting the loop")
                    nested_loop_Twitter_fallow() 
        start_time = time.time()
        while True:
            button1_template = cv2.imread('ytsb2.png', cv2.IMREAD_GRAYSCALE)
            button2_template = cv2.imread('ytsb3.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
            button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
            button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
            button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
            if button1_max_val >= 0.8:
                x, y = button1_max_loc
                w, h = button1_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Youtube Subscribe Button Found")
                time.sleep(1)
                pg.click(x, y)
                time.sleep(3)
                pg.moveTo(1090, 500)
                pg.hotkey("ctrl", "w")
                break # exit the loop
            elif button2_max_val >= 0.8:
                x, y = button2_max_loc
                w, h = button2_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Youtube Unsubscribe Button Found")
                time.sleep(1)
                pg.click(x, y)
                pg.moveTo(1090, 500)
                time.sleep(1)
                pg.hotkey("ctrl", "w")
                break # exit the loop
            else:
                print("Youtube Subscribe Or Unsubscribe Button Not Found")
                time.sleep(0.1)
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                if elapsed_time >= 20:
                    print("Elapsed time exceeded 20 seconds, exiting the loop")
                    pg.hotkey("ctrl", "w")
                    break # exit the loop
        confirm()


pg.click(557,47)
nested_loop_Youtube_subs()
#nested_loop_Twitter_fallow()
#nested_loop_Insta_fallow()
            
            