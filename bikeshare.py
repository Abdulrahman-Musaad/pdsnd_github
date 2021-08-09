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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # This part gets the user input for city (chicago, new york city, washington).

    print('First step is to enter the name of the city to analyze. There are three cities: \n - chicago \n - new york city \n - washington')
    city = input ('Enter the name of the city  to analyze: ')
    # This part is to handle invalid inputs for city
    while city !='chicago' and city !='washington' and city !='new york city':
        print ('You selected {} which is not a city in our data or misspelled.'. format(city))
        city = input ("Please type with correct spelling as 'chicago', 'new york city' or 'washington': ")

    # This part gets the user input for month (all, january, february, ... , june)
    monthss = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    print ('Months in recoreds are:', ' '.join(monthss[0:-1]) )
    month = input ('Enter the name of the month to filter by, or "all" to apply no month filte: ')
    # This part is to handle invalid inputs for month
    while month not in monthss:
        print('It looks like you entered a month that is not in the record or you misspelled it')
        print ('months in recoreds are:', ' '.join(monthss[0:-1]))
        month = input ('type name of the month to filte by or or "all" to apply no month filter: ')

    # This part gets the user input for day of week (all, monday, tuesday, ... sunday)
    days_names = ['monday' , 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input ('name of the day of week to filter by, or "all" to apply no day filter: ')
    # This part is to handle invalid inputs for day
    while day not in days_names:
        #print('you typed an invalid day name as : {}.'. format(day))
        print('name of the day of week to filter by as', ' '.join(days_names[0:-1]))
        day = input ('name of the day of week to filter by, or "all" to apply no day filter: ')


    print('-'*40)
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
    df= pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month!= 'all':
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

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    if month == 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month = df['month'].mode()[0]

        print ('The most common month is: {}'. format(months[popular_month-1]))
    else:
        print ( 'If you choosed to apply no filter by month you can see The most common month')


    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print ('The most common day is: {}'. format(popular_day))
    else:
        print ( 'If you choosed to apply no filter by day you can see The most common day')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print ('The most common hour is: {}'. format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print (' The most commonly used start station is: {}'. format (popular_start_station))
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print (' The most commonly used end station is: {}'. format (popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination of stations']='Starts from: '+df['Start Station']+ ' and ends at: ' + df['End Station']
    popular_combination_stations=df['combination of stations'].mode()[0]

    print (' The most frequent combination of start and end station trip: \n {}'. format (popular_combination_stations))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_time_sec= sum ( df['Trip Duration'])
    tot_time_hrs= int(tot_time_sec // (60*60))
    tot_time_min= int((tot_time_sec % (60*60)) // 60)
    tot_time_rem_sec=int(((tot_time_sec % (60*60))% 60) )

    print ('total travel time is: {} hours, {} minutes and {} seconds'. format(tot_time_hrs,tot_time_min,tot_time_rem_sec))

    # TO DO: display mean travel time
    average_travel_time= df['Trip Duration'].mean()
    average_in_min=average_travel_time//60
    average_in_sec=average_travel_time % 60
    print ('the average travel time is: {} minutes and {} seconds'. format(average_in_min,average_in_sec))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('The counts of user types are as follow:')
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types)


    # TO DO: Display counts of gender
    print ('The counts of user gender are as follow:')
    user_gender = df.groupby(['Gender'])['Gender'].count()
    print(user_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year=df['Birth Year'].min()
    recent_birth_year=df['Birth Year'].max()
    common_birth_year=df['Birth Year'].mode()[0]

    print ('The earliest year of birth is: {}'. format(earliest_birth_year))
    print ('The most recent year of birth is: {}'. format(recent_birth_year))
    print ('The most common year of birth is: {}'. format(common_birth_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        while restart.lower() !='yes' and restart.lower() !='yes':
            print ('This is invalid input')
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
