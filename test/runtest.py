# -*- coding: utf-8 -*-
#
# Copyright 2012-2015 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys
import warnings

import nose

def main():
    # Add project directory to python path
    run_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
    sys.path.insert(0, run_path)

    with warnings.catch_warnings():
        warnings.simplefilter("default")
        warnings.filterwarnings(
            "ignore",
            message='(.*)outputs has no custom(.*)',
            category=UserWarning
        )
        nose.main()

__name__ == '__main__' and main()
