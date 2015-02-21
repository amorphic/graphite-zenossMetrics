# root directory of Zenoss metric RRD files
# this should be an nfs mount to /opt/zenoss/perf on the Zenoss server
zenossRoot = '/mnt/nfs/zenossrrd/perf'

# root path of Zenoss metrics
graphiteRoot = '/opt/graphite/storage/rrd/Zenoss'

# regexes to match Zenoss device names
devicePatterns = [
    '.*'
]

# log symlink creation and deleted device cleanup to stdout
logging = False

# delete old devices from graphiteRoot
deleteOld = True

# map of Graphite device root metrics to Zenoss metric RRD files
metricMapDeviceRoot = {
    'cpuidle.rrd'      :   'ssCpuIdle_ssCpuIdle.rrd',
    'cpuwait.rrd'      :   'ssCpuRawWait_ssCpuRawWait.rrd',
    'cpusystem.rrd'    :   'ssCpuSystem_ssCpuSystem.rrd',
    'cpuuser.rrd'      :   'ssCpuUser_ssCpuUser.rrd',
    'memoryreal.rrd'   :   'memAvailReal_memAvailReal.rrd',
    'memoryswap.rrd'   :   'memAvailSwap_memAvailSwap.rrd',
    'memorybuffer.rrd' :   'memBuffer_memBuffer.rrd',
    'memorycache.rrd'  :   'memCached_memCached.rrd',
    'load1min.rrd'     :   'laLoadInt1_laLoadInt1.rrd',
    'load5min.rrd'     :   'laLoadInt5_laLoadInt5.rrd',
    'load15min.rrd'    :   'laLoadInt15_laLoadInt15.rrd',
    'IOreads.rrd'      :   'ssIORawReceived_ssIORawReceived.rrd',
    'IOwrites.rrd'     :   'ssIORawSent_ssIORawSent.rrd'
}

# map of Graphite interface metrics to Zenoss metric RRD files
metricMapOSComponents = {
    'interfaces'  : {
        'inputoctets.rrd'  :   'ifHCInOctets_ifHCInOctets.rrd',
        'inputpackets.rrd' :   'ifHCInUcastPkts_ifHCInUcastPkts.rrd',
        'inputerrors.rrd'  :   'ifInErrors_ifInErrors.rrd',
        'outputoctets.rrd' :   'ifHCOutOctets_ifHCOutOctets.rrd',
        'outputpackets.rrd':   'ifHCOutUcastPkts_ifHCOutUcastPkts.rrd',
        'outputerrors.rrd' :   'ifOutErrors_ifOutErrors.rrd'
    },
    'filesystems' : {
        'usedblocks.rrd'   :   'usedBlocks_usedBlocks.rrd'
    },
    'processes'   : {
        'processcount.rrd' :   'count_count.rrd',
        'cpuutil.rrd'      :   'cpu_cpu.rrd',
        'memoryused.rrd'   :   'mem_mem.rrd'
    }
}

