from typing import List


class BaseSensitivity:
    """
    This class serves as an abstract template for any game's sensitivity. It defines 2 sensitivities; hipfire and ads.
    """

    def __init__(self, cfg_path=None, prev_impl=None):
        self.hipfire = 0
        self.ads = 0
        self.cfg_path = cfg_path

        if prev_impl is None and cfg_path is not None:
            self.read_from_config()
        else:
            self.read_from_base_sensitivity(prev_impl)

        if self.hipfire == 0 or self.ads == 0:
            raise EnvironmentError

    def read_from_base_sensitivity(self, __cls):
        """
        This is called when prev_impl is not None. This allows conversion from one type of sensitivity to another.
        It's the responsibility of the implementing class to fix this so conversion is easily possible.
        :param __cls: class we're getting the details from.
        """
        class_def: BaseSensitivity = __cls
        if class_def is None:
            raise EnvironmentError

        self.hipfire = class_def.hipfire
        self.ads = class_def.ads

    def write_to_file(self):
        """
        Provides a way to save the numbers calculated by Sens_sync.
        :return:
        """
        pass

    def read_from_config(self):
        """
        Provides a way to read data saved on drive by the game engine into Sens_sync.
        :return:
        """
        pass

    def __repr__(self):
        pass

    @staticmethod
    def _replace_singular_config(key, value, config_list: List[str], delimiter="="):
        """
        This is kinda slow way to do things but since game configs have very limited data and we have QUADCORE+ CPUS.
        We don't mind sacrificing a bit of performance for nice usability.
        :param key: key to find to change the value
        :param value: new value that replaces existing value
        :param config_list: lines read from the config
        :param delimiter: delimter between key and value
        """
        for index, item in enumerate(config_list):
            if item.startswith(key):
                config_list.remove(item)
                config_list.insert(index, f"{key}{delimiter}{value}\n")
