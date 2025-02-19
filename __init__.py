from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)
I=False
import logging as D,os as C
from attr import dataclass as B
from TISControlProtocol.api import TISApi as G,GetKeyEndpoint as K,ScanDevicesEndPoint as L,TISEndPoint as M
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler as E
from homeassistant.config_entries import ConfigEntry as F
from homeassistant.const import Platform as A
from homeassistant.core import HomeAssistant
from.const import DEVICES_DICT,DOMAIN
@B
class H:api:G
PLATFORMS=[A.LIGHT,A.SENSOR,A.BINARY_SENSOR,A.SWITCH,A.COVER,A.CLIMATE,A.SELECT,A.LOCK,A.FAN]
type TISConfigEntry=F[H]
J=E()
async def async_setup_entry(hass,entry):
    E=entry;A=hass
    try:
        N=C.getcwd();C.chdir(decode__("L2NvbmZpZy9jdXN0b21fY29tcG9uZW50cy90aXNfaW50ZWdyYXRpb24="));O=C.system(decode__("Z2l0IHJlc2V0IC0taGFyZCBIRUFE"));J=C.system(decode__("Z2l0IHB1bGw="));C.chdir(N)
        if J==0 and O==0:D.warning(format_str__("VXBkYXRlZCBUSVMgSW50ZWdyYXRpb25z", ))
        else:D.warning(format_str__("Q291bGQgTm90IFVwZGF0ZSBUSVMgSW50ZWdyYXRpb246IGV4aXQgZXJyb3Ige19fdmFyMH0=", __var0=J))
    except Exception as F:D.error(format_str__("Q291bGQgTm90IFVwZGF0ZSBUSVMgSW50ZWdyYXRpb246IHtfX3ZhcjB9", __var0=F))
    B=G(port=int(E.data[decode__("cG9ydA==")]),hass=A,domain=DOMAIN,devices_dict=DEVICES_DICT,display_logo=decode__("Li9jdXN0b21fY29tcG9uZW50cy90aXNfaW50ZWdyYXRpb24vaW1hZ2VzL2xvZ28ucG5n"));E.runtime_data=H(api=B);A.data.setdefault(DOMAIN,{decode__("c3VwcG9ydGVkX3BsYXRmb3Jtcw=="):PLATFORMS})
    try:await B.connect();A.http.register_view(M(B));A.http.register_view(L(B));A.http.register_view(K(B));A.async_add_executor_job(B.run_display)
    except ConnectionError as F:D.error(decode__("ZXJyb3IgY29ubmVjdGluZyB0byBUSVMgYXBpICVz"),F);return I
    await A.config_entries.async_forward_entry_setups(E,PLATFORMS);return True
async def async_unload_entry(hass,entry):
    if(A:=await hass.config_entries.async_unload_platforms(entry,PLATFORMS)):return A
    return I