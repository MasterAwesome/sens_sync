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
from implementations.CSGOSensitivity import CSGOSensitivity
from implementations.R6Sensitivity import R6Sensitivity

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
        CSSens = CSGOSensitivity()
        R6Sens = R6Sensitivity(prev_impl=CSSens)
        R6Sens.write_to_file()

    elif val == 2:
        R6Sens = R6Sensitivity()
        CSSens = CSGOSensitivity(prev_impl=R6Sens)
        CSSens.write_to_file()

    elif val == 3:
        R6Sens = R6Sensitivity()
        CSSens = CSGOSensitivity()

        R6SensConverted = R6Sensitivity(prev_impl=CSSens)
        CSSensConverted = CSGOSensitivity(prev_impl=R6Sens)

        print("\nCURRENT")
        print("-" * 150)
        print("Siege vals [sens, mouse_multiplier_unit, zoom, x_factor_aiming]: " + R6Sens.__repr__())
        print("CS vals [sensitivity,zoom_sensitivity]: " + CSSens.__repr__())
        print("-" * 150)

        print("\nCONVERTED")
        print("-" * 150)
        print("Siege vals [sens, mouse_multiplier_unit, zoom, x_factor_aiming]: " + R6SensConverted.__repr__())
        print("CS vals [sensitivity, zoom_sensitivity]: " + CSSensConverted.__repr__())
        print("-" * 150)
    elif val == 42:
        print("MEANING OF LIFE ATTAINED!")
    else:
        raise NotImplementedError("The option you're looking for doesn't exist :O. Try 42")
