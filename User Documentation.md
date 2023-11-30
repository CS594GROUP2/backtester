**FastTrader Documentation**

**Introduction:**

Welcome to FastTrader, Your Gateway to Innovative Financial Analysis

In the dynamic world of quantitative financial analysis, FastTrader
stands out as a pioneering tool designed to empower you, the user. At
the heart of FastTrader is our commitment to transparency and
user-driven functionality. Unlike many other platforms, we provide
complete visibility into the inner workings of our system, allowing you
to not just utilize but also understand every aspect of your trading
strategies.

What truly sets FastTrader apart is our dedication to democratizing
financial decision-making. Our open-source approach ensures that
everyone, from individual investors to professional analysts, has equal
access to sophisticated tools, fostering a community where knowledge and
resources are shared openly.

But that\'s not all. Speed is critical in financial analysis, and
FastTrader excels here too. Leveraging the power of Numba, an advanced
performance compiler, FastTrader accelerates numerous functions. This
technological edge means you can test potentially thousands of trading
strategies in real-time, giving you a significant advantage in today\'s
fast-paced market.

Join us on this journey to reshape financial analysis. With FastTrader,
your strategies are limited only by your imagination.

**Disclaimer:**

None of the Research derived from this software constitutes financial
advice. The contributors of this software shall not be held liable for
its accuracy or the outcome of any decisions derived by the research
produced from it.

Installation:

System requirements:

Python 3.8 interpreter on Mac OS x, Windows 10 or higher, or Linux

Internet connection

Multiple-core CPU (recommended)

