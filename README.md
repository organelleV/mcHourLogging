# mcHourLogging
tool to track when users are playing on a Minecraft server
Then visualize the data with a weekly and daily chart

uses rcon to connect to a Minecraft server and run remote logging commands, and matplotlib for displaying data

## installing rcon
```pip install mcrcon```

## setup rcon
in ```mcServerStatus.py``` set server name and rcon password

## verify timezone
run ```date``` if time incorrect follow: https://www.tecmint.com/set-time-timezone-and-synchronize-time-using-timedatectl-command/

## running

Collect data (runs in background) ```./start.sh```

Display graph ```python3 visualizeData.py```

