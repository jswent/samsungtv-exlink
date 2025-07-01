from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.components.media_player.const import (
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from .samsungtv import SamsungExLinkTV


async def async_setup_entry(hass, config_entry, async_add_entities):
    data = config_entry.data
    tv = SamsungExLinkTV(data["host"], data.get("port", 23))
    async_add_entities([SamsungExLinkEntity(tv, data["name"])])


class SamsungExLinkEntity(MediaPlayerEntity):
    def __init__(self, tv: SamsungExLinkTV, name: str):
        self._tv = tv
        self._attr_name = name
        self._attr_supported_features = (
            MediaPlayerEntityFeature.TURN_ON
            | MediaPlayerEntityFeature.TURN_OFF
            | MediaPlayerEntityFeature.VOLUME_STEP
        )
        self._attr_state = MediaPlayerState.OFF

    def turn_on(self):
        self._tv.power_on()
        self._attr_state = MediaPlayerState.ON
        self.schedule_update_ha_state()

    def turn_off(self):
        self._tv.power_off()
        self._attr_state = MediaPlayerState.OFF
        self.schedule_update_ha_state()

    def volume_up(self):
        self._tv.volume_up()

    def volume_down(self):
        self._tv.volume_down()

    def mute_volume(self, mute):
        self._tv.mute()
