#!/bin/bash
IN=eDP-1
EXT=HDMI-1-0

if xrandr | grep "$EXT disconnected" ; then
    xrandr --output $IN--mode 1600x900 --primary --output $EXT --off
else
   xrandr --output $IN --mode 1600x900 --pos 1920x180 --rotate normal --output $EXT --primary --mode 1920x1080 --pos 0x0 --rotate normal
fi
