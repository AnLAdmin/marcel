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

HELP = '''
To learn more about a topic, run the command:

{L}help TOPIC

{b:Overview:}

Run {n:help overview} to start learning about marcel. Or run {n:help}
on these introductory topics:

{L,indent=4:12}- {n:configuration}: How to customize and configure marcel.
{L,indent=4:12}- {n:interaction}: Interacting with marcel.
{L,indent=4:12}- {n:command}: Marcel operators, Linux executables.
{L,indent=4:12}- {n:function}: The use of functions in marcel commands.
{L,indent=4:12}- {n:pipeline}: The main structuring mechanism of marcel, relying on pipes 
as in other shells.
{L,indent=4:12}- {n:object}: The data operated on by commands, and carried by pipes.

{b:Objects:}

{p,wrap=F}
    - {n:file}
    - {n:history_record}
    - {n:process}

{b:Operators:}

{p,wrap=F}
    - {n:args}        - {n:bash}        - {n:bg}          - {n:cd}
    - {n:delete}      - {n:difference}  - {n:dirs}        - {n:edit}
    - {n:env}         - {n:expand}      - {n:fg}          - {n:gen}
    - {n:head}        - {n:help}        - {n:history}     - {n:ifelse}
    - {n:ifthen}      - {n:import}      - {n:intersect}   - {n:jobs}
    - {n:join}        - {n:load}        - {n:ls}          - {n:map}
    - {n:out}         - {n:popd}        - {n:ps}          - {n:pushd}
    - {n:pwd}         - {n:red}         - {n:reverse}     - {n:run}
    - {n:select}      - {n:sort}        - {n:sql}         - {n:squish}
    - {n:store}       - {n:sudo}        - {n:tail}        - {n:tee}
    - {n:timer}       - {n:unique}      - {n:union}       - {n:version}
    - {n:window}
'''
