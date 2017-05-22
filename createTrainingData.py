import numpy as np
from grabscreen_mss import grab_screen
import cv2
import time
from getkeys import key_check
import os
from colorama import init as colorama_init
from colorama import Fore, Back, Style


# initalize colorama
colorama_init(autoreset=True)


def keys_to_output(keys):
    # Convert keys to multi-hot array

    output = [0, 0, 0]

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist.  Starting fresh!')
    training_data = []

def main():

    for i in list(range(2))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    while(True):

        if not paused:
            # 800x600 windowed mode
            # Sentdex's code
            # screen = grab_screen(region=(0, 40, 800, 640))
            screen = grab_screen()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160, 120))
            cv2.imshow('test-screen', screen)
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            if len(training_data) % 1000 == 0:
                print(len(training_data), ': ', Back.RED + 'SAVED')
                np.save(file_name, training_data)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print(Fore.CYAN + 'unpaused')
                time.sleep(1)
            else:
                print(Fore.CYAN + 'pausing')
                paused = True
                time.sleep(1)
        # NOTE: this deletes the datafile
        if 'X' in keys:
            if os.path.isfile(file_name):
                os.remove(file_name)
                break
            else:
                break

main()
