import matplotlib.pyplot as plt
import numpy as np

class BubblePlotGenerator:
    def __init__(self, simulation):
        # Get win_loss_df
        self.win_loss_df = simulation["win_loss"]

        # Extract timestamps for the X-axis
        self.timestamps = self.win_loss_df.index

        self.win_loss_percents_np = self.win_loss_df['win_loss_percents'].values
        self.portfolio_values_np = self.win_loss_df['portfolio_values'].values

    def generate_bubble_plot(self):
        # Separate winning and losing trades
        winning_trades = [perc > 0 for perc in self.win_loss_percents_np]
        losing_trades = [perc < 0 for perc in self.win_loss_percents_np]

        print("Total Trades:", len(self.win_loss_percents_np))
        print("Winning Trades:", sum(winning_trades))
        print("Losing Trades:", sum(losing_trades))

























        # # Create a scatter plot with green bubbles for winning trades and red for losing trades
        # plt.figure(figsize=(12, 6))
        # plt.scatter(
        #     self.timestamps,
        #     self.win_loss_percents_np,
        #     s=[abs(value) * 20000 for value in self.win_loss_percents_np],
        #     c=['g' if win else 'r' for win in winning_trades],
        #     edgecolor='black'
        # )
        #
        # plt.xlabel("Time Frame")
        # plt.ylabel("Profit/Loss")
        # plt.title("Bubble Plot of Winning and Losing Trade Profit/Loss")
        #
        # # Adjust plot size to fit the screen
        # plt.tight_layout()
        #
        # # Show the plot
        # plt.show()













################################## OLD CODE ###########################################
        # # Array of winning values
        # winning_values = [round(perc, 4) for perc, win in zip(self.win_loss_percents_np, winning_trades) if win]
        #
        # print("Winning Bubble Sizes:", winning_values)
        #
        # # Array of losing values
        # losing_values = [round(perc, 4) for perc, lose in zip(self.win_loss_percents_np, losing_trades) if lose]
        #
        # print("Losing Bubble Sizes:", losing_values)
        #
        # # Create Y positions (constant)
        # y_positions_winning = [1] * len(winning_values)
        # y_positions_losing = [1] * len(losing_values)
        #
        # # Create a scatter plot with green bubbles for winning trades
        # plt.figure(figsize=(12, 6))
        # plt.scatter(winning_values, y_positions_winning, s=[abs(value) * 20000 for value in winning_values], c='g'
        #             , edgecolor='black')
        # plt.scatter(losing_values, y_positions_losing, s=[abs(value) * 20000 for value in losing_values], c='r'
        #             , edgecolor='black')
        #
        # plt.xlabel("Profit/Loss")
        # plt.title("Bubble Plot of Winning and Losing Trade Profit/Loss")
        #
        # # Hide y-axis labels
        # plt.yticks([])
        #
        # # Adjust plot size to fit the screen
        # plt.tight_layout()
        #
        # # Show the plot
        # plt.show()