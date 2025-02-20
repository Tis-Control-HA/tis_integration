from __future__ import annotations
from TISControlProtocol import *
T=alpha__("Y2hhbm5lbF9udW1iZXI=")
S=alpha__("Y29udHJvbF9yZXNwb25zZQ==")
O=iter
N=next
K=str
I=alpha__("YWRkaXRpb25hbF9ieXRlcw==")
H=alpha__("ZmVlZGJhY2tfdHlwZQ==")
F=int
D=False
A=property
C=True
B=None
import logging as U
from math import ceil
from typing import Any
from TISControlProtocol.api import TISApi
from TISControlProtocol.BytesHelper import int_to_8_bit_binary as V
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler as W
from homeassistant.components.cover import ATTR_POSITION as L,CoverDeviceClass as P,CoverEntity as Q,CoverEntityFeature as J
from homeassistant.const import STATE_CLOSING as M,STATE_OPENING as E,STATE_UNKNOWN as X,Platform
from homeassistant.core import Event,HomeAssistant,callback as R
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
G=W()
async def async_setup_entry(hass,entry,async_add_devices):
    J=alpha__("Z2F0ZXdheQ==");I=alpha__("ZGV2aWNlX2lk");F=async_add_devices;E=alpha__("Y2hhbm5lbHM=");A=entry.runtime_data.api;G=await A.get_entities(platform=alpha__("bW90b3I="));H=await A.get_entities(platform=alpha__("c2h1dHRlcg=="))
    if G:B=[(B,N(O(A[E][0].values())),A[I],A[J])for A in G for(B,A)in A.items()];D=[Y(tis_api=A,cover_name=B,channel_number=C,device_id=D,gateway=E)for(B,C,D,E)in B];F(D,update_before_add=C)
    if H:B=[(B,N(O(A[E][0].values())),N(O(A[E][1].values())),A[I],A[J])for A in H for(B,A)in A.items()];D=[Z(tis_api=A,cover_name=B,up_channel_number=C,down_channel_number=D,device_id=E,gateway=F)for(B,C,D,E,F)in B];F(D,update_before_add=C)
class Y(Q):
    def __init__(A,tis_api,gateway,cover_name,channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.channel_number=F(channel_number);A._attr_name=cover_name;A._attr_is_closed=B;A._attr_current_cover_position=B;A._attr_device_class=P.SHUTTER;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A._attr_name, __var1=A.channel_number);A.listener=B;A.update_packet=G.generate_control_update_packet(A);A.generate_cover_packet=G.generate_light_control_packet
    async def async_added_to_hass(A):
        @R
        async def D(event):
            D=event
            if D.event_type==K(A.device_id):
                if D.data[H]==S:
                    U.info(beta__("Y2hhbm5lbCBudW1iZXIgZm9yIGNvdmVyOiB7X192YXIwfQ==", __var0=A.channel_number));G=D.data[I][2];J=D.data[T]
                    if F(J)==A.channel_number:A._attr_is_closed=G==0;A._attr_current_cover_position=G
                    A.async_write_ha_state()
                elif D.data[H]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):
                    L=ceil(D.data[I][0]/8);N=alpha__("").join(V(D.data[I][A])for A in range(1,L+1))
                    if N[A.channel_number-1]==alpha__("MA=="):A._attr_is_closed=C
                    A.async_write_ha_state()
                elif D.data[H]==alpha__("dXBkYXRlX3Jlc3BvbnNl"):O=D.data[I];A._attr_current_cover_position=O[A.channel_number];A._attr_is_closed=A._attr_current_cover_position==0;A._attr_state=M if A._attr_is_closed else E
                elif D.data[H]==alpha__("b2ZmbGluZV9kZXZpY2U="):A._attr_state=X;A._attr_is_closed=B;A._attr_current_cover_position=B
            await A.async_update_ha_state(C)
        A.listener=A.hass.bus.async_listen(K(A.device_id),D);G=await A.api.protocol.sender.send_packet(A.update_packet)
    @A
    def name(self):return self._attr_name
    @A
    def is_closed(self):return self._attr_is_closed
    @A
    def supported_features(self):return J.SET_POSITION
    @A
    def current_cover_position(self):return self._attr_current_cover_position
    @A
    def unique_id(self):return self._attr_unique_id
    async def async_open_cover(A,**F):
        C=A.generate_cover_packet(A,100);E=await A.api.protocol.sender.send_packet_with_ack(C)
        if E:A._attr_is_closed=D;A._attr_current_cover_position=100
        else:A._attr_is_closed=B;A._attr_current_cover_position=B
        A.async_write_ha_state()
    async def async_close_cover(A,**G):
        E=A.generate_cover_packet(A,0);F=await A.api.protocol.sender.send_packet_with_ack(E)
        if F:A._attr_is_closed=C;A._attr_current_cover_position=0
        else:A._attr_is_closed=D;A._attr_current_cover_position=B
    async def async_set_cover_position(A,**C):
        D=A.generate_cover_packet(A,C[L]);E=await A.api.protocol.sender.send_packet_with_ack(D)
        if E:A._attr_is_closed=C[L]==0;A._attr_current_cover_position=C[L]
        else:A._attr_is_closed=B;A._attr_current_cover_position=B
