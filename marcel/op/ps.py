# This file is part of Marcel.
# 
# Marcel is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or at your
# option) any later version.
# 
# Marcel is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Marcel.  If not, see <https://www.gnu.org/licenses/>.

import marcel.core
import marcel.exception
import marcel.object.process
import marcel.util


SUMMARY = '''
Generate a stream of {n:Process} objects, representing processes.
'''


DETAILS = '''
By default, {r:ps} outputs a {n:Process} object for each process. The flags are all 
concerned with filtering:

{L}{r:--user}: By user.
{L}{r:--group}: By group.
{L}{r:--pid}: By pid.
{L}{r:--command}: By command (select commands containing the given string).

These are conveniences, as arbitrary predicates can be applied by piping {r:ps} output to 
{n:select}.
'''


def ps(user=None, group=None, pid=None, command=None):
    op = Ps()
    op.user = user
    op.group = group
    op.pid = pid
    op.command = command
    return op


class PsArgParser(marcel.core.ArgParser):

    def __init__(self, env):
        super().__init__('ps',
                         env,
                         ['-u', '--user', '-g', '--group', '-p', '--pid', '-c', '--command'],
                         SUMMARY,
                         DETAILS)
        filter_group = self.add_mutually_exclusive_group()
        filter_group.add_argument('-u', '--user',
                                  help='Select processes owned by the specified username or uid.')
        filter_group.add_argument('-g', '--group',
                                  help='Select processes owned by the specified group name or gid.')
        filter_group.add_argument('-p', '--pid',
                                  help='Select the process with the given pid.')
        filter_group.add_argument('-c', '--command',
                                  help='Select processes whose commandline contains the given string.')


class Ps(marcel.core.Op):

    def __init__(self):
        super().__init__()
        self.user = None
        self.group = None
        self.pid = None
        self.command = None
        self.filter = None

    # BaseOp
    
    def setup_1(self):
        # user, group can be name or id. A name can be numeric, and in that case, the name interpretation
        # takes priority. Convert name to uid, since that is a cheaper lookup on a Project.
        option_count = 0
        if self.user is not None:
            option_count += 1
            self.user = Ps.convert_to_id(self.user, marcel.util.uid)
            self.filter = lambda p: p.uid == self.user
        if self.group is not None:
            option_count += 1
            self.group = Ps.convert_to_id(self.group, marcel.util.gid)
            self.filter = lambda p: p.gid == self.group
        if self.pid is not None:
            option_count += 1
            try:
                self.pid = int(self.pid)
                self.filter = lambda p: p.pid == self.pid
            except ValueError:
                raise marcel.exception.KillCommandException(f'pid must be an int: {self.pid}')
        if self.command is not None:
            option_count += 1
            self.filter = lambda p: self.command in p.commandline
        if option_count > 1:
            raise marcel.exception.KillCommandException('ps options are mutually exclusive')
        if option_count == 0:
            self.filter = lambda p: True

    def receive(self, _):
        for process in marcel.object.process.processes():
            if self.filter(process):
                self.send(process)

    # Op

    def must_be_first_in_pipeline(self):
        return True

    # For use by this class

    @staticmethod
    def convert_to_id(name, lookup):
        id = lookup(name)
        if id is None:
            try:
                id = int(name)
            except ValueError:
                pass
        if id is None:
            raise marcel.exception.KillCommandException(f'{name} is not a recognized id or name.')
        return id

