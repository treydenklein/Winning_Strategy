# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  # Import ticker module

# Read CSV files into DataFrames
swap_strategy_df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Winning_Strategy\csv_files\swap_strategy_data.csv"
)
stay_strategy_df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Winning_Strategy\csv_files\stay_strategy_data.csv"
)

# Extract iteration and win percentage values from swap strategy data
swap_iterations = swap_strategy_df["iteration"]
swap_win_percentages = round(swap_strategy_df["proportion_of_wins"] * 100, 3)

# Extract iteration and win percentage values from stay strategy data
stay_iterations = stay_strategy_df["iteration"]
stay_win_percentages = round(stay_strategy_df["proportion_of_wins"] * 100, 3)

# Create plot
plt.style.use("dark_background")  # Set plot style to dark mode
plt.figure(figsize=(10, 6))
plt.ylim(0, 100)  # Set y-axis range

# Plot data
plt.plot(
    swap_iterations,
    swap_win_percentages,
    color="skyblue",
    label="Strategy: Accept Offer to Swap Doors",
)

plt.plot(
    stay_iterations,
    stay_win_percentages,
    color="salmon",
    label="Strategy: Stay with Original Choice",
)

# Add horizontal lines representing the theoretical win probabilities
plt.axhline(y=66.667, color="gray", linestyle="--")
plt.axhline(y=33.333, color="gray", linestyle="--")

# Add text labels for plot lines
plt.text(
    x=8750,  # x-position
    y=68.5,  # y-position
    s="Theoretical Win Probability (66.667%)",  # Text to display
    color="gray",
    ha="center",
    fontsize=9,
)

plt.text(
    x=8750,  # x-position
    y=29,  # y-position
    s="Theoretical Win Probability (33.333%)",  # Text to display
    color="gray",
    ha="center",
    fontsize=9,
)

# Add plot titles and labels
plt.title("Win Probability by Strategy")
plt.xlabel("Number of Simulations")
plt.ylabel("Percentage of Wins")
plt.legend(fontsize=10)

# Set a formatter to include '%' in y-axis ticks
percent_formatter = ticker.FuncFormatter(lambda x, _: f"{x:.0f}%")
plt.gca().yaxis.set_major_formatter(percent_formatter)

# Show the plot
plt.show()
