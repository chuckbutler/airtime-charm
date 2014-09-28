import os

common = {}
# airtime base config options
common['basepath'] = os.path.join(os.path.sep, 'opt', 'airtime')
common['cfgpath'] = os.path.join(os.path.sep, 'etc', 'airtime')
common['publicpath'] = os.path.join(os.path.sep, 'usr', 'share', 'airtime', 'public')
# supporting airtime config
common['vhostpath'] = os.path.join(os.path.sep, 'etc', 'apache2', 'sites-available', 'airtime.conf')
common['inipath'] = os.path.join(os.path.sep, 'etc', 'airtime', 'airtime.ini')
