import os
import pickle as pkl


class Experiment:
    """
    Class that contains the trials of an experiment. Can also contain recursively other subexperiments. This class implements an API to manage such experiments and trials.
    """
    path_name = 'experiment'

    def __init__(self, exp_name):
        """
        Args:
            exp_name (str): Name of the experiment.
        """
        self.exp_name = exp_name
        self.path = os.path.join('./', self.path_name)
        self.trials = []
        self.sub_exps = []
        self.selected_trials = []

    @staticmethod
    def load(filename=None):
        """
        Loads into memory an experiment.

        Args:
            filename (str or None, optional): Name of the experiment to load. If None, it will try to automatically find an experiment in a subdirectory of the current one.
        """
        if not filename:
            _, sub_dir, _ = next(os.walk('.'))
            if 'experiment' not in sub_dir:
                print('No experiment found.')
                return

            _, _, files = next(os.walk('./experiment')):
            for file in files:
                if file.endswith('.expmng'):
                    filename = file
                    break
            else:
                print('No experiment found.')
                return

        with open(filename, 'rb') as file:
            return = pkl.load(file)

    def sort(self, key=lambda param: None):
        """
        Sorts the trials according to the key.

        Args:
            key (callable, optional): Function to compare the values of the parameter. By default, will sort according to the date.

        Returns the list of sorted trials.
        """
        pass

    def filter(self, key=None, value=None):
        """
        Filters the current selected trials, masking all trials not having the key.

        Args:
            key (string or None, optional): Parameter of the trial to apply a filter on. If None, returns a list of all possible filter keys.
            value (int, float or str, optional): Value of the parameter to filter.

        Returns the list of filtered trials or a list of valid filter keys (if None).
        """
        pass

    def list(self):
        """
        Lists all current selected trials.
        """
        pass


if __name__ == '__main__':
    exp = Experiment('test')
    exp.list()
    exp.filter()
