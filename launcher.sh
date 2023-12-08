!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/michael/ton-o-mat
while true
do
    pipenv run /home/michael/ton-o-mat/env/bin/python /home/michael/ton-o-mat/src/manageToken.py
    echo oops, restarting...
done

