:q!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/michael/ton-o-mat
source  /home/michael/ton-o-mat/env/bin/activate
#fluidsynth -a alsa -m alsa_seq -i -l -s -g 1.0 /usr/share/sounds/sf2/FluidR3_GM.sf2 &
python /home/michael/ton-o-mat/src/manageToken.py 
cd /
