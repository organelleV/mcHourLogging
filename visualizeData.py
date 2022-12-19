import matplotlib.pyplot as plt
import pandas as pd

def visualize_player_count_line_chart(data):
    # Load the data into a Pandas DataFrame
    df = pd.read_csv(data)

    # Convert the timestamp column to a datetime index
    df.index = pd.to_datetime(df['timestamp'])

    # Format the datetime index as "YYYY-MM-DD HR:MIN"
    df.index = df.index.strftime('%m-%d %H:%M')

    # Plot the player count data as a line chart
    plt.plot(df['player_count'])
    plt.xlabel('Time')
    plt.ylabel('Number of Players')
    plt.title('Player Count Over Time')
    plt.show()

def visualize_player_count_bar_chart(data):
    # Load the data into a Pandas DataFrame
    df = pd.read_csv(data)

    # Convert the timestamp column to a datetime index
    df.index = pd.to_datetime(df['timestamp'])

    # Group the data by day and take the maximum player count
    df_by_day = df.resample('D').max()

    # Filter out days with no players
    df_by_day = df_by_day[df_by_day['player_count'] > 0]

    # Keep only the last 7 days of data
    df_by_day = df_by_day.tail(7)

    # Format the datetime index as "YYYY-MM-DD"
    df_by_day.index = df_by_day.index.strftime('%Y-%m-%d')

    # Plot the player count data as a bar chart
    plt.bar(df_by_day.index, df_by_day['player_count'])
    plt.xlabel('Time')
    plt.ylabel('Number of Players')
    plt.title('Maximum Player Count by Day (Last 7 Days)')
    plt.show()

def visualize_player_count_hour_bar_chart(data):
    # Load the data into a Pandas DataFrame
    df = pd.read_csv(data)

    # Convert the timestamp column to a datetime index
    df.index = pd.to_datetime(df['timestamp'])

    # Group the data by hour and take the mean
    df_by_hour = df.resample('H').mean()

    # Filter out hours with no players
    df_by_hour = df_by_hour[df_by_hour['player_count'] > 0]

    # Keep only the last 7 days of data
    df_by_hour = df_by_hour.tail(168)

    # Format the datetime index as "YYYY-MM-DD HR"
    df_by_hour.index = df_by_hour.index.strftime('%Y-%m-%d %H')

    # Plot the player count data as a bar chart
    plt.bar(df_by_hour.index, df_by_hour['player_count'])
    plt.xlabel('Time')
    plt.ylabel('Number of Players')
    plt.title('Player Count by Hour (Last 7 Days)')
    plt.show()




visualize_player_count_hour_bar_chart('player_counts.csv')

