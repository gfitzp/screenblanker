# screenblanker
Script to toggle screen power on Raspberry Pi

## To install
(Assuming the `screenblanker` directory is saved at `/home/pi/Documents/`...)

Copy the `screenblanker.service` file to the appropriate systemd directory and reboot.

```
sudo cp screenblanker.service /etc/systemd/system/ &&
sudo systemctl daemon-reload &&
sudo systemctl enable screenblanker.service &&
sudo reboot
```

On Bullseye I needed to also comment out the vc4-kms-v3d driver in /boot/config.txt:

```
# Enable DRM VC4 V3D driver
#dtoverlay=vc4-kms-v3d
```

## To use
I wired a button between the GPIO pin 24 and ground. If you wire up a different GPIO pin make sure to change the pin number in the script.

To prevent the button from bouncing, install a 100nF capacitor in parallel between GPIO pin 24 and ground as well. (See https://forums.raspberrypi.com/viewtopic.php?t=131440&start=50#p890185 for info.)

The script should run in the background; push the button to toggle the screen backlight on or off.

The script can be called via crontab to enable/disable the screen at various times.

### To turn on
```
/usr/bin/python3 /home/pi/Documents/screenblanker/screenblanker.py noblank
```

### To turn off
```
/usr/bin/python3 /home/pi/Documents/screenblanker/screenblanker.py blank
```
