from marcel.api import *

# negate = map(lambda x: -x)
# run(gen(5) | negate)
# run(gen(5) | negate | negate)

cat = map(lambda f: (f, f.readlines())) | expand(1)
# for f, line in ls('/home/jao/*.txt', file=True, recursive=True) | cat:
#     print(f'{f}: {line}')

from time import time as now
import marcel.util
start = now()
N = 1000
for i in range(N):
    marcel.util.copy(cat)
stop = now()
avg_msec = 1000 * (stop - start) / N
print(f'Average copy time: {avg_msec} msec')

# run(remote('jao', gen(3)))

# run(ls())
#
# # run
# run(gen(3))
#
# # gather
# print(gather(gen(3)))
#
# # first
# print(first(gen(start=100, count=10)))
#
# # iterator
# for x in gen(3, start=5):
#     print(x)
#
# for ext, count, size in (ls('/home/jao/git/marcel', file=True, recursive=True)
#                          | map(lambda f: (f.suffix.lower(), 1, f.size))
#                          | red(None, r_plus, r_plus)
#                          | sort(lambda ext, count, size: -size)
#                          | head(10)):
#     print(f'{ext}: {size / count}')
#
# for size, pid, commandline in (ps(command='python')
#                                | sort(lambda p: p.VmRSS)
#                                | map(lambda p: (p.VmRSS, p.pid, p.commandline))):
#     print(f'{size} -- {pid}: {commandline}')
#
# for x in gen(3, -1) | map(lambda x: 1/x):
#     print(x)
#
# # # first with exception
# # print(first(map(lambda: 1 / 0)))
