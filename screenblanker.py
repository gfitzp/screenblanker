#!/usr/bin/python3

import os
import subprocess
import sys

import RPi.GPIO as GPIO

from signal import pause

def get_current_status():
    process = subprocess.Popen(
        [
            "/usr/bin/xset",
            "-display",
            ":0",
            "q",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    return(stdout.decode("utf-8"), stderr.decode("utf-8"))

def toggle(pin):
    stdout, stderr = get_current_status()
    if "prefer blanking:  no" in stdout:
        turn_off()
    else:
        turn_on()

def turn_off():
    print("Screen is on; turning screen off.")
    os.system(
    """
        /usr/bin/xset -display :0 s blank &&
        /usr/bin/xset -display :0 s reset &&
        /usr/bin/xset -display :0 s activate
    """
    )

def turn_on():
    print("Screen is off; turning screen on.")
    os.system(
    """
        /usr/bin/xset -display :0 s reset &&
        /usr/bin/xset -display :0 s noblank
    """
    )

if __name__ == "__main__":
    os.environ["DISPLAY"] = ":0"
    os.environ["XAUTHORITY"] = "/home/pi/.XAuthority"

    if len(sys.argv) == 1:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            print("Waiting for button input to toggle screen status...")
            GPIO.add_event_detect(24, GPIO.RISING, callback=toggle, bouncetime=200)
            try:
                pause()
            except KeyboardInterrupt:
                GPIO.cleanup()
            GPIO.cleanup()

    else:
        if sys.argv[1] == "blank":
            print("User requested screen off. ", end="")
            stdout, stderr = get_current_status()
            if "prefer blanking:  no" in stdout:
                turn_off()
            else:
                print("Screen is already off.")

        elif sys.argv[1] == "noblank":
            print("User requested screen on. ", end="")
            stdout, stderr = get_current_status()
            if "prefer blanking:  yes" in stdout:
                turn_on()
            else:
                print("Screen is already on.")

        else:
            print(f"'{sys.argv[1]}' is an invalid argument!")
            print("Should be 'blank' or 'noblank', or no argument for button toggle.")