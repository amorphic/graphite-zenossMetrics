import sys
import os
import re
import config
import logging

# logging
log = logging.getLogger('graphite-zenossMetrics')
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

def sanitizePath(path):
    '''remove .s from path for Graphite compatibility'''

    return path.replace('.', '_')

def matchDevice(device, patterns):
    '''check if device matches any regex in patterns'''

    for pattern in patterns:
        # return True on match
        if re.match(pattern, device):
            return True
    # no matches so return False
    return False

def main():
    
    
    zenossPath = os.path.join(config.zenossRoot, 'Devices')
    zenossDevices = os.listdir(zenossPath) 
    zenossDevicesSanitized = []
    deleteOld = True
    
    # get devices for zenoss perf directory
    for device in zenossDevices:
        # remove unwanted chars from device name
        sanitizedDevice = sanitizePath(device)
        # maintain list of sanitized device names for later comparison
        zenossDevicesSanitized.append(sanitizedDevice)
        # check for match against regex list
        if matchDevice(device, config.devicePatterns):
            # create symlnk name and target paths to device
            linkNameDevicePath = sanitizePath(os.path.join(config.graphiteRoot, device))
            linkTargetDevicePath = sanitizePath(os.path.join(zenossPath, device))
            # create device directory if not existing
            if not os.path.exists(linkNameDevicePath):
                os.mkdir(linkNameDevicePath)
            for metricGroup, metrics in config.metricMap.iteritems():
                # create symlink path to metric group
                linkNameMetricGroupPath = sanitizePath(os.path.join(linkNameDevicePath, metricGroup))
                # create metricGroup directory if not existing
                if not os.path.exists(linkNameMetricGroupPath):
                    os.mkdir(linkNameMetricGroupPath)
                for metric, zenossRrd in metrics.iteritems():
                    # ultimate symlink name
                    symlinkName = sanitizePath(os.path.join(linkNameMetricGroupPath, metric))
                    # ultimate symlink target
                    symlinkTarget = os.path.join(linkTargetDevicePath, zenossRrd)
                    # create symlink
                    log.info('creating symlink %s -> %s' % (symlinkName, symlinkTarget))
                    try:
                        os.symlink(symlinkTarget, symlinkName)
                    except OSError, err:
                        log.info(err)

    # delete devices no longer in zenoss
    if deleteOld:
        graphiteDevices = os.listdir(config.graphiteRoot) 
        for device in graphiteDevices:
            if device not in zenossDevicesSanitized:
                removalDir = os.path.join(config.graphiteRoot, device)
                log.info('removing symlinks for %s: device no longer in Zenoss' % device)
                #os.rmdir(removalDir)
    return 0

if __name__ == '__main__':
    sys.exit(main())
