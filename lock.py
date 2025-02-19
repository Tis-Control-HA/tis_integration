from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)
J=decode__("bG9ja2Vk")
I=decode__("YWRtaW5fbG9jaw==")
A=property
G=decode__("SW52YWxpZCBwYXNzd29yZA==")
F=decode__("dXNlcg==")
E=ValueError
D=True
C=decode__("Y29kZQ==")
B=False
from homeassistant.components.lock import LockEntity as K
from homeassistant.core import HomeAssistant
from.const import DOMAIN
from TISControlProtocol.api import TISApi
import asyncio as H
async def async_setup_entry(hass,entry,async_add_devices):A=entry.runtime_data.api;async_add_devices([L(decode__("QWRtaW4gTG9jaw=="),decode__("MTIzNA=="))])
class L(K):
    def __init__(A,name,password):A._attr_name=name;A._attr_is_locked=D;A._attr_password=password;A._attr_changed_by=None;A._attr_code_format=decode__("Lio=");A._attr_is_locking=B;A._attr_is_unlocking=B;A._attr_is_opening=B;A._attr_is_open=B;A._attr_timeout=60
    @A
    def name(self):return self._attr_name
    @A
    def is_locked(self):return self._attr_is_locked
    async def async_lock(A,**B):
        if C in B and B[C]==A._attr_password:A._attr_is_locked=D;A._attr_changed_by=F;A.hass.bus.async_fire(str(I),{J:D})
        else:raise E(G)
    async def async_unlock(A,**D):
        if C in D and D[C]==A._attr_password:
            A._attr_is_locked=B;A._attr_changed_by=F;A.hass.bus.async_fire(str(I),{J:B})
            if hasattr(A,decode__("X2F1dG9fbG9ja190YXNr"))and A._auto_lock_task:A._auto_lock_task.cancel()
            A._auto_lock_task=H.create_task(A.auto_lock())
        else:raise E(G)
    async def auto_lock(A):await H.sleep(A._attr_timeout);await A.async_lock(code=A._attr_password)
    async def async_open(A,**B):
        if C in B and B[C]==A._attr_password:A._attr_is_open=D;A._attr_changed_by=F
        else:raise E(G)