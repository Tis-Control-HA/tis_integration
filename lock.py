from __future__ import annotations
from TISControlProtocol import *
K=alpha__("bG9ja2Vk")
J=alpha__("YWRtaW5fbG9jaw==")
A=property
H=alpha__("SW52YWxpZCBwYXNzd29yZA==")
G=alpha__("dXNlcg==")
F=None
E=ValueError
D=True
C=alpha__("Y29kZQ==")
B=False
from homeassistant.components.lock import LockEntity as L
from homeassistant.core import HomeAssistant
from.const import DOMAIN
from TISControlProtocol.api import TISApi
import asyncio as I,logging as M
async def async_setup_entry(hass,entry,async_add_devices):
    B=entry.runtime_data.api;A=B.config_entries.get(alpha__("bG9ja19tb2R1bGU="),F)
    if A is F:M.error(alpha__("Tm8gbG9jayBtb2R1bGUgZm91bmQgaW4gdGhlIGNvbmZpZ3VyYXRpb24="));return
    else:async_add_devices([N(alpha__("QWRtaW4gTG9jaw=="),A[alpha__("cGFzc3dvcmQ=")])])
class N(L):
    def __init__(A,name,password):A._attr_name=name;A.unique_id=beta__("bG9ja197X192YXIwfQ==", __var0=A.name);A._attr_is_locked=D;A._attr_password=password;A._attr_changed_by=F;A._attr_code_format=alpha__("Lio=");A._attr_is_locking=B;A._attr_is_unlocking=B;A._attr_is_opening=B;A._attr_is_open=B;A._attr_timeout=60
    @A
    def name(self):return self._attr_name
    @A
    def is_locked(self):return self._attr_is_locked
    async def async_lock(A,**B):
        if C in B and B[C]==A._attr_password:A._attr_is_locked=D;A._attr_changed_by=G;A.hass.bus.async_fire(str(J),{K:D})
        else:raise E(H)
    async def async_unlock(A,**D):
        if C in D and D[C]==A._attr_password:
            A._attr_is_locked=B;A._attr_changed_by=G;A.hass.bus.async_fire(str(J),{K:B})
            if hasattr(A,alpha__("X2F1dG9fbG9ja190YXNr"))and A._auto_lock_task:A._auto_lock_task.cancel()
            A._auto_lock_task=I.create_task(A.auto_lock())
        else:raise E(H)
    async def auto_lock(A):await I.sleep(A._attr_timeout);await A.async_lock(code=A._attr_password)
    async def async_open(A,**B):
        if C in B and B[C]==A._attr_password:A._attr_is_open=D;A._attr_changed_by=G
        else:raise E(H)