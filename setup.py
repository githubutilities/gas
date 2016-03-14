# Copyright (c) 2012 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import os

from setuptools import setup

def get_static_files(path):
    return [os.path.join(dirpath.replace("luigi/", ""), ext)
            for (dirpath, dirnames, filenames) in os.walk(path)
            for ext in ["*.html", "*.js", "*.css", "*.png",
                        "*.eot", "*.svg", "*.ttf", "*.woff", "*.woff2"]]

gas_package_data = sum(map(get_static_files, ["gas"]), [])

readme_note = """\
.. note::

   For the latest source, discussion, etc, please visit the
   `GitHub repository <https://github.com/githubutilities/gas>`_\n\n
"""

long_description = readme_note

install_requires = [
    'watchdog',
]

setup(
    name='gas',
    version='0.1',
    description='Workflow mgmgt + task dependency resolution + memory pipeline',
    long_description=long_description,
    author='Erik Bernhardsson',
    url='https://github.com/githubutilities/gas',
    license='Apache License 2.0',
    packages=[
        'gas',
        'gas.utils',
    ],
    package_data={
        'gas': gas_package_data
    },
    entry_points={
        'console_scripts': [
            'gasd = gas.cmdline:gasd',
        ]
    },
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Pipeline',
    ],
)
