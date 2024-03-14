
on_subs = ['activate', 'true', 'enable', 'on', 'yes', '1', 'y']
off_subs = ['deactivate', 'false', 'disable', 'off', 'no',  '0', 'n']

def on_off_to_string(bool):
    """Returns string 'on'/'off' based on received boolean variable."""

    if bool: return 'on'
    return 'off'

def show_