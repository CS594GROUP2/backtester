from setuptools import setup, find_packages

# Setting up
setup(
    name='fasttrader',
    version='0.3.0',
    author='CS594GROUP2',
    author_email='<johnpiapian@gmail.com>',
    description='Welcome to FastTrader, Your Gateway to Innovative Financial Analysis!',
    url='https://github.com/CS594GROUP2/backtester',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=open('DESCRIPTION.md').read(),
    packages=find_packages(),
    install_requires=['yfinance', 'pandas', 'pandas_ta', 'numpy', 'numba', 'matplotlib'],
    keywords=['python', 'yfinance', 'trading', 'backtesting', 'stock market', 'trading strategies'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Financial and Insurance Industry',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)