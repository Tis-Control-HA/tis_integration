from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)
A=property
C=int
B=None
from TISControlProtocol.api import TISApi
from homeassistant.components.binary_sensor import STATE_OFF as E,STATE_ON as F,BinarySensorEntity as D
from homeassistant.const import MATCH_ALL as G
from homeassistant.core import Event,HomeAssistant,callback as H
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
async def async_setup_entry(hass,entry,async_add_entities):
    A=entry.runtime_data.api;B=await A.get_entities(platform=decode__("YmluYXJ5X3NlbnNvcg=="))
    if B:C=[(C,next(iter(A[decode__("Y2hhbm5lbHM=")][0].values())),A[decode__("ZGV2aWNlX2lk")],A[decode__("Z2F0ZXdheQ==")],A[decode__("aXNfcHJvdGVjdGVk")])for B in B for(C,A)in B.items()];D=[I(tis_api=A,sensor_name=B,channel_number=C,device_id=D,gateway=E)for(B,C,D,E,F)in C]
    async_add_entities(D)
class I(D):
    def __init__(A,tis_api,sensor_name,channel_number,device_id,gateway):A._api=tis_api;A._name=sensor_name;A._device_id=device_id;A._channel_number=C(channel_number);A._listener=B;A._attr_state=B;A._attr_is_on=B;A._attr_device_class=decode__("bW90aW9u"),;A._gateway=gateway;A._attr_unique_id=format_str__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A._name, __var1=A._channel_number)
    async def async_added_to_hass(A):
        @H
        async def B(event):
            H=False;G=decode__("ZmVlZGJhY2tfdHlwZQ==");D=True;B=event
            if B.event_type==str(A._device_id):
                if B.data[G]==decode__("YXV0b19iaW5hcnlfZmVlZGJhY2s="):
                    I=B.data[decode__("Y2hhbm5lbHNfdmFsdWVz")][A._channel_number-1]
                    if C(I)==1:A._attr_is_on=D;A._attr_state=F
                    else:A._attr_is_on=H;A._attr_state=E
                elif B.data[G]==decode__("cmVhbHRpbWVfZmVlZGJhY2s="):
                    if B.data[decode__("Y2hhbm5lbF9udW1iZXI=")]==A._channel_number:
                        J=C(B.data[decode__("YWRkaXRpb25hbF9ieXRlcw==")][1])
                        if J==100:A._attr_is_on=D;A._attr_state=F
                        else:A._attr_is_on=H;A._attr_state=E
            await A.async_update_ha_state(D)
        A._listener=A.hass.bus.async_listen(G,B)
    async def async_will_remove_from_hass(A):A._listener();A._listener=B
    @A
    def name(self):return self._name
    @A
    def is_on(self):return self._attr_is_on