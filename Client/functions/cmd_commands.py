import os

commands = [
    ['sleep','rundll32.exe powrprof.dll, SetSuspendState Sleep'],['test','D:\detector.jpg']
]


def execute_cmd_command(command_word):
    for command in commands:
        if command[0] == command_word.strip():
            os.system(command[1])


