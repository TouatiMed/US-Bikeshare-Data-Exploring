# US-Bikeshare-Data-Exploring
Udacity Prefoessional Data Analyst Degree Project I

## Overview
In this project, I used Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. the code imports the data and answers interesting questions about it by computing descriptive statistics, By taking in raw input to create an interactive experience in the terminal to present these statistics.

## Requirements
- Python 3, NumPy, and pandas installed using Anaconda 
- A text editor, like Sublime or Atom
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows)

## Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year
![Data for the first 10 rides in the new_york_city.csv file](https://i.imgur.com/MBrFbzS.png)

## Answering Questions
I will answer the following questions about the bike share data:

### 1 Popular times of travel (i.e., occurs most often in the start time)
most common month
most common day of week
most common hour of day

### 2 Popular stations and trip
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

### 3 Trip duration
total travel time
average travel time

### 4 User info
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

## The Files
We have the three city dataset files:

- chicago.csv
- new_york_city.csv
- washington.csv

## The Interactive Experience
For an interactive experience,the script takes in raw inputs in the terminal to present the relevant statistics. Below the screenshots show some results after requesting information about New York City:

![screenshot](https://i.imgur.com/Oit97pN.png)

![screenshot](https://i.imgur.com/xvCULDV.png)

![screenshot](https://i.imgur.com/TUhw1FI.png)
