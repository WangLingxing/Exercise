#!/usr/bin/env python

def safe_float(obj):
    """safe version of float"""
    try:
        retval = float(obj)
    except (ValueError, TypeError) as diag:
        retval = str(diag)
    return retval


def logResult():
    'handles all the data processing'
    log = open('carlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.0
    log.write('account log:\n')

    for eachtxns in txns:
        result = safe_float(eachtxns)
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')
        else:
            log.write('ignored: %s' % result)
    print('$%.2f (new balance)' % (total))
    log.close()


logResult()
