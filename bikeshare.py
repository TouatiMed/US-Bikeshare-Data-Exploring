import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # user may type NYC instead of New York City so let's provide a dictionary
    city_dict = {"chicago": ["chicago"], "new york city": ["new york city", "nyc"], "washington": ["washington"]}

    while True:
        city_input = input("Please specify which city you like to see data for (chicago, new york city, washington):\n")
        cities_list = [item for sublist in list(city_dict.values()) for item in sublist]
        if city_input.lower() in cities_list:
            city = [key for key, value in city_dict.items() if city_input.lower() in list(value)][0]
            print("You chose {}!".format(city.title()))

            break
        else:
            print("You entered an invalid city! Please try again.")

    # get user input for month (all, january, february, ... , june)
    # user can either type the name of the month, number of the month or just an abbreviation like "Feb" so let's provie a dictionary
    month_dict = {"january": ["january", "jan", "1"],
                  "february": ["february", "feb", "2"],
                  "march": ["march", "mar", "3"],
                  "april": ["april", "apr", "4"],
                  "may": ["may", "may", "5"],
                  "june": ["june", "jun", "6"],
                  "july": ["july", "jul", "7"],
                  "august": ["august", "aug", "8"],
                  "september": ["september", "sep", "9"],
                  "october": ["october", "oct", "10"],
                  "november": ["november", "nov", "11"],
                  "december": ["december", "dec", "12"]}
    available_months_lit = ['january', 'february', 'march', 'april', 'may', 'june']

    # we can write a while loop until we get a valid input from the user
    while True:
        month_input = input("If you want to filter by month, please type the desired month (January, February, March, April, May or June) \nOr type \"none\" if else.\n")
        month_list = [item for sublist in list(month_dict.values()) for item in sublist]
        if month_input.lower() == "none":
            print("We will not filter by month then.")
            month = "none"
            break
        elif month_input.lower() in month_list:
            month = [key for key, value in month_dict.items() if month_input.lower() in list(value)][0]
            if month in available_months_lit:
                print("You chose {}!".format(month.title()))

                break
            else: #user might enter a valid month that we don't have the data for
                print( "looks like we don't have the data for {}! Please choose from January, February, March, April, May or June".format(month.title()))
                print("Let's try again...")

        else:
            print("You entered an invalid month.")
            print("Let's try again...")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    # user can either type the name of the day, number of the day (Monday is 1) or just an abbreviation like "Mon" so let's provie a dictionary

    day_dict = {"monday": ["monday", "mon", "1"],
                "tuesday": ["tuesday", "tue", "2"],
                "wednesday": ["wednesday", "wed", "3"],
                "thursday": ["thursday", "thu", "4"],
                "friday": ["friday", "fri", "5"],
                "saturday": ["saturday", "sat", "6"],
                "sunday": ["sunday", "sun", "7"]}

    while True:
        day_input = input("If you want to filter by day, please type the desired day (Example: \"Monday\",\"Mon\" or \"1\" for monday) \nOr type \"all\" if you don't want a specific.\n")
        day_list = [item for sublist in list(day_dict.values()) for item in sublist]
        if day_input.lower() == "all":
            day = "all"
            print("We will not filter by any specific day then.")
            break
        elif day_input.lower() in day_list:
            day = [key for key, value in day_dict.items() if day_input.lower() in list(value)][0]
            print("You chose {}!".format(day.title()))

            break
        else:
            print("You entered an invalid day.")

    print('-' * 100)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'none':
#         # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_index]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    if month != 'none' and day != 'all':
        print("Let's calculate some statistics for {} during the month of {} every {}.".format(city.title(),month.title(),day.title()))
    elif month == 'none' and day != 'all':
        print("Let's calculate some statistics for {} for every {}".format(city.title(),day.title()))
    elif month != 'none' and day == 'all':
        print("Let's calculate some statistics for {} during the month of {}.".format(city.title(),month.title()))
    else:
        print("Let's calculate some statistics for {}.".format(city.title()))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month )


    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: {}, with the count of: {}.'.format( popular_start_station,df['Start Station'].value_counts()[0]) )


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: {}, with the count of: {}.'.format(popular_end_station,df['End Station'].value_counts()[0])  )


    # display most frequent combination of start station and end station trip
    frequent_combinations = df.groupby(["Start Station", "End Station"]).size().sort_values(ascending=False)
    most_frequent = frequent_combinations.idxmax()
    print("The most frequent trip is from \"{}\" to \"{}\" with {} trips in total!".format(most_frequent[0],most_frequent[1],frequent_combinations[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df["Travel Time"] = df['End Time'] - df['Start Time']
    # display total travel time
    print("The total travel time is {}".format(df["Travel Time"].sum()))

    # display mean travel time
    print("The average travel time is {}".format(df["Travel Time"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types: \n{}".format(user_types.to_string()))

    # Display counts of gender if we have data for it
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\nCounts of Genders: \n{}".format(gender_count.to_string()))
    else:
        print("\nlooks like there is no gender data for {}!".format(city.title()))


    # Display earliest, most recent, and most common year of birth if we have data for it
    if 'Birth Year' in df.columns:
        earliest_BY = df['Birth Year'].min()
        recent_BY = df['Birth Year'].max()
        common_BY = df['Birth Year'].mode()[0]
        print("\nThe oldest Birth Year: {}".format(int(earliest_BY)))
        print("The Youngest Birth Year: {}".format(int(recent_BY)))
        print("Most Common Birth Year: {}".format(int(common_BY)))
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print("\nlooks like there is no birth year data for {}!".format(city.title()))


    print('-'*100)

def display_raw_data(df):

    user_input = input("Would you like to see 5 lines of raw data? (Answer with \"yes\" or \"no\") \n")
    possible_answers = ['yes', "y","no","n"]
    #if user_input.lower() in possible_answers:
    if user_input.lower() == "yes" or user_input.lower() == "y":
            n=5
            print("showing the first 5 lines of raw data with the specified filters applied above.")
            print(df.iloc[n-5:n, :])
            while True:
                user_second_input = input("Would you like to see the next 5 lines of raw data? (Answer with \"yes\" or \"no\") \n")
                if user_second_input.lower() == "no" or user_second_input.lower() == "n":
                    break
                elif user_second_input.lower() == "yes" or user_second_input.lower() == "y":
                    n+= 5
                    print("showing the next 5 lines of raw data with the specified filters applied above.")
                    print(df.iloc[n - 5:n, :])
                else:
                    print("Sorry, looks like \"{}\" is not a valid answer".format(str(user_second_input)))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
