from gpiozero import Buzzer, OutputDevice, Button
from time import sleep

class BistrobotBell:
    def __init__(self, buzzer_pin):
        self.buzzer = Buzzer(buzzer_pin)

    def buzz(self, duration=5):
        for i in range (0, duration):
            self.buzzer.on()
            sleep(0.01)
            self.buzzer.off()


class Bistrobot:
    def __init__(self, feeder_pin, sensor_pin):
        self.feeder = OutputDevice(feeder_pin)
        self.sensor = Button(sensor_pin)

    def get_sensor_status(self):
        return self.sensor.is_pressed

    def reset_rotation(self):
        if not self.sensor.is_pressed:
            self.feeder.on()
            while not self.sensor.is_pressed:
                pass
            while self.sensor.is_pressed:
                pass
            feeder.off()

    def trigger_portion(self):
        if not self.sensor.is_pressed:
            self.feeder.on()
            while not self.sensor.is_pressed:
                pass
            sleep(0.2)
            self.feeder.off()
        self.feeder.on()
        while self.sensor.is_pressed:
            pass
        sleep(0.2)
        self.feeder.off()

    def serve_meal(self, portions, wait_time=100):
        for i in range(0, portions):
            self.trigger_portion()
            if i < portions - 1:
                sleep(wait_time)
