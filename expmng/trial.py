import os
from datetime import datetime
import json


class Trial:
    """
    Class that implements a trial of an experiment. It gathers all parameters of a single trial and compiles metadata about it.

    At initialization, the parent experiment should be provided as well as all parameters of the trial. An implementation of the method 'procedure' should be given, either by subclassing this class or by assigning a function to replace the method. The trial is launch by calling the 'run' method. The procedure method should take arguments for all trial parameters passed in the __init__ as well as a checkpoint filename and a log filename.
    """
    checkpoint_filename = 'checkpoint'
    log_filename = 'log'
    params_filename = 'trial_params'

    def __init__(self, experiment, trial_name=None,
                 checkpoint_extension='.pkl', log_extension='.csv',
                 **trial_params):
        """
        Args:
            experiment (Experiment object): Parent experiment of the trial.
            trial_name (str or None, optional): Name of the trial to distinguish it from others. Should be unique.
            checkpoint_extension (str, optional): Checkpoint will be saved with pickle extension '.pkl' by default.
            log_extension (str, optional): Log will be saved with csv extension '.csv' by default.
            trial_params (dict): All parameters needed to execute the trial.
        """
        self.exp_name = experiment.exp_name
        self.trial_name = trial_name or self._generate_trial_name(experiment)
        self.trial_path = os.path.join(experiment.path, self.trial_name)

        self.checkpoint_extension = checkpoint_extension
        self.log_extension = log_extension

        self.trial_params = trial_params

        os.makedirs(self.trial_path)

    @property
    def checkpoint_filepath(self):
        return os.path.join(self.trial_path, self.checkpoint_filename + self.checkpoint_extension)
    @property
    def log_filepath(self):
        return os.path.join(self.trial_path, self.log_filename + self.log_extension)

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
        with open(self.trial_path + self.params_filename + '.json', 'w') as file:
            json.dump(json_file, file, sort_keys=True)

    def _generate_json_file(self):
        pass

    @staticmethod
    def load_json_file():
        pass
