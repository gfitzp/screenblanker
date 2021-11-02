# screenblanker
Script to toggle screen power on Raspberry Pi

## To install
Copy the `screenblanker.desktop` file to the `~/.config/autostart/` directory and reboot.

```
mkdir -p ~/.config/autostart &&
cp screenblanker.desktop ~/.config/autostart &&
sudo reboot 
```

## To use
I wired a button between the GPIO pin 24 and ground. If you wire up a different GPIO pin make sure to change the pin number in the script.

The script should run in the background; push the button to toggle the screen backlight on or off.

The script can be called via crontab to enable/disable the screen at various times.

### To turn on
```
/usr/bin/python3 /home/pi/screenblanker.py noblank
```

### To turn off
```
/usr/bin/python3 /home/pi/screenblanker.py blank
```
