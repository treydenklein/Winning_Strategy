# Import libraries
import pandas as pd
import numpy as np

# Number of iterations to simulate
num_iterations = 10000

# Create a list to store the results
results = []

# Simulation loop
num_wins = 0
for iteration in range(1, num_iterations + 1):
    # Randomly choose a door for the prize
    prize_door = np.random.randint(1, 4)

    # Contestant's initial choice
    initial_choice = np.random.randint(1, 4)

    # Determine if the contestant wins by sticking with their initial choice
    win = initial_choice == prize_door

    # Increment the number of wins if the contestant wins
    if win:
        num_wins += 1

    # Calculate the proportion of wins
    proportion_of_wins = num_wins / iteration

    # Store the result in the list
    results.append(
        {"iteration": iteration, "win": win, "proportion_of_wins": proportion_of_wins}
    )

# Convert the list of results to a DataFrame
df = pd.DataFrame(results)

# Write dataframe to CSV file
df.to_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Winning_Strategy\csv_files\stay_strategy_data.csv",
    index=False,
)
