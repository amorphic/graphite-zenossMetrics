import sys
import os
import re
import config


def sanitizePath(path):
    '''remove .s from path for Graphite compatibility'''

    return path.replace('.', '_')

def matchDevice(device, patterns):
    '''check if device matches any regex in patterns'''

    for pattern in patterns:
        # if regex match return True

    return False

def main():
    
    # get devices for zenoss perf directory
    for device in os.listdir(config.zenossPerfDir):
        # check for match against regex list
        if matchDevice(device, config.devicePatterns):
            # add symlinks
            for metricGroup, metrics in metricMap:
                pass
    return 0

if __name__ == '__main__':
    sys.exit(main())
