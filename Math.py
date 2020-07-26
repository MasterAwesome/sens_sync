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
    SIEGE_CS_MAGIC_NUMBER_LOOK_AROUND = 0.00153589608577778
    SIEGE_CS_MAGIC_NUMBER_AIM_DOWN = 0.0126984126984127
    
    siege_hip_multiplier = hipfire * SIEGE_CS_MAGIC_NUMBER_LOOK_AROUND
    siege_awp_multiplier = awp * SIEGE_CS_MAGIC_NUMBER_AIM_DOWN
    return [str(round(siege_hip_multiplier, 6)), str(round(siege_awp_multiplier, 6))]


def convert_siege_to_cs(sens, mmultipler, aim, amultiplier):
    CS_SIEGE_MAGIC_NUMBER_LOOK_AROUND = 13.02171428470
    CS_SIEGE_MAGIC_NUMBER_AIM_DOWN = 0.7875
    
    cs_hip =  sens * mmultipler * CS_SIEGE_MAGIC_NUMBER_LOOK_AROUND
    cs_awp = amultiplier * aim * CS_SIEGE_MAGIC_NUMBER_AIM_DOWN
    return [str(round(cs_hip, 2)), str(round(cs_awp, 2))]
