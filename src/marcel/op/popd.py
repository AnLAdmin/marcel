import pathlib

import marcel.core


SUMMARY = '''
Pop the directory stack, and cd to the new top directory.
'''


DETAILS = None


def popd():
    return Popd()


class PopdArgParser(marcel.core.ArgParser):

    def __init__(self, global_state):
        super().__init__('popd', global_state, None, SUMMARY, DETAILS)


class Popd(marcel.core.Op):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'popd()'

    # BaseOp

    def doc(self):
        return self.__doc__

    def setup_1(self):
        pass

    def receive(self, _):
        self.global_state().env.popd()
        for dir in self.global_state().env.dirs():
            self.send(dir)

    # Op

    def must_be_first_in_pipeline(self):
        return True
