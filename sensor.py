from __future__ import annotations
from TISControlProtocol import *
_D=alpha__("ZmVlZGJhY2tfdHlwZQ==")
_C=alpha__("bWRpOnRoZXJtb21ldGVy")
_B=alpha__("aGVhbHRoX3NlbnNvcg==")
_A=alpha__("dGVtcF9zZW5zb3I=")
from datetime import timedelta
import logging
from gpiozero import CPUTemperature
from TISControlProtocol.api import TISApi
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler
from homeassistant.components.sensor import SensorEntity,UnitOfTemperature
from homeassistant.core import Event,HomeAssistant,callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from.import TISConfigEntry
from.coordinator import SensorUpdateCoordinator
from.entities import BaseSensorEntity
class TempEntity:
    def __init__(A,device_id,api,gateway):A.device_id=device_id;A.api=api;A.gateway=gateway
async def async_setup_entry(hass,entry,async_add_devices):
    C=entry.runtime_data.api;A=[]
    for(D,E)in RELEVANT_TYPES.items():
        B=await C.get_entities(platform=D)
        if B and len(B)>0:F=[(C,next(iter(A[alpha__("Y2hhbm5lbHM=")][0].values())),A[alpha__("ZGV2aWNlX2lk")],A[alpha__("aXNfcHJvdGVjdGVk")],A[alpha__("Z2F0ZXdheQ==")])for B in B for(C,A)in B.items()];G=[E(hass=hass,tis_api=C,gateway=D,name=A,device_id=B)for(A,F,B,G,D)in F];A.extend(G)
    H=CPUTemperatureSensor(hass);A.append(H);async_add_devices(A)
def get_coordinator(hass,tis_api,device_id,gateway,coordinator_type):
    D=tis_api;B=coordinator_type;A=device_id;C=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=tuple(A), __var1=B)
    if C not in coordinators:
        logging.info(alpha__("Y3JlYXRpbmcgbmV3IGNvb3JkaW5hdG9y"));E=TempEntity(A,D,gateway)
        if B==_A:F=protocol_handler.generate_temp_sensor_update_packet(entity=E)
        elif B==_B:F=protocol_handler.generate_health_sensor_update_packet(entity=E)
        coordinators[C]=SensorUpdateCoordinator(hass,D,timedelta(seconds=30),A,F)
    return coordinators[C]
protocol_handler=TISProtocolHandler()
_LOGGER=logging.getLogger(__name__)
coordinators={}
class CoordinatedTemperatureSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id):B=device_id;C=get_coordinator(hass,tis_api,B,gateway,_A);super().__init__(C,name,B);A._attr_icon=_C;A.name=name;A.device_id=B
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_D]==alpha__("dGVtcF9mZWVkYmFjaw=="):A._state=B.data[alpha__("dGVtcA==")]
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgdGVtcGVyYXR1cmU6IHtfX3ZhcjB9", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
    @property
    def unit_of_measurement(self):return UnitOfTemperature.CELSIUS
class CoordinatedLUXSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id):B=device_id;C=get_coordinator(hass,tis_api,B,gateway,_B);super().__init__(C,name,B);A._attr_icon=alpha__("bWRpOmJyaWdodG5lc3MtNg==");A.name=name;A.device_id=B
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_D]==alpha__("aGVhbHRoX2ZlZWRiYWNr"):A._state=int(B.data[alpha__("bHV4")])
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgbHV4OiB7X192YXIwfQ==", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CPUTemperatureSensor(SensorEntity):
    def __init__(A,hass):A._cpu=CPUTemperature();A._state=A._cpu.temperature;A._hass=hass;A._attr_name=alpha__("Q1BVIFRlbXBlcmF0dXJlIFNlbnNvcg==");A._attr_icon=_C;A._attr_update_interval=timedelta(seconds=10);async_track_time_interval(A._hass,A.async_update,A._attr_update_interval)
    async def async_update(A,event_time):A._state=A._cpu.temperature;A.hass.bus.async_fire(alpha__("Y3B1X3RlbXBlcmF0dXJl"),{alpha__("dGVtcGVyYXR1cmU="):int(A._state)});A.async_write_ha_state()
    @property
    def should_poll(self):return False
    @property
    def state(self):return self._state
    @property
    def unit_of_measurement(self):return UnitOfTemperature.CELSIUS
    @property
    def name(self):return self._attr_name
RELEVANT_TYPES={alpha__("bHV4X3NlbnNvcg=="):CoordinatedLUXSensor,alpha__("dGVtcGVyYXR1cmVfc2Vuc29y"):CoordinatedTemperatureSensor}