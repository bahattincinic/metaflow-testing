import json
import os
import subprocess
import unittest
import uuid
from os.path import abspath, dirname, join

from metaflow import Run, Step

APP_DIR = dirname(dirname(dirname(abspath(__file__))))
TESTS_DIR = join(APP_DIR, 'tests')


class BaseTestCase(unittest.TestCase):

    @classmethod
    def run_flow(cls, name, context='default') -> Run:
        """
        This function runs Metaflow flow and returns Run object.
        :param name: filename.flowname (e.g bidding.AdNetworkOptimizationFlow)
        :param context: command context (env. variables, arguments etc.)
        :return: metaflow.client.Run
        """
        context = cls.load_contexts()[context]
        run_id_file = f"unittest-{str(uuid.uuid4())}"
        python_path = os.environ['_']
        file_name, flow_name = name.split('.')

        cmd = [
            python_path, '-B', f"{join(APP_DIR, file_name)}.py",
        ]
        cmd.extend(context['args'])
        cmd.extend(['run', f'--run-id-file={run_id_file}'])

        env = dict(os.environ)
        env.update(context['env'])

        subprocess.check_call(" ".join(cmd),
                              env=env,
                              cwd=APP_DIR,
                              shell=True)

        with open(join(APP_DIR, run_id_file)) as f:
            run_id = f.read()

        # cleanup Metaflow run_id file
        os.remove(join(APP_DIR, run_id_file))

        return Run(f"{flow_name}/{run_id}")

    @classmethod
    def load_contexts(cls) -> dict:
        with open(join(TESTS_DIR, 'contexts.json'), 'rb') as f:
            return json.loads(f.read())['contexts']

    def get_step(self, run: Run, step_name: str) -> Step:
        """
        Get step function returns metaflow `Step`
        object for given `Run` and `step_name`

        :param run: metaflow.Run
        :param step_name: step name
        :return: metaflow.client.Step
        """
        flow_id = run._object['flow_id']
        return Step(f'{flow_id}/{run.id}/{step_name}')
