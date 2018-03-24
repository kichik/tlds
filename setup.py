import os
import re
import sys
from distutils.command.build_py import build_py

from setuptools import setup, find_packages

if sys.version_info.major >= 3:
    import urllib.request

    r = urllib.request.urlopen('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    assert r.status == 200
    data = r.read().decode('utf-8').split('\n')
else:
    import urllib
    
    r = urllib.urlopen('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    assert r.getcode() == 200
    data = r.read().split('\n')
    
version = re.match('^# Version (?P<version>[0-9]+).*$', data[0]).group('version')
tlds = [i.lower() for i in data[1:] if i and not i.startswith('#')]


class build_tld_py(build_py):
    def run(self):
        if not self.dry_run:
            target_dir = os.path.join(self.build_lib, 'tlds')
            self.mkpath(target_dir)

            with open(os.path.join(target_dir, '_data.py'), 'w') as f:
                f.write('tld_set = set(%s)\n' % (tlds, ))

        build_py.run(self)


setup(name='tlds',
      version=version,
      description='Automatically updated list of valid TLDs taken directly from IANA',
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
          'Topic :: Communications',
      ],
      keywords='tld',
      author='Amir Szekely',
      author_email='kichik@gmail.com',
      url='https://github.com/kichik/tlds',
      license='MIT',
      packages=['tlds'],
      cmdclass={'build_py': build_tld_py},
      include_package_data=True,
      zip_safe=True,
      )
