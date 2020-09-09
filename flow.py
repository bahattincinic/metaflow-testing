import logging
import os
import sys

if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())

from metaflow import FlowSpec, step

from data import CARS


class ExampleFlow(FlowSpec):

    @step
    def start(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info('Flow started')

        self.next(self.load_cars)

    @step
    def load_cars(self):
        self.cars = CARS
        self.next(self.calculate_car, foreach='cars')

    @step
    def calculate_car(self):
        self.calculated_value = len(self.input['name'])

        self.next(self.merge_car_data)

    @step
    def merge_car_data(self, inputs):
        self.calculated_values = [
            input.calculated_value
            for input in inputs
        ]
        self.merge_artifacts(inputs, exclude=['calculated_value'])
        self.next(self.end)

    @step
    def end(self):
        self.logger.info('Car calculation is finished')


if __name__ == '__main__':
    ExampleFlow()
