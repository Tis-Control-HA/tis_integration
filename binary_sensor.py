from __future__ import annotations
from TISControlProtocol import *
_D=alpha__("cGFzc3dvcmQ=")
_C=False
_B=True
_A=None
from TISControlProtocol.api import TISApi
import asyncio
from homeassistant.components.binary_sensor import STATE_OFF,STATE_ON,BinarySensorEntity
from homeassistant.const import MATCH_ALL
from homeassistant.core import Event,HomeAssistant,callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_call_later
from.import TISConfigEntry
async def async_setup_entry(hass,entry,async_add_entities):
    A=entry.runtime_data.api;C=await A.get_entities(platform=alpha__("YmluYXJ5X3NlbnNvcg=="));D=await A.get_entities(platform=alpha__("cGFzc3dvcmRz"));B=[]
    if C:
        E=[(C,next(iter(A[alpha__("Y2hhbm5lbHM=")][0].values())),A[alpha__("ZGV2aWNlX2lk")],A[alpha__("Z2F0ZXdheQ==")],A[alpha__("aXNfcHJvdGVjdGVk")])for B in C for(C,A)in B.items()]
        for(F,G,H,I,J)in E:B.append(TISBinarySensor(tis_api=A,sensor_name=F,channel_number=G,device_id=H,gateway=I))
    if D:B.extend(TISPasswordSensor(tis_api=A,password_name=B.get(alpha__("dGl0bGU=")),password=B.get(_D))for B in D)
    async_add_entities(B)
class TISBinarySensor(BinarySensorEntity):
    def __init__(A,tis_api,sensor_name,channel_number,device_id,gateway):A._api=tis_api;A._name=sensor_name;A._device_id=device_id;A._channel_number=int(channel_number);A._listener=_A;A._attr_state=_A;A._attr_is_on=_A;A._attr_device_class=alpha__("bW90aW9u"),;A._gateway=gateway;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A._name, __var1=A._channel_number)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            C=alpha__("ZmVlZGJhY2tfdHlwZQ==");B=event
            if B.event_type==str(A._device_id):
                if B.data[C]==alpha__("YXV0b19iaW5hcnlfZmVlZGJhY2s="):
                    D=B.data[alpha__("Y2hhbm5lbHNfdmFsdWVz")][A._channel_number-1]
                    if int(D)==1:A._attr_is_on=_B;A._attr_state=STATE_ON
                    else:A._attr_is_on=_C;A._attr_state=STATE_OFF
                elif B.data[C]==alpha__("cmVhbHRpbWVfZmVlZGJhY2s="):
                    if B.data[alpha__("Y2hhbm5lbF9udW1iZXI=")]==A._channel_number:
                        E=int(B.data[alpha__("YWRkaXRpb25hbF9ieXRlcw==")][1])
                        if E==100:A._attr_is_on=_B;A._attr_state=STATE_ON
                        else:A._attr_is_on=_C;A._attr_state=STATE_OFF
            await A.async_update_ha_state(_B)
        A._listener=A.hass.bus.async_listen(MATCH_ALL,B)
    async def async_will_remove_from_hass(A):A._listener();A._listener=_A
    @property
    def name(self):return self._name
    @property
    def is_on(self):return self._attr_is_on
class TISPasswordSensor(BinarySensorEntity):
    def __init__(A,tis_api,password_name,password):A._api=tis_api;A._name=password_name;A._listener=_A;A._attr_state=_A;A._attr_is_on=_A;A._password=password;A._attr_unique_id=beta__("cGFzc3dvcmRfe19fdmFyMH0=", __var0=A._name)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==alpha__("cGFzc3dvcmRfZmVlZGJhY2s="):
                if B.data[_D]==A._password:A._attr_is_on=_B;A.async_write_ha_state();async_call_later(A.hass,1,A._turn_off_callback)
        A._listener=A.hass.bus.async_listen(MATCH_ALL,B)
    @callback
    async def _turn_off_callback(self,_now):self._attr_is_on=_C;await self.async_write_ha_state()
    async def async_will_remove_from_hass(A):A._listener();A._listener=_A
    @property
    def name(self):return self._name
    @property
    def is_on(self):return self._attr_is_on