class Z(Q):
    def __init__(A,tis_api,gateway,cover_name,up_channel_number,down_channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.up_channel_number=F(up_channel_number);A.down_channel_number=F(down_channel_number);A._attr_name=cover_name;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn0=", __var0=A._attr_name, __var1=A.up_channel_number, __var2=A.down_channel_number);A.channel_number=A.up_channel_number;A._attr_is_closed=B;A._attr_device_class=P.WINDOW;A.last_status=E;A.listener=B
    async def async_added_to_hass(A):
        @R
        async def B(event):
            B=event
            if B.event_type==K(A.device_id):
                if B.data[H]==S:
                    G=B.data[I][2];J=B.data[T]
                    if F(J)==A.up_channel_number:
                        if G!=0:A._attr_is_closed=D;A.last_status=E
                    elif F(J)==A.down_channel_number:
                        if G!=0:A._attr_is_closed=C;A.last_status=M
                    else:A._attr_is_closed=D if A.last_status==E else C
            await A.async_update_ha_state(C);A.schedule_update_ha_state()
        A.listener=A.hass.bus.async_listen(K(A.device_id),B)
    @A
    def name(self):return self._attr_name
    @A
    def is_closed(self):0
    @A
    def supported_features(self):return J.OPEN|J.STOP|J.CLOSE
    @A
    def unique_id(self):return self._attr_unique_id
    async def async_open_cover(A,**H):
        C,I=G.generate_no_pos_cover_packet(A,alpha__("b3Blbg=="));F=await A.api.protocol.sender.send_packet_with_ack(C)
        if F:A._attr_is_closed=D;A.last_status=E
        else:A._attr_is_closed=B
        A.async_write_ha_state()
    async def async_close_cover(A,**F):
        H,D=G.generate_no_pos_cover_packet(A,alpha__("Y2xvc2U="));E=await A.api.protocol.sender.send_packet_with_ack(D)
        if E:A._attr_is_closed=C;A.last_status=M
        else:A._attr_is_closed=B
        A.async_write_ha_state()
    async def async_stop_cover(A,**J):
        H,I=G.generate_no_pos_cover_packet(A,alpha__("c3RvcA=="))
        if A._attr_is_closed:
            F=await A.api.protocol.sender.send_packet_with_ack(I)
            if F:A._attr_state=A.last_status;A._attr_is_closed=D if A.last_status==E else C
            else:A._attr_state=B;A._attr_is_closed=B
        elif not A._attr_is_closed:
            F=await A.api.protocol.sender.send_packet_with_ack(H)
            if F:A._attr_state=A.last_status;A._attr_is_closed=D if A.last_status==E else C
            else:A._attr_state=B;A._attr_is_closed=B
        A.async_write_ha_state()