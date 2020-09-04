import sys
import argparse

from . import Bistrobot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpio_buzzer', required=True, type=int, help='GPIO pin number for the Buzzer')
    parser.add_argument('--gpio_sensor', required=True, type=int, help='GPIO pin number for the Sensor')
    parser.add_argument('--gpio_feeder', required=True, type=int, help='GPIO pin number for the Feeder')
    parser.add_argument('-m', '--meal', action='store_true', help='Serve a meal')
    parser.add_argument('-p', '--portions', type=int, default=1, help='Number of portions to server for this meal')
    args = parser.parse_args()

    if args.meal:
        gpio_buzzer, gpio_feeder, gpio_sensor = None, None, None
        gpio_buzzer = int(args.gpio_buzzer)
        gpio_feeder = int(args.gpio_feeder)
        gpio_sensor = int(args.gpio_sensor)
        garcon = Bistrobot(gpio_feeder, gpio_sensor, gpio_buzzer)
        portions = args.portions
        if portions < 1:
            print("The number of portions must be >= 1")
            parser.print_help()
            return 1
        garcon.serve_meal(portions)

if __name__ == "__main__":
    sys.exit(main())
