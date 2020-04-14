# Copyright 2011 James McCauley
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Fires up topology, discovery, and a l2 learning switch controller
"""

def launch ():
    import pox3.topology
    pox3.topology.launch()
    import pox3.openflow.discovery
    pox3.openflow.discovery.launch()
    import pox3.openflow.topology
    pox3.openflow.topology.launch()
    import pox3.forwarding.l2_learning
    pox3.forwarding.l2_learning.launch()
