import sys
import os
import re
import config
import logging
import shutil

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
    
    # get devices from zenoss perf directory
    for device in zenossDevices:
        # remove unwanted chars from device name
        sanitizedDevice = sanitizePath(device)
        # maintain list of sanitized device names for later comparison
        zenossDevicesSanitized.append(sanitizedDevice)
        # check for match against regex list
        if matchDevice(device, config.devicePatterns):
            zenossDevicePath = os.path.join(zenossPath, device)
            graphiteDevicePath = os.path.join(config.graphiteRoot, sanitizedDevice)
            # create device directory if not existing
            if not os.path.exists(graphiteDevicePath):
                os.mkdir(graphiteDevicePath)
            # device root metric symlinks
            for metric, zenossRrd in config.metricMapDeviceRoot.iteritems():
                if os.path.exists(os.path.join(zenossDevicePath, zenossRrd)):
                    symlinkName = os.path.join(graphiteDevicePath, metric)
                    symlinkTarget = os.path.join(zenossDevicePath, zenossRrd)
                    if not os.path.exists(symlinkName):
                        if config.logging:
                            log.info('creating symlink %s -> %s' % (symlinkName, symlinkTarget))
                        try:
                            os.symlink(symlinkTarget, symlinkName)
                        except OSError, err:
                            log.info(err)
            # OS Component symlinks
            for OSComponentGroup, metrics in config.metricMapOSComponents.iteritems():
                if os.path.exists(os.path.join(zenossDevicePath, 'os', OSComponentGroup)):
                    if not os.path.exists(os.path.join(graphiteDevicePath, OSComponentGroup)):
                        os.mkdir(os.path.join(graphiteDevicePath, OSComponentGroup))
                    components = os.listdir(os.path.join(zenossDevicePath, 'os', OSComponentGroup))
                    for component in components:
                        if not os.path.exists(os.path.join(graphiteDevicePath, OSComponentGroup, sanitizePath(component))):
                            os.mkdir(os.path.join(graphiteDevicePath, OSComponentGroup, sanitizePath(component)))
                        for metric, zenossRrd in metrics.iteritems():
                            if os.path.exists(os.path.join(zenossDevicePath, 'os', OSComponentGroup, component, zenossRrd)):
                                symlinkName = os.path.join(graphiteDevicePath, OSComponentGroup, sanitizePath(component), metric)
                                symlinkTarget = os.path.join(zenossDevicePath, 'os', OSComponentGroup, component, zenossRrd)
                                if not os.path.exists(symlinkName):
                                    if config.logging:
                                        log.info('creating symlink %s -> %s' % (symlinkName, symlinkTarget))
                                    try:
                                        os.symlink(symlinkTarget, symlinkName)
                                    except OSError, err:
                                        log.info(err)


    # delete devices no longer in zenoss
    if config.deleteOld:
        graphiteDevices = os.listdir(config.graphiteRoot) 
        for device in graphiteDevices:
            if device not in zenossDevicesSanitized:
                removalDir = os.path.join(config.graphiteRoot, device)
                if config.logging:
                    log.info('removing symlinks for %s: device no longer in Zenoss' % device)
                try:
                    shutil.rmtree(removalDir)
                except OSError, err:
                    log.info(err)
    return 0

if __name__ == '__main__':
    sys.exit(main())
