

class Experiment:
    def __init__(self, exp_name):
        self.exp_name = exp_name
        self.trials = []

    def open(self, filename=None):
        pass

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