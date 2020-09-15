import glob

from implementations.interface.BaseSensitivity import BaseSensitivity


class R6Sensitivity(BaseSensitivity):
    """
    This implementation of BaseSensitivity can crunch Tom Clancy's Rainbow Six Siege numbers
    """

    # siege to base sens numbers
    SIEGE_BASE_MAGIC_NUMBER_LOOK_AROUND = 0.00153589608577778
    SIEGE_BASE_MAGIC_NUMBER_AIM_DOWN = 0.0126984126984127

    # base to siege sens numbers
    BASE_SIEGE_MAGIC_NUMBER_LOOK_AROUND = 13.02171428470
    BASE_SIEGE_MAGIC_NUMBER_AIM_DOWN = 0.7875

    def __init__(self, cfg_path='C:/Users/*/Documents/My Games/Rainbow Six - Siege/*/GameSettings.ini', prev_impl=None):
        self.__mouse_multiplier_unit, self.__x_factor_aiming = [0, 0]
        self.__actual_sens, self.__actual_ads_sens = [50, 100]
        super(R6Sensitivity, self).__init__(cfg_path, prev_impl)

    def read_from_base_sensitivity(self, __cls: BaseSensitivity):
        self.hipfire = __cls.hipfire
        self.ads = __cls.ads
        self.__mouse_multiplier_unit, self.__x_factor_aiming = self.__base_sensitivity_to_r6_sens()

    def __base_sensitivity_to_r6_sens(self):
        """
        Cool math prior to Y5S3 (TODO: Test this in Y5S3)
        """
        siege_hip_multiplier = self.hipfire * R6Sensitivity.SIEGE_BASE_MAGIC_NUMBER_LOOK_AROUND
        siege_awp_multiplier = self.ads * R6Sensitivity.SIEGE_BASE_MAGIC_NUMBER_AIM_DOWN
        return str(round(siege_hip_multiplier, 6)), str(round(siege_awp_multiplier, 6))

    def __r6_sens_to_base_sensitivity(self, sens, mouse_multiplier_unit, aim, x_factor_aiming):
        """
        Cool math prior to Y5S3 (TODO: Test this in Y5S3)
        """
        cs_hip = sens * mouse_multiplier_unit * R6Sensitivity.BASE_SIEGE_MAGIC_NUMBER_LOOK_AROUND
        cs_awp = x_factor_aiming * aim * R6Sensitivity.BASE_SIEGE_MAGIC_NUMBER_AIM_DOWN
        return cs_hip, cs_awp

    def read_from_config(self):
        siege_target = glob.glob(self.cfg_path)

        profile_target = self.__siege_profiler(siege_target)

        with open(profile_target) as f:
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

        self.__actual_sens = sens
        self.__actual_ads_sens = aim
        self.hipfire, self.ads = self.__r6_sens_to_base_sensitivity(sens, mouse_multiplier_unit, aim, x_factor_aiming)
        self.__mouse_multiplier_unit = mouse_multiplier_unit
        self.__x_factor_aiming = x_factor_aiming

    def __siege_profiler(self, siege_target):
        """
        Supports multiple profiles here!
        """
        if len(siege_target) > 1:
            print("\nDetected profiles ")
            for index, file in enumerate(siege_target):
                file = file.replace("/", "\\")
                profile_name = file.split("\\")[-2]
                print(f"{index}. {profile_name}")

            option = int(input("Select a profile: "))
            if option >= len(siege_target) or option < 0:
                raise IndexError("WHAT IN THE WORLD IS THAT PROFILE!?!")
            else:
                return siege_target[option]
        else:
            return siege_target[0]

    def write_to_file(self):

        siege_target = glob.glob(self.cfg_path)
        profile_target = self.__siege_profiler(siege_target)

        with open(profile_target) as f:
            content = f.readlines()

        with open(profile_target + ".bak", 'w') as f:
            for x in content:
                f.write(x)

        BaseSensitivity._replace_singular_config("MouseYawSensitivity", "50", content)
        BaseSensitivity._replace_singular_config("MousePitchSensitivity", "50", content)
        BaseSensitivity._replace_singular_config("MouseSensitivityMultiplierUnit", str(self.__mouse_multiplier_unit),
                                                 content)
        BaseSensitivity._replace_singular_config("XFactorAiming", str(self.__x_factor_aiming), content)
        BaseSensitivity._replace_singular_config("AimDownSightsMouse", "100", content)
        BaseSensitivity._replace_singular_config("ADSMouseUseSpecific", "1", content)
        BaseSensitivity._replace_singular_config("ADSMouseMultiplierUnit", str(self.__x_factor_aiming), content)

        self.__y5s3_ads_mouse_specifics(content)

        with open(profile_target, 'w') as f:
            for x in content:
                f.write(x)

    def __repr__(self):
        vals = [self.__actual_sens, self.__mouse_multiplier_unit, self.__actual_ads_sens, self.__x_factor_aiming]
        return str(vals)

    def __y5s3_ads_mouse_specifics(self, content):
        """
        TODO: Check if it works as intended.
        :param content: list that contains the config values.
        """
        prefix = "ADSMouseSensitivity"
        scopes = ["Global", "1x", "1xHalf", "2x", "2xHalf", "3x", "4x", "12x"]
        ratios = [1, 0.67, 1, 1, 1, 1, 1, 1]
        for index, scope in enumerate(scopes):
            BaseSensitivity._replace_singular_config(f"{prefix}{scope}", str(ratios[index] * 100), content)
