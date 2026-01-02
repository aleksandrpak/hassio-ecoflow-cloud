from ..internal.delta3_plus import Delta3Plus as InternalDelta3Plus
from ...api import EcoflowApiClient
from ...sensor import StatusSensorEntity


class Delta3Plus(InternalDelta3Plus):
    """
    EcoFlow Delta 3 Plus public API implementation.

    Wraps the internal Delta 3 Plus (which inherits from Delta 3) for use with the public cloud API.
    Note: Public API is not available for Delta 3 Plus, but this wrapper is provided for completeness.
    """

    def _status_sensor(self, client: EcoflowApiClient) -> StatusSensorEntity:
        return StatusSensorEntity(client, self)
