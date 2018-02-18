# opkg

[opkg](https://git.yoctoproject.org/cgit/cgit.cgi/opkg/) is a package manager used on various systems. It can be installed on a [Synology NAS with entware-ng](https://github.com/Entware-ng/Entware-ng/wiki/Install-on-Synology-NAS) as well as many other systems.

This bundle is proving an action to update the opkg package list.
Beside that it enabled other bundles to add package requirements via metadata.

## Requirements

* Installation of opkg
* opkg binary in path
  * This can become an issue on some devices where opkg is not the standard package manager. You may have to add a symlink in another bundle to make opkg available to bundlewrap.

## Metadata

    'metadata': {
        'opkg': {
			      'extra_packages': ['somepackage'], # optional
        },
    }

## Usage in metadata.py

Other bundles can add opkg dependencies as follows:

    @metadata_processor
    def opkg(metadata):
        if node.has_bundle('opkg'):
            metadata.setdefault('opkg', {})
            metadata['opkg'].setdefault('extra_packages', [])
            for package in ['htop']:
                if package not in metadata['opkg']['extra_packages']:
                    metadata['opkg']['extra_packages'].append(package)
        return metadata, DONE
