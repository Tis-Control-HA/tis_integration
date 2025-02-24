from __future__ import annotations
from TISControlProtocol import *
U=alpha__("Y2hhbm5lbF9udW1iZXI=")
T=alpha__("Y29udHJvbF9yZXNwb25zZQ==")
P=iter
O=next
M=str
K=alpha__("YWRkaXRpb25hbF9ieXRlcw==")
J=alpha__("ZmVlZGJhY2tfdHlwZQ==")
H=int
F=False
A=property
D=True
B=None
import logging as C
from math import ceil
from typing import Any
from TISControlProtocol.api import TISApi
from TISControlProtocol.BytesHelper import int_to_8_bit_binary as V
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler as W
from homeassistant.components.cover import ATTR_POSITION as N,CoverDeviceClass as Q,CoverEntity as R,CoverEntityFeature as L
from homeassistant.const import STATE_CLOSING as G,STATE_OPENING as E,STATE_UNKNOWN as X,Platform
from homeassistant.core import Event,HomeAssistant,callback as S
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
I=W()
async def async_setup_entry(hass,entry,async_add_devices):
    J=alpha__("Z2F0ZXdheQ==");I=alpha__("ZGV2aWNlX2lk");F=async_add_devices;E=alpha__("Y2hhbm5lbHM=");A=entry.runtime_data.api;G=await A.get_entities(platform=alpha__("bW90b3I="));H=await A.get_entities(platform=alpha__("c2h1dHRlcg=="))
    if G:B=[(B,O(P(A[E][0].values())),A[I],A[J])for A in G for(B,A)in A.items()];C=[Y(tis_api=A,cover_name=B,channel_number=C,device_id=D,gateway=E)for(B,C,D,E)in B];F(C,update_before_add=D)
    if H:B=[(B,O(P(A[E][0].values())),O(P(A[E][1].values())),A[I],A[J])for A in H for(B,A)in A.items()];C=[Z(tis_api=A,cover_name=B,up_channel_number=C,down_channel_number=D,device_id=E,gateway=F)for(B,C,D,E,F)in B];F(C,update_before_add=D)
class Y(R):
    def __init__(A,tis_api,gateway,cover_name,channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.channel_number=H(channel_number);A._attr_name=cover_name;A._attr_is_closed=B;A._attr_current_cover_position=B;A._attr_device_class=Q.SHUTTER;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A._attr_name, __var1=A.channel_number);A.listener=B;A.update_packet=I.generate_control_update_packet(A);A.generate_cover_packet=I.generate_light_control_packet
    async def async_added_to_hass(A):
        @S
        async def handle_event(event):
            F=event
            if F.event_type==M(A.device_id):
                if F.data[J]==T:
                    C.info(beta__("Y2hhbm5lbCBudW1iZXIgZm9yIGNvdmVyOiB7X192YXIwfQ==", __var0=A.channel_number));I=F.data[K][2];L=F.data[U]
                    if H(L)==A.channel_number:A._attr_is_closed=I==0;A._attr_current_cover_position=I
                    A.async_write_ha_state()
                elif F.data[J]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):
                    N=ceil(F.data[K][0]/8);O=alpha__("").join(V(F.data[K][A])for A in range(1,N+1))
                    if O[A.channel_number-1]==alpha__("MA=="):A._attr_is_closed=D
                    A.async_write_ha_state()
                elif F.data[J]==alpha__("dXBkYXRlX3Jlc3BvbnNl"):P=F.data[K];A._attr_current_cover_position=P[A.channel_number];A._attr_is_closed=A._attr_current_cover_position==0;A._attr_state=G if A._attr_is_closed else E
                elif F.data[J]==alpha__("b2ZmbGluZV9kZXZpY2U="):A._attr_state=X;A._attr_is_closed=B;A._attr_current_cover_position=B
            await A.async_update_ha_state(D)
        A.listener=A.hass.bus.async_listen(M(A.device_id),handle_event);F=await A.api.protocol.sender.send_packet(A.update_packet)
    @A
    def name(self):return self._attr_name
    @A
    def is_closed(self):return self._attr_is_closed
    @A
    def supported_features(self):return L.SET_POSITION
    @A
    def current_cover_position(self):return self._attr_current_cover_position
    @A
    def unique_id(self):return self._attr_unique_id
    async def async_open_cover(A,**E):
        C=A.generate_cover_packet(A,100);D=await A.api.protocol.sender.send_packet_with_ack(C)
        if D:A._attr_is_closed=F;A._attr_current_cover_position=100
        else:A._attr_is_closed=B;A._attr_current_cover_position=B
        A.async_write_ha_state()
    async def async_close_cover(A,**G):
        C=A.generate_cover_packet(A,0);E=await A.api.protocol.sender.send_packet_with_ack(C)
        if E:A._attr_is_closed=D;A._attr_current_cover_position=0
        else:A._attr_is_closed=F;A._attr_current_cover_position=B
    async def async_set_cover_position(A,**C):
        D=A.generate_cover_packet(A,C[N]);E=await A.api.protocol.sender.send_packet_with_ack(D)
        if E:A._attr_is_closed=C[N]==0;A._attr_current_cover_position=C[N]
        else:A._attr_is_closed=B;A._attr_current_cover_position=B
