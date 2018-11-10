import os
from datetime import datetime
import json


class Trial:
    """
    Class that implements a trial of an experiment. It gathers all parameters of a single trial and compiles metadata about it.

    At initialization, the parent experiment should be provided as well as all parameters of the trial. An implementation of the method 'procedure' should be given, either by subclassing this class or by assigning a function to replace the method. The trial is launch by calling the 'run' method. The procedure method should take arguments for all trial parameters passed in the __init__ as well as a checkpoint filename and a log filename.
    """
    checkpoint_extension = '.ckpt'
    log_extension = '.log'

    def __init__(self, experiment, trial_name=None, **trial_params):
        self.exp_name = experiment.exp_name
        self.trial_name = trial_name or self._generate_trial_name(experiment)
        self.trial_params = trial_params
        self.trial_path = os.path.join(experiment.path, self.trial_name)

        os.makedirs(self.trial_path)

    @property
    def checkpoint_filename(self):
        return os.path.join(self.trial_path, self.trial_name + self.checkpoint_extension)
    @property
    def log_filename(self):
        return os.path.join(self.trial_path, self.trial_name + self.log_extension)

    def _generate_trial_name(self, experiment):
        """
        Generates a trial name so that no trial names collide.
        """
        pass

    def procedure(self, *, checkpoint_filename, log_filename, **trial_params):
        """
        Procedure to implement to run the trial.
        """
        raise NotImplementedError

    def run(self):
        """
        Runs the trial, generates all metadata associated and dumps every files created at the right place.
        """
        self.date_time_run = datetime.now().isoformat()
        self.procedure()

    def save_trial(self):
        json_file = self._generate_json_file()
        with open(self.trial_path + '/trial_params.json', 'w')

    def _generate_json_file(self):
        pass

    @staticmethod
    def load_json_file():
        pass
