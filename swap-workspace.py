#!/usr/bin/python2.7
import i3

# swap workspaces on two monitors
for output in i3.get_outputs():
    if output['active']:
        i3.workspace(output['current_workspace'])
        i3.command('move', 'workspace to output right')