class Z(R):
    def __init__(A,tis_api,gateway,cover_name,up_channel_number,down_channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.up_channel_number=H(up_channel_number);A.down_channel_number=H(down_channel_number);A._attr_name=cover_name;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn0=", __var0=A._attr_name, __var1=A.up_channel_number, __var2=A.down_channel_number);A.channel_number=A.up_channel_number;A._attr_is_closed=B;A._attr_device_class=Q.WINDOW;A.last_state=E;A.listener=B
    async def async_added_to_hass(A):
        @S
        async def handle_event(event):
            I=event
            if I.event_type==M(A.device_id):
                if I.data[J]==T:
                    B=I.data[K][2];L=I.data[U]
                    if H(L)==A.up_channel_number:
                        if B!=0:A._attr_is_closed=F;A.last_state=E;A._attr_state=E;C.warning(beta__("dXAgY2hhbm5lbCB2YWx1ZToge19fdmFyMH0gJ29wZW5pbmcn", __var0=B))
                        else:A._attr_is_closed=D;A.last_state=G;A._attr_state=G;C.warning(beta__("dXAgY2hhbm5lbCB2YWx1ZToge19fdmFyMH0gJ2Nsb3Npbmcn", __var0=B))
                    elif H(L)==A.down_channel_number:
                        if B!=0:A._attr_is_closed=D;A._attr_state=G;A.last_state=G;C.warning(beta__("ZG93biBjaGFubmVsIHZhbHVlOiB7X192YXIwfSAnY2xvc2luZyc=", __var0=B))
                        else:A._attr_is_closed=F;A._attr_state=E;A.last_state=E;C.warning(beta__("ZG93biBjaGFubmVsIHZhbHVlOiB7X192YXIwfSAnb3BlbmluZyc=", __var0=B))
                    else:C.warning(beta__("Y2hhbm5lbCBudW1iZXI6IHtfX3ZhcjB9ICdzdG9wcGluZyc=", __var0=L));A._attr_state=A.last_state;A._attr_is_closed=F if A.last_state==E else D
            await A.async_update_ha_state(D);A.schedule_update_ha_state()
        A.listener=A.hass.bus.async_listen(M(A.device_id),handle_event)
    @A
    def name(self):return self._attr_name
    @A
    def is_closed(self):0
    @A
    def supported_features(self):return L.OPEN|L.STOP|L.CLOSE
    @A
    def unique_id(self):return self._attr_unique_id
    async def async_open_cover(A,**H):
        D,J=I.generate_no_pos_cover_packet(A,alpha__("b3Blbg=="));G=await A.api.protocol.sender.send_packet_with_ack(D)
        if G:C.warning(alpha__("dXAgcGFja2V0IHNlbnQgJ29wZW5pbmcn"));A._attr_is_closed=F;A._attr_state=E;A.last_state=E
        else:C.warning(alpha__("dXAgcGFja2V0IG5vdCBzZW50ICdOb25lJw=="));A._attr_is_closed=B;A._attr_state=B
        A.async_write_ha_state()
    async def async_close_cover(A,**H):
        J,E=I.generate_no_pos_cover_packet(A,alpha__("Y2xvc2U="));F=await A.api.protocol.sender.send_packet_with_ack(E)
        if F:C.warning(alpha__("ZG93biBwYWNrZXQgc2VudCAnY2xvc2luZyc="));A._attr_is_closed=D;A._attr_state=G;A.last_state=G
        else:C.warning(alpha__("ZG93biBwYWNrZXQgbm90IHNlbnQgJ05vbmUn"));A._attr_is_closed=B;A._attr_state=B
        A.async_write_ha_state()
    async def async_stop_cover(A,**K):
        H,J=I.generate_no_pos_cover_packet(A,alpha__("c3RvcA=="))
        if A._attr_is_closed:
            G=await A.api.protocol.sender.send_packet_with_ack(J)
            if G:C.warning(alpha__("ZG93biBwYWNrZXQgc2VudCAnc3RvcHBpbmcn"));A._attr_state=A.last_state;A._attr_is_closed=F if A.last_state==E else D
            else:C.warning(alpha__("ZG93biBwYWNrZXQgbm90IHNlbnQgJ3N0b3BwaW5nJw=="));A._attr_state=B;A._attr_is_closed=B
        elif not A._attr_is_closed:
            G=await A.api.protocol.sender.send_packet_with_ack(H)
            if G:C.warning(alpha__("dXAgcGFja2V0IHNlbnQgJ3N0b3BwaW5nJw=="));A._attr_state=A.last_state;A._attr_is_closed=F if A.last_state==E else D
            else:C.warning(alpha__("dXAgcGFja2V0IG5vdCBzZW50ICdzdG9wcGluZyc="));A._attr_state=B;A._attr_is_closed=B
        A.async_write_ha_state()