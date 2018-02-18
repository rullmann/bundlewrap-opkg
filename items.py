pkg_opkg = {}

actions = {
    'opkg_update': {
        'command': 'opkg update',
        'triggered': True,
    },
}

for package in node.metadata.get('opkg', {}).get('extra_packages', {}):
    pkg_opkg['{}'.format(package)] = {}
