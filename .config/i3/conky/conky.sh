#!/bin/bash



#-----Created By-----#
#-----walo Ahammed-----#
#-----http://www.obakwalo.com-----#



# Kill Conky If Running . If you want to run this conky along with other
# Put a "#" Symbol before the "test" word from below line .
#test -z "`pgrep conky`" || killall -9 conky

# The directory of conkyrcs
#conky_dir="./conkyrc"

# The command for start conkys
START="conky -d -c"

# The Conkys
$START /home/walo/.config/i3/conky/conkyrc/foxconky

$START /home/walo/.config/i3/conkyrc