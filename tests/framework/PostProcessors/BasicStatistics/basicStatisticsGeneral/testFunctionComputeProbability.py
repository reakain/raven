# Copyright 2017 Battelle Energy Alliance, LLC
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
'''
Created on NO NEED TO KNOW

@author: alfoa
'''
import numpy as np
import math

def failureProbability(self):
  failure = 0
  success = 0
  for element in range(len(self.x01)):
    if self.x01[element] > 2:
      failure += 1
    else:
      success += 1
  if failure > 0 and success > 0:
    return float(failure)/float(failure+success)
  else:
    return 0.0