\
We Recommend using jupyter notebooks/labs as your IDE
[*https://jupyter.org/install*](https://jupyter.org/install)

Once in the IDE of your choice create a new virtual environment
[*https://www.geeksforgeeks.org/using-jupyter-notebook-in-virtual-environment/*](https://www.geeksforgeeks.org/using-jupyter-notebook-in-virtual-environment/)

Then you just need to run

Pip install fasttrader

\
All of the necessary dependencies will be installed

Getting started:

To get started with FastTrader follow the steps laid out in installation
to get it installed on your machine.

After you have followed the installation steps familiarize yourself with
the Pandas and NumPy libraries. Almost all of the data we use will be
stored in these data structures.

You can't Backtest any strategies if you don't have any historical data
so typical that is what you will want to start with. Fastraders Data
class can help query data from the yahoo finance api

**Getting Data:**

To fetch data from the api ensure you are connected to the internet and
construct the parameters for your query and call the function
get_price_data() it takes four arguments\
\
Start -\> Pandas.Timestamp (the starting date/time of the data you would
like to query)\
End -\> Pandas.TImestamp (the ending date/time of the data you would
like to query)\
interval-\> Pandas.Timedelta (the time aggregation for the time series
data you are querying)

Ticker -\> String (the ticker symbol of the asset you wish to query

Ex.

Import fasttrader as ft

Import pandas as pd

#fetch some historical price data

Data_grabber = Data()

start = pd.Timestamp(\'2020-01-01\')

end = pd.Timestamp(\'2021-01-01\')

interval = pd.Timedelta(\'1d\')

ticker = \'AAPL\'

data = data_grabber.get_price_data(start, end, interval, ticker)

The function returns a pandas DataFrame. Dataframes are multi-columnar
data structures where columns can be indexed by keys and each column
requires homogeneity, all columns have the same index as well and for
time series data these are time stamps. If you want to see all the
columns you have access to you can simply call data.head() to see them.
If you extract a single column from the dataframe by key it becomes a
pandas series which is a single columnar data structure sharing the same
index as the DataFrame it was extracted from. The user is required to
maintain the index of the dataframe as we will store information later
in NumPy arrays which will cause a loss of information in the indices
they were derived from.

If the yahoo finance api is not working or you don't have a connection
to the internet you can download a CSV from
[*https://finance.yahoo.com/*](https://finance.yahoo.com/) and then
extract the same DataFrame using Pandas.read_csv()

**Generating a Technical Indicator: **\
\
Technical indicators are crucial in driving many quantitative trading
strategies. With FastTrader, leveraging these indicators is streamlined,
thanks to seamless integration with Pandas. Here\'s how you can generate
technical indicators using pandas_ta:

\
import pandas_ta as pta

\# To find out the arguments for a specific indicator:

help(pta.indicator_name)

\# Generating an indicator:

indicator_values = pta.indicator_name(\*\*args)

Note: If you plan on simulating multiple strategies then make sure you
save your indicator parameters as a list or NumPy array as you will need
them later if you intend to visualize if the indicator takes multiple
parameters save them as a array of tuples

**Generating Trading Signals:**

FastTrader offers versatile methods for generating trading signals, but
we encourage you to think beyond the provided tools. The possibilities
are endless: from using NLP to analyze news reports for sentiment-based
trading signals to crafting complex algorithms that rely on multiple
conditions. Remember, the trading signals follow a simple convention: +1
for position entry, -1 for exiting a position, and 0 for no trade.
Adhering to this convention allows you to formulate your strategies in
any way you see fit.

**SignalGenerator Object:**

The core of your strategy lies within the SignalGenerator object, which
encapsulates all necessary data for simulation.

Constructor: The constructor takes a pandas.Series (typically the
"Close" column from your historical data) and stores it in
self.price_data.

Note: In our terminology, hist_data refers to a full DataFrame of
historical asset data, while price_data denotes a single column
representing an asset\'s price over time.

**Methods for Signal Generation:**

generate_above_below(technical_indicator, metadata): Generates signals
based on the asset price crossing a given technical indicator or another
value. Signals are positive when crossing above and negative when
crossing below.

generate_crossover(self, crossover_data1, crossover_data2, metadata={}):
This more generalized method allows for creating signals based on the
crossover of two data sets, which could be two different technical
indicators, or one technical indicator and the price data.

generate_random(size, entry_probability, exit_probability): A method
useful for benchmarking, which surprisingly often outperforms many
example strategies. It generates random trading signals based on the
specified probabilities for entry and exit.

**Simulation with FastTrader:**

FastTrader simplifies the simulation process, allowing you to test your
trading strategies effectively. You can use the strategy instance
created earlier and add any additional metadata (like indicator_param)
to aid in visualization and analysis. Here\'s how you can set up and run
a simulation:

**Steps to Run a Simulation:**

Setting the Risk-Free Rate:

The risk-free rate is necessary for generating the sharpe ratio. You can
obtain it using ft.get_risk_free_rate().

If the Yahoo Finance API is unavailable, you can manually look up the
current rate of the 10-year US Treasury yield and input it directly.

1.  Create a new Simulator

Simulator = Simulator(strategy_instance, risk_free_rate)

1.  Run The Simulation

simulator.simulate()

1.  Accessing Simulation Results:

The results of the simulation are stored in dictionaries for easy access
and analysis.

To view individual elements of the results, refer to the Simulator
constructor or use the simulator.get_results() method. This returns a
dictionary containing:

Nested DataFrames with:

> win_loss_np

> win_loss_percents_np

> portfolio_values_np

> Input data used for the simulation:

> trading_signals_np

> price_data_np

Metadata passed in:

metadata

Performance metrics:

> max_drawdown

> ratio_winning_trades

> sharpe_ratio

> expectancy

> Variance

For multiple simulation one can construct many signal_generator objects
that fully encapsulate their trading strategies, store them in a NumPy
array and pass them to

\
simulate_all( many_strategies, index )

Many_strategies - the numpy array of signal_generator objects\
Index - the index of the parameter varied among the strategies pass as a

pd.Index (for 1-Dimensional input spaces) and as a pd.MultiIndex (for
higher dimensional input spaces).

The output will be in the form of a pd.Series with the only column being
the desired statistic over every possible strategy instance you pass in.
the index is passed through and will be attached as well. if you have a
mulit-core machine don't be afraid to crank up the strategy instances as
this operation is well-parallelized and Numba accelerated 💪

**Visualization: **

Once you have simulated a strategy or multiple strategies rather than
looking at a bunch of numbers in a terminal or on a spreadsheet it is
best to visualize that information. If you want to just look at asset
information we have integrated with matplotlib and you can reference
their documentation to see how to make a bar or line chart with your
hist_data.

We wrapped matplotlib for some of our outputs to streamline the process.
You can take the output of a single simulation and visualize it with

visualize \_strategy(self, price_data, trading_signals,
win_loss_percents, portfolio_values)\
\
All of these parameter can be found as members of your simulator object
after running a simulation. The output will be a line plot of portfolio
values overlaid on the price data and showing the positive and negative
trading signals.

You may also want to generate a bubble plot of the win_loss_percents and
you can use

generate_bubble_plot(simulator)

With this function you simply pass the entire simulator and a plot will
be generated.

If you wish to visualize multiple strategies this can be accomplished
with matplotlib for 1 dimensional input spaces a simple line plot can be
created from the output of simulate_all. For 2 dimensional input spaces
a heat map can be created just be sure to use a pd.MultiIndex in the
series you use to create the plot.

**Terminology:**\

Trading Signals: Indicators or suggestions generated by a system, based
on technical analysis or other criteria, signaling when it might be a
good time to buy or sell a particular asset.

Sentiment Analysis: A technique used in NLP to identify and categorize
opinions expressed in text, especially to determine whether the
writer\'s attitude towards a particular topic is positive, negative, or
neutral.

Crossover Value: A point on a chart where two different data sets (such
as a security\'s price and a technical indicator) intersect, which
traders often use to make buy or sell decisions.

Technical Indicator: A mathematical calculation based on historical
price, volume, or open interest information that aims to forecast
financial market direction. Common examples include moving averages, RSI
(Relative Strength Index), and MACD (Moving Average Convergence
Divergence).

Metadata: Data that provides information about other data. In
FastTrader, this could refer to additional details related to trading
signals, such as the parameters used in their generation.

Backtesting: The process of testing a trading strategy on historical
data to see how it would have performed.

Risk-Free Rate: A theoretical return on an investment with zero risk of
financial loss. Often, the yield on U.S. Treasury securities is used as
a proxy for this rate.
