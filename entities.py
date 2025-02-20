from __future__ import annotations
from TISControlProtocol import *
A=property
from homeassistant.core import callback as B
from homeassistant.helpers.update_coordinator import CoordinatorEntity as C,DataUpdateCoordinator
class BaseSensorEntity(C):
    def __init__(A,coordinator,name,device_id):B=coordinator;super().__init__(B);A.coordinator=B;A._attr_name=name;A._state=None;A._device_id=device_id
    async def async_added_to_hass(A):await super().async_added_to_hass();A.async_on_remove(A.coordinator.async_add_listener(A._handle_coordinator_update))
    @B
    def _handle_coordinator_update(self):A=self;A._update_state(A.coordinator.data);A.async_write_ha_state()
    def _update_state(A,data):raise NotImplementedError
    @A
    def should_poll(self):return False
    @A
    def state(self):return self._state