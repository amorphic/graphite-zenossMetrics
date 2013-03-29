# root directory of Zenoss metric RRD files
# this should be an nfs mount to /opt/zenoss/perf/Devices on the Zenoss server
zenossRoot = '/mnt/zenossPerf'

# root path of Zenoss metrics
#graphiteRoot = '/opt/grahite/storage/rrd/Zenoss/Linux'
graphiteRoot = '/home/james/gztest'

# regexes to match Zenoss Linux server device names
devicePatterns = [
    '.*woy.amorphicdestiny.com'
]

# map of Graphite metric paths to Zenoss metric RRD files
# in most circumstances this should not need to be changed
metricMap = {
    'cpu'       :   {
        'idle'      :   'ssCpuIdle_ssCpuIdle.rrd',
        'wait'      :   'ssCpuRawWait_ssCpuRawWait.rrd',
        'system'    :   'ssCpuSystem_ssCpuSystem.rrd',
        'user'      :   'ssCpuUser_ssCpuUser.rrd'
    },
    'memory'    :   {
        'real'      :   'memAvailReal_memAvailReal.rrd',
        'swap'      :   'memAvailSwap_memAvailSwap.rrd',
        'buffer'    :   'memBuffer_memBuffer.rrd',
        'cache'     :   'memCached_memCached.rrd'
    },
    'load'      :   {
        '1min'      :   'laLoadInt1_laLoadInt1.rrd',
        '5min'      :   'laLoadInt5_laLoadInt5.rrd',
        '15min'     :   'laLoadInt15_laLoadInt15.rrd'
    },
    'io'        :   {
        'reads'     :   'ssIORawReceived_ssIORawReceived.rrd',
        'writes'    :   'ssIORawSent_ssIORawSent.rrd'
    }
}

