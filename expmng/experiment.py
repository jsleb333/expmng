import os
import pickle as pkl


class Experiment:
    """
    Class that contains the trials of an experiment. Can also contain recursively other subexperiments. This class implements an API to manage such experiments and trials.
    """
    def __init__(self, exp_name):
        """
        Args:
            exp_name (str): Name of the experiment.
        """
        self.exp_name = exp_name
        self.trials = []
        self.sub_exps = []

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
        pass
    
    def filter(self, key=None):
        pass
    
    def list(self):
        pass


if __name__ == '__main__':
    exp = Experiment('test')
    exp.list()
    exp.filter()