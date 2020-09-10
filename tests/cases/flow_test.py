from data import CARS

from .base import BaseTestCase


class FlowTestCases(BaseTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.flow_run = cls.run_flow(name='flow.ExampleFlow')

    def test_successful_run_flow(self):
        """ Check successful & finished run """
        self.assertTrue(self.flow_run.successful)
        self.assertTrue(self.flow_run.finished)

    def test_load_cars(self):
        step_load_cars = self.get_step(self.flow_run, 'load_cars')

        self.assertEqual(len(CARS),
                         len(step_load_cars.task.data.cars))

    def test_calculate_car(self):
        step_calculate_car = self.get_step(self.flow_run, 'calculate_car')

        self.assertEqual(len(list(step_calculate_car.tasks())),
                         len(CARS))

    def test_merge_car_data(self):
        step_merge_car_data = self.get_step(self.flow_run, 'merge_car_data')
        values = step_merge_car_data.task.data.calculated_values

        expected = [len(car['name']) for car in CARS]
        self.assertEqual(sorted(values), sorted(expected))
