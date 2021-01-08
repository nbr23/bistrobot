import sys
import argparse

from . import Bistrobot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpio_buzzer', type=int, help='GPIO pin number for the Buzzer')
    parser.add_argument('--gpio_sensor', required=True, type=int, help='GPIO pin number for the Sensor')
    parser.add_argument('--gpio_feeder', required=True, type=int, help='GPIO pin number for the Feeder')
    parser.add_argument('-m', '--meal', action='store_true', help='Serve a meal')
    parser.add_argument('-p', '--portions', type=int, default=1, help='Number of portions to server for this meal')
    parser.add_argument('-d', '--delay', type=int, default=100, help='Number of seconds to pause for between each portion')
    args = parser.parse_args()

    if args.meal:
        gpio_buzzer = int(args.gpio_buzzer) if args.gpio_buzzer else None
        gpio_feeder = int(args.gpio_feeder)
        gpio_sensor = int(args.gpio_sensor)
        garcon = Bistrobot(gpio_feeder, gpio_sensor)
        portions = args.portions
        if portions < 1:
            print("The number of portions must be >= 1")
            parser.print_help()
            return 1
        garcon.serve_meal(portions, args.delay)

if __name__ == "__main__":
    sys.exit(main())
