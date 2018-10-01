# File: Main.py
# sync_sync synchronizes sensitivities cross games. Currently supported: CS:GO and Rainbow Six Siege
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

import glob

from Math import convert_siege_to_cs, convert_cs_to_siege


def read_from_siege():
    siege_target = glob.glob('C:/Users/*/Documents/My Games/Rainbow Six - Siege/*/GameSettings.ini')

    with open(siege_target[0]) as f:
        content = f.readlines()

    sens = 0
    mouse_multiplier_unit = 0
    aim = 0
    x_factor_aiming = 0

    for x in content:

        if "MouseYawSensitivity" in x:
            sens = int(x.split("=")[1])
        elif "MouseSensitivityMultiplierUnit" in x:
            mouse_multiplier_unit = float(x.split("=")[1])
        elif "XFactorAiming" in x:
            x_factor_aiming = float(x.split("=")[1])
        elif "AimDownSightsMouse" in x:
            aim = int(x.split("=")[1])

    return [sens, mouse_multiplier_unit, aim, x_factor_aiming]


def read_from_cs():
    cs_target = glob.glob('C:/Program Files (x86)/Steam/userdata/*/730/local/cfg/config.cfg')

    with open(cs_target[0]) as f:
        content = f.readlines()

    hipfire = 0
    awp = 0

    for x in content:
        if x.startswith("sensitivity \""):
            hipfire = float(x.split("\"")[1])
        if "zoom_sensitivity_ratio_mouse" in x:
            awp = float(x.split("\"")[1])

    return [hipfire, awp]


def write_to_cs():
    values = read_from_siege()
    csgo_vals = convert_siege_to_cs(values[0], values[1], values[2], values[3])
    cs_target = glob.glob('C:/Program Files (x86)/Steam/userdata/*/730/local/cfg/config.cfg')
    with open(cs_target[0]) as f:
        content = f.readlines()

    modified_list = list()

    for x in content:
        if x.startswith("sensitivity \""):
            modified_list.append("sensitivity \"" + str(csgo_vals[0]) + "\"\n")
            continue
        elif "zoom_sensitivity_ratio_mouse" in x:
            modified_list.append("zoom_sensitivity_ratio_mouse \"" + str(csgo_vals[1]) + "\"\n")
            continue
        modified_list.append(x)

    f = open(cs_target[0], 'w')
    for x in modified_list:
        f.write(x)


def write_to_siege():
    values = read_from_cs()
    siege_vals = convert_cs_to_siege(values[0], values[1])
    siege_target = glob.glob('C:/Users/*/Documents/My Games/Rainbow Six - Siege/*/GameSettings.ini')
    with open(siege_target[0]) as f:
        content = f.readlines()

    modified_list = list()

    for x in content:
        if x.startswith("MouseYawSensitivity"):
            modified_list.append("MouseYawSensitivity=50\n")
            continue
        elif x.startswith("MousePitchSensitivity"):
            modified_list.append("MousePitchSensitivity=50\n")
            continue
        elif "MouseSensitivityMultiplierUnit" in x:
            modified_list.append("MouseSensitivityMultiplierUnit=" + str(siege_vals[0]) + "\n")
            continue
        elif "XFactorAiming" in x:
            modified_list.append("XFactorAiming=" + str(siege_vals[1]) + "\n")
            continue
        elif "AimDownSightsMouse" in x:
            modified_list.append("AimDownSightsMouse=100\n")
            continue
        modified_list.append(x)

    f = open(siege_target[0], 'w')
    for x in modified_list:
        f.write(x)


if __name__ == '__main__':
    print("Main.py: Copyright (C) 2018  Arvind Mukund<armu30@gmail.com>\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it\n")
    print("1. Copy CS:GO to Siege")
    print("2. Copy Siege to CS:GO")
    print("3. Dry Run")
    val = input("Enter your input: ")
    val = int(val)
    if val == 1:
        write_to_siege()
    elif val == 2:
        write_to_cs()
    elif val == 3:
        print(
            "------------------------------------------------------------------------------------------------------\n"
            "Current CS vals [sensitivity,zoom_sensitivity]: " + str(read_from_cs()))
        print("Current siege vals [sens, mouse_multiplier_unit, zoom, x_factor_aiming]: " + str(read_from_siege()))
        print("------------------------------------------------------------------------------------------------------")
    else:
        print("unknown val")
