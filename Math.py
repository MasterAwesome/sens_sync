# File: Math.py: Conversion math handled here
# Copyright (C) 2018  Arvind Mukund<armu30@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

def convert_cs_to_siege(hipfire, awp):
    siege_hip_multiplier = hipfire * 0.00153589608577778
    siege_awp_multiplier = awp * 0.0126984126984127
    return [str(round(siege_hip_multiplier, 6)), str(round(siege_awp_multiplier, 6))]


def convert_siege_to_cs(sens, mmultipler, aim, amultiplier):
    cs_hip = 13.02171428470 * sens * mmultipler
    cs_awp = amultiplier * 50  * aim * 0.012
    return [str(round(cs_hip, 2)), str(round(cs_awp, 2))]
