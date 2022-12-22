from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import csv
import plotly.express as px

def string_to_datetime(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')

def print_data(data):
    for date,players in data:
        print("\nDay:",date.day,"Hour:",date.hour,"Players:",players)

def visualize_player_count(data):
    # Load the data into a Pandas DataFrame
    csvreader = csv.reader(open(data))
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        row[0] = string_to_datetime(row[0])
        rows.append(row)
    print_data(rows)
    
    #sort into days
    days = {}
    numplayers_template = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    hours_template = [8,9,10,11,12,13,14,15,16,17,18,19,20]
    # fig = px.line(x=hours_template,y=numplayers_template)
    # fig.show()
    # fig2 = px.line(x=hours_template,y=numplayers_template)
    # fig2.show()

    for date,players in rows:
        hour = date.hour
        hourIndex = hour-8
        players = int(players)
        day = str(date.year)+"/"+str(date.month)+"/"+str(date.day)
        if day not in days:
            days[day] = numplayers_template.copy()
        if players>days[day][hourIndex]:days[day][hourIndex]=players
    
    print(days)
    for dayNum in days:
        fig = px.line(x=hours_template,y=days[dayNum],title="Minecraft Server, Player Activity on "+dayNum)
        #fig.
        fig.show()



    

# Example usage:
visualize_player_count('player_counts.csv')
