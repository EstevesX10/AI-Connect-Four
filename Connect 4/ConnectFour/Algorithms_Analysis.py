# This file contains functions used to properly evaluate how the algorithms performed within the Connect Four Game

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from time import (time)
import tracemalloc
from .Heuristics import (heuristic_suggested)

def Analyse_Algorithm_Time_Space(algorithm, *args, **kwargs):
    n_itr = 10
    # Initializing the measured time and space
    times = []
    spaces = []

    # Iterating n_itr times to generate reliable results
    for _ in range(n_itr):
        # Start tracing memory allocations
        tracemalloc.start()
    
        # Snapshot before the function call
        snapshot_before = tracemalloc.take_snapshot()
    
        # Saving the Initial Time
        start = time()
        # Executing the function
        node = algorithm(*args, **kwargs)
        end = time()
    
        # Snapshot after the function call
        snapshot_after = tracemalloc.take_snapshot()
    
        # Calculate the difference in memory usage
        stats = snapshot_after.compare_to(snapshot_before, 'lineno')
    
        # Calculating the memory used in KB
        total_memory_diff = sum(stat.size_diff for stat in stats)

        # Updating the time and space averages
        times.append((end - start))
        spaces.append(abs(total_memory_diff))
    
    return (node, times, spaces)

def Display_Results(df, X, Y, HUE, Title):
    # Setting theme for the Chart
    sns.set_theme(style='dark',rc={'axes.facecolor':'White', 'figure.facecolor':'White'})
    fig, ax1 = plt.subplots(figsize=(10,5))
    
    # Ploting the dataset    
    sns.scatterplot(data = df, x=X, y=Y, hue=HUE, marker='o')
    ax2 = ax1.twinx()
    
    # Adding a Title
    plt.title(Title)
    
    # Showing the Graph
    plt.show()

def Analyse_Game_State(node, Analysis_Title, Algorithms):
    Result_Nodes = []
    data = []

    # Applying all algorithms to a given game state
    for algo in Algorithms:
        new_node, times, spaces = Analyse_Algorithm_Time_Space(algo, node, heuristic_suggested)
        Result_Nodes.append(new_node)
        for i in range(len(times)):
            data.append([algo.__name__, times[i], spaces[i]])
    
    # Creating a Dataframe with the Results
    columns = ['Algorithm', 'Average Time (s)', 'Average Space (KB)']
    df = pd.DataFrame(data, columns=columns)

    # Displaying the Results with a Scatterplot
    Display_Results(df, 'Average Time (s)', 'Average Space (KB)', 'Algorithm', Analysis_Title)

    # Returning the Nodes obtained by each algorithm
    return Result_Nodes