STOP_CONTROL = False
def run(should_stop_parameter=None):
    global STOP_CONTROL
    if should_stop_parameter == 'false':
        STOP_CONTROL = False
    if should_stop_parameter == 'stop':
        STOP_CONTROL = True
