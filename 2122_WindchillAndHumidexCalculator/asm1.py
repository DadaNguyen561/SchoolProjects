# COMP 1026 â€“ Assignment 1

# Dada Nguyen

# Write a program using user input, loops, and conditionals to calculate the windchill or humidex.

import math

# Ask the user for the (air) temperature until an appropriate value is entered
user_wants_to_continue = True

# Start loop
while user_wants_to_continue:
    Tempt = float(input('Enter a temperature between -50 and 50: '))

    # Check the temperature
    while Tempt > 50 or Tempt < -50:
        print('That temperature is invalid.')
        Tempt = int(input('Enter a temperature between -50 and 50: '))

    # Calculate the windchill
    if Tempt <= 0:
        print('Calculating windchill.')

        # Check the windspeed
        windSpeed = float(input('Enter a wind speed between 1 and 99 km/h: '))
        while windSpeed < 1 or windSpeed > 99:
            print('That wind speed is invalid.')
            windSpeed = float(input('Enter a wind speed between 1 and 99 km/h: '))

        # Calculate valid windchill
        windchill = 13.12 + (0.6125 * Tempt) - (11.37 * (windSpeed ** 0.16)) + (0.3965 * Tempt * (windSpeed ** 0.16))
        windchill = round(windchill)

        # Categorize the windchill risk
        if windchill <= 0 and windchill >= -9:
            print('The windchill is {}. {}'.format(windchill, 'Low risk.'))
        elif windchill <= -10 and windchill >= -27:
            print('The windchill is {}. {}'.format(windchill, 'Moderate risk.'))
        elif windchill <= -28 and windchill >= -39:
            print('The windchill is {}. {}'.format(windchill, 'High Risk. Skin can freeze in 10-30 minutes.'))
        else:
            print('The windchill is {}. {}'.format(windchill, 'Very High Risk. Skin can freeze in under 10 minutes.'))

    # Calculate the humidex
    elif 50 > Tempt >= 20:
        print('Calculating humidex.')

        # Check the dewpoint
        dewPoint = float(input('Enter the dewpoint between -50 and 50: '))
        while dewPoint > Tempt or dewPoint > 50 or dewPoint < -50:
            print('That dew point is invalid.')
            dewPoint = float(input('Enter the dewpoint between -50 and 50: '))

        # Calculate valid dewpoint
        if dewPoint <= Tempt and dewPoint <= 50 or dewPoint >= -50:
            f2 = 6.11 * (math.exp(5417.7530 * (1/273.16 - 1/(273.16 + dewPoint))))
            f3 = 5/9 * (f2 - 10)
            humidex = f3 + Tempt
            humidex = round(humidex)

            # Categorize the humidex risk
            if humidex <= 29 and humidex >= 20:
                print('The humidex is {}. {}'.format(humidex, 'Little or no discomfort.'))
            elif humidex <= 39 and humidex >= 30:
                print('The humidex is {}. {}'.format(humidex, 'Some discomfort.'))
            elif humidex <= 44 and humidex >= 40:
                print('The humidex is {}. {}'.format(humidex, 'Great discomfort. Avoid exertion.'))
            else:
                print('The humidex is {}. {}'.format(humidex, 'Dangerous. Heat stroke possible.'))

    # Normal temperature
    elif Tempt > 0 and Tempt < 20:
        print('Windchill and humidex are not a factor at this temperature.')

    # Ask the user if they would like to continue with a Y/N question
    ask = input('Check another weather condition (Y/N)? ')
    ask = ask.lower()

    # Check the valid input
    while ask not in ['y', 'n']:
        print('That input is invalid.')
        ask = input('Check another weather condition (Y/N)? ').lower()
    if ask == 'y':
        continue
    elif ask == 'n':
        break