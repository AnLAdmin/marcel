import marcel.core
import marcel.job


class JobOpArgParser(marcel.core.ArgParser):

    def __init__(self, op_name, global_state, summary, details):
        super().__init__(op_name, global_state, None, summary, details)
        id_group = self.add_mutually_exclusive_group()
        id_group.add_argument('-j', '--job',
                              type=super().constrained_type(marcel.core.ArgParser.check_non_negative,
                                                            'must be non-negative'),
                              dest='jid',
                              help='A job number, (not a process id)')
        id_group.add_argument('-p', '--process',
                              type=super().constrained_type(marcel.core.ArgParser.check_non_negative,
                                                            'must be non-negative'),
                              dest='pid',
                              help='A process id')
        self.add_argument('job_id',
                          nargs='?',
                          type=super().constrained_type(marcel.core.ArgParser.check_non_negative,
                                                        'must be non-negative'),
                          help='A job number, (not a process id)')


class JobOp(marcel.core.Op):
    
    def __init__(self):
        super().__init__()
        self.jid = None
        self.pid = None
        self.job_id = None
        self.job = None

    # BaseOp

    def setup_1(self):
        job_control = marcel.job.JobControl.only
        if self.jid is None and self.pid is None and self.job_id is None:
            raise marcel.exception.KillCommandException(f'Must specify a job or process.')
        flag_specified = self.jid is not None or self.pid is not None
        if flag_specified and self.job_id is not None:
            raise marcel.exception.KillCommandException(f'Job/process identification specified more than once.')
        if self.job_id is not None:
            self.jid = self.job_id
        assert (self.jid is None) != (self.pid is None)
        if self.jid is not None and self.jid >= len(job_control.jobs()):
            raise marcel.exception.KillCommandException(f'There is no job {self.jid}')
        self.job = job_control.job(jid=self.jid, pid=self.pid)

    def receive(self, x):
        self.action()

    # Op

    def must_be_first_in_pipeline(self):
        return True

    # JobOp

    def action(self):
        assert False
