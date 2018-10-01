# sync_sens

Sync_sens is used to synchronize sensitivities across games

## Current features
  - Copy CS:GO to Siege config
  - Copy Siege to CS:GO config
  - Dry Run

### Usage
  - The first 2 options re-writes the sensitivities without confirmation so make sure you've created a backup before executing
  - The Dry Run prints the current values of the sensitivities

#### Example
```$python Main.py```
```sh
1. Copy CS:GO to Siege
2. Copy Siege to CS:GO
3. Dry Run
Enter your input: 3
------------------------------------------------------------------------------------------------------
Current CS vals [sensitivity,zoom_sensitivity]: [2.6, 0.88]
Current siege vals [sens, mouse_multiplier_unit, zoom, x_factor_aiming]: [50, 0.003993, 100, 0.011175]
------------------------------------------------------------------------------------------------------
```
