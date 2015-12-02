
#!/usr/bin/env python

from distutils.core import setup

setup(name='annotation of genomic mutation',
    version='0.1.0',
    description='Python tools to annotate genomic mutations.',
    author='Ken-ichi Chiba',
    author_email='kchiba@hgc.jp',
    url='https://github.com/ken0-1n/mutanno',
    package_dir = {'': 'lib'},
    packages=['mutanno'],
    scripts=['mutanno'],
    license='GPL-3'
)
