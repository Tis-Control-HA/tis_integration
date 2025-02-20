from __future__ import annotations
from TISControlProtocol import *
from datetime import timedelta
import logging as A
from TISControlProtocol.api import TISApi
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler as B
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as C
D=A.getLogger(__name__)
E=B()
class SensorUpdateCoordinator(C):
    def __init__(A,hass,api,update_interval,device_id,update_packet):B=device_id;A.api=api;A.device_id=B;A.update_packet=update_packet;super().__init__(hass,D,name=beta__("U2Vuc29yIFVwZGF0ZSBDb29yZGluYXRvciBmb3Ige19fdmFyMH0=", __var0=B),update_interval=update_interval)
    async def _async_update_data(A):return await A.api.protocol.sender.send_packet(A.update_packet)