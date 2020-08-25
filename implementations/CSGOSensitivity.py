import glob

from implementations.interface.BaseSensitivity import BaseSensitivity


class CSGOSensitivity(BaseSensitivity):
    """
    This class is an implementation of BaseSensitivity. CSGO has a nice standarized engine so we use it's sensitivity as
    base pretty much.
    """

    def __init__(self, cfg_path='C:/Program Files (x86)/Steam/userdata/*/730/local/cfg/config.cfg', prev_impl=None):
        super(CSGOSensitivity, self).__init__(cfg_path, prev_impl)

    def read_from_config(self):
        """
        We keep CSGO as our base sensitivity hence the BaseSensitivity and CS:GO Sensitivity are 1:1 in 360/cm.
        """
        cs_target = glob.glob(self.cfg_path)

        with open(cs_target[0]) as f:
            content = f.readlines()

        hipfire = 0
        awp = 0

        for x in content:
            if x.startswith("sensitivity \""):
                hipfire = float(x.split("\"")[1])
            if "zoom_sensitivity_ratio_mouse" in x:
                awp = float(x.split("\"")[1])

        self.hipfire = hipfire
        self.ads = awp

    def read_from_base_sensitivity(self, __cls: BaseSensitivity):
        self.hipfire = __cls.hipfire
        self.ads = __cls.ads

    def write_to_file(self):
        cs_target = glob.glob(self.cfg_path)[0]
        with open(cs_target) as f:
            content = f.readlines()

        with open(cs_target + ".bak", 'w') as f:
            for x in content:
                f.write(x)

        # H4X TO MAKE IT COMPLIANT
        BaseSensitivity._replace_singular_config("sensitivity \"", str(self.hipfire) + "\"", content, delimiter="")
        BaseSensitivity._replace_singular_config("zoom_sensitivity_ratio_mouse \"", str(self.ads) + "\"", content,
                                                 delimiter="")
        with open(cs_target, 'w') as f:
            for x in content:
                f.write(x)

    def __repr__(self):
        return str([self.hipfire, self.ads])
