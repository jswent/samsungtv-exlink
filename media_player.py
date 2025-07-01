from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.components.media_player.const import (
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from homeassistant.helpers.device_registry import DeviceInfo
from .samsungtv import SamsungExLinkTV
from .const import DOMAIN


async def async_setup_entry(hass, config_entry, async_add_entities):
    data = config_entry.data
    tv = SamsungExLinkTV(data["host"], data.get("port", 23))
    async_add_entities([SamsungExLinkEntity(tv, data["name"], config_entry.entry_id)])


class SamsungExLinkEntity(MediaPlayerEntity):
    def __init__(self, tv: SamsungExLinkTV, name: str, entry_id: str):
        self._tv = tv
        self._attr_name = name
        self._attr_supported_features = (
            MediaPlayerEntityFeature.TURN_ON
            | MediaPlayerEntityFeature.TURN_OFF
            | MediaPlayerEntityFeature.VOLUME_STEP
            | MediaPlayerEntityFeature.SELECT_SOURCE
        )
        self._attr_state = MediaPlayerState.OFF
        self._attr_source_list = ["HDMI 1", "HDMI 2", "HDMI 3", "HDMI 4"]
        self._attr_source = None
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry_id)},
            name=name,
            manufacturer="Samsung",
            model="Ex-Link TV",
        )

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

    def select_source(self, source):
        source_map = {
            "HDMI 1": 1,
            "HDMI 2": 2,
            "HDMI 3": 3,
            "HDMI 4": 4,
        }
        if source in source_map:
            self._tv.select_hdmi(source_map[source])
            self._attr_source = source
            self.schedule_update_ha_state()
