import sys
import argparse
from time import sleep

from . import Bistrobot, BistrobotBell

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpio_buzzer', type=int, help='GPIO pin number for the Buzzer')
    parser.add_argument('--gpio_sensor', type=int, help='GPIO pin number for the Sensor')
    parser.add_argument('--gpio_feeder', type=int, help='GPIO pin number for the Feeder')
    parser.add_argument('-m', '--meal', action='store_true', help='Serve a meal')
    parser.add_argument('-p', '--portions', type=int, default=1, help='Number of portions to server for this meal')
    parser.add_argument('-d', '--delay', type=int, default=100, help='Number of seconds to pause for between each portion')
    parser.add_argument('-s', '--sleep', type=int, default=5, help='Number of seconds to pause for after buzzing the bell')
    args = parser.parse_args()

    if args.gpio_buzzer is not None:
        bell = BistrobotBell(args.gpio_buzzer)
        bell.buzz()
        sleep(args.sleep)

    if args.meal and args.gpio_sensor is not None and args.gpio_feeder is not None:
        garcon = Bistrobot(args.gpio_feeder, args.gpio_sensor)
        portions = args.portions
        if portions < 1:
            print("The number of portions must be >= 1")
            parser.print_help()
            return 1
        garcon.serve_meal(portions, args.delay)

if __name__ == "__main__":
    sys.exit(main())
