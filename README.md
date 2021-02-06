# bistrobot

Simple controller for Raspberry Pi Zero GPIO equipped cat feeding robot.

A companion ansible collection is available at [bistrobot-ansible](https://github.com/nbr23/bistrobot-ansible)

## Installation

This python module relies on `>=python3.5`.

You can install the module and its dependencies using `pip install git+https://github.com/nbr23/bistrobot.git` to install from github, or `pip install .` from your project directory to install your local version.


## Usage

Use `bistrobot -h` to view the following bistrobot help:

```
usage: bistrobot [-h] [--gpio_buzzer GPIO_BUZZER] [--gpio_sensor GPIO_SENSOR] [--gpio_feeder GPIO_FEEDER] [-m] [-p PORTIONS] [-d DELAY] [-s SLEEP]

optional arguments:
  -h, --help            show this help message and exit
  --gpio_buzzer GPIO_BUZZER
                        GPIO pin number for the Buzzer
  --gpio_sensor GPIO_SENSOR
                        GPIO pin number for the Sensor
  --gpio_feeder GPIO_FEEDER
                        GPIO pin number for the Feeder
  -m, --meal            Serve a meal
  -p PORTIONS, --portions PORTIONS
                        Number of portions to server for this meal
  -d DELAY, --delay DELAY
                        Number of seconds to pause for between each portion
  -s SLEEP, --sleep SLEEP
                        Number of seconds to pause for after buzzing the bell
```

Some popular usage examples can be found below.

### Serve a 1 portion meal, 5 seconds after buzzing the meal bell

`bistrobot --gpio_buzzer $GPIO_BUZZER --gpio_sensor $GPIO_SENSOR --gpio_feeder $GPIO_FEEDER -p 1 -s 5`


### Serve a 2 portions meal, with a 30 second pause between each portion. No meal bell buzzing.

`bistrobot -gpio_sensor $GPIO_SENSOR --gpio_feeder $GPIO_FEEDER -p 2 -d 30`

### Serve a 3 portions meal, all 3 portions at once.

`bistrobot -gpio_sensor $GPIO_SENSOR --gpio_feeder $GPIO_FEEDER -p 3 -d 0`

