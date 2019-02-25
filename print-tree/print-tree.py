#!/usr/bin/python

import os


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        # import ipdb; ipdb.set_trace()
        for f in sorted(files):
            print('{}{}'.format(subindent, f))


list_files(os.getcwd())
