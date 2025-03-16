from __future__ import annotations
from TISControlProtocol import *
_E=alpha__("bWRpOnRoZXJtb21ldGVy")
_D=alpha__("aGVhbHRoX3NlbnNvcg==")
_C=alpha__("dGVtcF9zZW5zb3I=")
_B=alpha__("ZmVlZGJhY2tfdHlwZQ==")
_A=alpha__("YW5hbG9nX3NlbnNvcg==")
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
        if B and len(B)>0:F=[(C,next(iter(A[alpha__("Y2hhbm5lbHM=")][0].values())),A[alpha__("ZGV2aWNlX2lk")],A[alpha__("aXNfcHJvdGVjdGVk")],A[alpha__("Z2F0ZXdheQ==")])for B in B for(C,A)in B.items()];G=[E(hass=hass,tis_api=C,gateway=F,name=A,device_id=D,channel_number=B)for(A,B,D,G,F)in F];A.extend(G)
    H=CPUTemperatureSensor(hass);A.append(H);async_add_devices(A)
def get_coordinator(hass,tis_api,device_id,gateway,coordinator_type):
    F=tis_api;B=device_id;A=coordinator_type;C=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=tuple(B), __var1=A)
    if C not in coordinators:
        logging.info(alpha__("Y3JlYXRpbmcgbmV3IGNvb3JkaW5hdG9y"));D=TempEntity(B,F,gateway)
        if A==_C:E=protocol_handler.generate_temp_sensor_update_packet(entity=D)
        elif A==_D:E=protocol_handler.generate_health_sensor_update_packet(entity=D)
        elif A==_A:E=protocol_handler.generate_update_analog_packet(entity=D)
        coordinators[C]=SensorUpdateCoordinator(hass,F,timedelta(seconds=30),B,E)
    return coordinators[C]
protocol_handler=TISProtocolHandler()
_LOGGER=logging.getLogger(__name__)
coordinators={}
class CoordinatedTemperatureSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):B=device_id;C=get_coordinator(hass,tis_api,B,gateway,_C);super().__init__(C,name,B);A._attr_icon=_E;A.name=name;A.device_id=B;A.channel_number=channel_number
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_B]==alpha__("dGVtcF9mZWVkYmFjaw=="):A._state=B.data[alpha__("dGVtcA==")]
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgdGVtcGVyYXR1cmU6IHtfX3ZhcjB9", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
    @property
    def unit_of_measurement(self):return UnitOfTemperature.CELSIUS
class CoordinatedLUXSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):B=device_id;C=get_coordinator(hass,tis_api,B,gateway,_D);super().__init__(C,name,B);A._attr_icon=alpha__("bWRpOmJyaWdodG5lc3MtNg==");A.name=name;A.device_id=B;A.channel_number=channel_number
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_B]==alpha__("aGVhbHRoX2ZlZWRiYWNr"):A._state=int(B.data[alpha__("bHV4")])
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgbHV4OiB7X192YXIwfQ==", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CoordinatedAnalogSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):B=device_id;C=get_coordinator(hass,tis_api,B,gateway,_A);super().__init__(C,name,B);A._attr_icon=alpha__("bWRpOmN1cnJlbnQtYWM=");A.name=name;A.device_id=B;A.channel_number=channel_number
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_B]==alpha__("YW5hbG9nX2ZlZWRiYWNr"):A._state=int(B.data[alpha__("YW5hbG9n")][A.channel_number-1])
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgYW5hbG9nIHNlbnNvcjoge19fdmFyMH0=", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CPUTemperatureSensor(SensorEntity):
    def __init__(A,hass):A._cpu=CPUTemperature();A._state=A._cpu.temperature;A._hass=hass;A._attr_name=alpha__("Q1BVIFRlbXBlcmF0dXJlIFNlbnNvcg==");A._attr_icon=_E;A._attr_update_interval=timedelta(seconds=10);async_track_time_interval(A._hass,A.async_update,A._attr_update_interval)
    async def async_update(A,event_time):A._state=A._cpu.temperature;A.hass.bus.async_fire(alpha__("Y3B1X3RlbXBlcmF0dXJl"),{alpha__("dGVtcGVyYXR1cmU="):int(A._state)});A.async_write_ha_state()
    @property
    def should_poll(self):return False
    @property
    def state(self):return self._state
    @property
    def unit_of_measurement(self):return UnitOfTemperature.CELSIUS
    @property
    def name(self):return self._attr_name
RELEVANT_TYPES={alpha__("bHV4X3NlbnNvcg=="):CoordinatedLUXSensor,alpha__("dGVtcGVyYXR1cmVfc2Vuc29y"):CoordinatedTemperatureSensor,_A:CoordinatedAnalogSensor}