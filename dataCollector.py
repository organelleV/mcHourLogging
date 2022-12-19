import datetime
import time
import mcServerStatus
import os

def save_player_count(player_count):
    # Get the current timestamp
    timestamp = datetime.datetime.now()

    # Check if the file exists and has data
    file_exists = os.path.exists('player_counts.csv') and os.path.getsize('player_counts.csv') > 0

    # Save the player count and timestamp to a file or database
    with open('player_counts.csv', 'a') as f:
        # Write the column headers if the file is empty
        if not file_exists:
            f.write(f"timestamp,player_count\n")

        # Write the data for the current run
        f.write(f"{timestamp},{player_count}\n")


player_count = mcServerStatus.getNumPlayers()
save_player_count(player_count)
while True:
    # Get the current time
    now = datetime.datetime.now()

    # Check if the current time is within the desired time range (e.g., 8:00 AM to 8:00 PM)
    if now.hour >= 8 and now.hour < 20:
        player_count = mcServerStatus.getNumPlayers()
        save_player_count(player_count)

    # Sleep for 20 minutes
    time.sleep(1200)
