from custom_components.ecoflow_cloud.devices.internal.delta3 import Delta3


class Delta3Plus(Delta3):
    """
    EcoFlow Delta 3 Plus device implementation.

    Delta 3 Plus is essentially a Delta 3 with double the battery capacity (2048Wh vs 1024Wh).
    It uses the same protobuf message format and all the same sensor keys.
    Therefore, it can directly inherit from Delta3 without any modifications.
    """

    pass
