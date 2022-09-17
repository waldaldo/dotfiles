#!/bin/bash
jq -r '.song.title, .song.artist' <"$HOME/.config/Google Play Music Desktop Player/json_store/playback.json" | sed ':a;N;$!ba;s/\n/ \- /'