from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)
N=decode__("ZmVlZGJhY2tfdHlwZQ==")
M=decode__("bWRpOnRoZXJtb21ldGVy")
L=decode__("aGVhbHRoX3NlbnNvcg==")
K=decode__("dGVtcF9zZW5zb3I=")
J=Exception
A=property
from datetime import timedelta as F
import logging as B
from gpiozero import CPUTemperature as O
from TISControlProtocol.api import TISApi
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler as P
from homeassistant.components.sensor import SensorEntity as C,UnitOfTemperature as E
from homeassistant.core import Event,HomeAssistant,callback as G
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as Q
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from.import TISConfigEntry
from.coordinator import SensorUpdateCoordinator
from.entities import BaseSensorEntity
class R:
    def __init__(A,device_id,api,gateway):A.device_id=device_id;A.api=api;A.gateway=gateway
async def async_setup_entry(hass,entry,async_add_devices):
    C=entry.runtime_data.api;A=[]
    for(D,E)in V.items():
        B=await C.get_entities(platform=D)
        if B and len(B)>0:F=[(C,next(iter(A[decode__("Y2hhbm5lbHM=")][0].values())),A[decode__("ZGV2aWNlX2lk")],A[decode__("aXNfcHJvdGVjdGVk")],A[decode__("Z2F0ZXdheQ==")])for B in B for(C,A)in B.items()];G=[E(hass=hass,tis_api=C,gateway=D,name=A,device_id=B)for(A,F,B,G,D)in F];A.extend(G)
    H=U(hass);A.append(H);async_add_devices(A)
def H(hass,tis_api,device_id,gateway,coordinator_type):
    G=tis_api;C=coordinator_type;A=device_id;E=format_str__("e19fdmFyMH1fe19fdmFyMX0=", __var0=tuple(A), __var1=C)
    if E not in D:
        B.info(decode__("Y3JlYXRpbmcgbmV3IGNvb3JkaW5hdG9y"));H=R(A,G,gateway)
        if C==K:J=I.generate_temp_sensor_update_packet(entity=H)
        elif C==L:J=I.generate_health_sensor_update_packet(entity=H)
        D[E]=SensorUpdateCoordinator(hass,G,F(seconds=30),A,J)
    return D[E]
I=P()
W=B.getLogger(__name__)
D={}
class S(BaseSensorEntity,C):
    def __init__(A,hass,tis_api,gateway,name,device_id):B=device_id;C=H(hass,tis_api,B,gateway,K);super().__init__(C,name,B);A._attr_icon=M;A.name=name;A.device_id=B
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @G
        def C(event):
            C=event
            try:
                if C.data[N]==decode__("dGVtcF9mZWVkYmFjaw=="):A._state=C.data[decode__("dGVtcA==")]
                A.async_write_ha_state()
            except J as D:B.error(format_str__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgdGVtcGVyYXR1cmU6IHtfX3ZhcjB9", __var0=C.data))
        A.hass.bus.async_listen(str(A.device_id),C)
    def _update_state(A,data):0
    @A
    def unit_of_measurement(self):return E.CELSIUS
class T(BaseSensorEntity,C):
    def __init__(A,hass,tis_api,gateway,name,device_id):B=device_id;C=H(hass,tis_api,B,gateway,L);super().__init__(C,name,B);A._attr_icon=decode__("bWRpOmJyaWdodG5lc3MtNg==");A.name=name;A.device_id=B
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @G
        def C(event):
            C=event
            try:
                if C.data[N]==decode__("aGVhbHRoX2ZlZWRiYWNr"):A._state=int(C.data[decode__("bHV4")])
                A.async_write_ha_state()
            except J as D:B.error(format_str__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgbHV4OiB7X192YXIwfQ==", __var0=C.data))
        A.hass.bus.async_listen(str(A.device_id),C)
    def _update_state(A,data):0
class U(C):
    def __init__(A,hass):A._cpu=O();A._state=A._cpu.temperature;A._hass=hass;A._attr_name=decode__("Q1BVIFRlbXBlcmF0dXJlIFNlbnNvcg==");A._attr_icon=M;A._attr_update_interval=F(seconds=10);Q(A._hass,A.async_update,A._attr_update_interval)
    async def async_update(A,event_time):A._state=A._cpu.temperature;A.hass.bus.async_fire(decode__("Y3B1X3RlbXBlcmF0dXJl"),{decode__("dGVtcGVyYXR1cmU="):int(A._state)});A.async_write_ha_state()
    @A
    def should_poll(self):return False
    @A
    def state(self):return self._state
    @A
    def unit_of_measurement(self):return E.CELSIUS
    @A
    def name(self):return self._attr_name
V={decode__("bHV4X3NlbnNvcg=="):T,decode__("dGVtcGVyYXR1cmVfc2Vuc29y"):S}