'''
author: dang100
date: 2022/4/15

windows cmd
'''
from os import popen

def netstat_cmd():
    cmd_result = ''
    cmd_analyse = []
    # all, number, pid, establish 
    with popen('netstat -ano | findstr EST', 'r') as f:
        cmd_result = f.read()
    cmd_result = cmd_result.split('\n')
    for i in cmd_result:
        if i == '':
            continue
        cmd_analyse.append(' '.join(i.split()).split(' '))

    return cmd_analyse

def netstat_checklist(cmd = None):
    if cmd == None:
        return

    