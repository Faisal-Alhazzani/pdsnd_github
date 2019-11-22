import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = str(input("Please choose a city: (chicago, new york city, or washington) "))
            city = city.lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                    print("Sorry, please enter a valid input (chicago, new york city, or washington) ")
                    continue
        except ValueError:
            print("Sorry, please enter a valid input (chicago, new york city, or washington) ")
            continue


    while True:
        try:
            filt = str(input("Would you like to filter by month, day, both or not at all? Type 'none' for no time                                     filter. "))
            filt = filt.lower()
            if filt in ['month', 'day', 'both', 'none']:
                break
            else:
                print("Sorry, invalid input!")
                continue

        except ValueError:
            print("Sorry, invalid input!")
            continue

    if filt == 'none':
                month = 'all'
                day = 'all'
                return city, month, day

    if filt in ['month', 'both']:
    # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            try:
                month = str(input("Please enter a month: (all, january, february, ... , june) "))
                month = month.lower()
                if month in ['all','january','february','March','april','may','june','july','august',
                              'september','october','november','december']:
                    break

                else:
                    print("Sorry, invalid input!")
                    continue

            except ValueError:
                print("Sorry, please enter a valid input ")

                continue
    if filt in ['day', 'both']:
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            try:
                day = str(input("Please enter a day: (all, monday, tuesday, ...sunday) "))
                day = day.lower()
                if day in ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
                    break
                else:
                    print("Sorry, please enter a valid input ")
                    continue
            except ValueError:
                print("Sorry, please enter a valid input ")
                continue

    if filt == 'month':
        day = 'all'
    if filt == 'day':
        month = 'all'


    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].value_counts().idxmax()
    print('Most Frequent Start month: { }'.format(popular_month))

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].value_counts().idxmax()
    print('Most Frequent Start day: { }'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Frequent Start Hour: { }'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_st_station = df['Start Station'].value_counts().idxmax()
    print('Most common Start station: { }'.format(popular_st_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most common End station:'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    counts = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print("Most frequent combined stations { }".format(counts.index[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel= df['Trip Duration'].sum()
    print('Total travel time: ', tot_travel)

    # TO DO: display mean travel time
    mean_travel= df['Trip Duration'].mean()
    print('Average travel time: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    df.name = city
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user = df['User Type'].value_counts()
    print('counts of user types: ', counts_user)
    # TO DO: Display counts of gender

    if df.name != 'washington':
        counts_gender = df['Gender'].value_counts()
        print('counts of user types: ', counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        recent_year = df['Birth Year'].min()
        print('Earliest year of birth', recent_year)


        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    while True:
        try:
            rows = 5
            user_input = str(input("do you want to see raw data? "))
            user_input = user_input.lower()
            if user_input =='yes' :
                print(df.iloc[:rows])
                while True:
                    try:
                         second_user_input = str(input("do you want to see more 5 lines of raw data?"))
                         second_user_input = second_user_input.lower()
                         if second_user_input =='yes':
                                rows += 5
                                print(df.iloc[:rows])
                                continue
                         elif second_user_input =='no':
                            return
                         else:
                            print("Sorry, invalid input! ")
                            continue

                    except ValueError:
                        print("Sorry, invalid input! ")
                        continue
            elif user_input =='no':
                break
            else:
                print("Sorry, invalid input! ")
                continue

        except ValueError:
            print("Sorry, invalid input! ")
            continue



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you, see you later!')
            break


if __name__ == "__main__":
	main()
