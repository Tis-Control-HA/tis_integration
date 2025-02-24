from __future__ import annotations
from TISControlProtocol import *
W=True
V=alpha__("b2ZmbGluZV9kZXZpY2U=")
U=alpha__("dXBkYXRlX3Jlc3BvbnNl")
T=alpha__("Y29udHJvbF9yZXNwb25zZQ==")
S=KeyError
R=range
O=alpha__("Y2hhbm5lbF9udW1iZXI=")
N=tuple
M=False
K=str
H=alpha__("YWRkaXRpb25hbF9ieXRlcw==")
G=iter
F=next
E=alpha__("ZmVlZGJhY2tfdHlwZQ==")
A=property
C=None
B=int
import logging as D
from math import ceil
from typing import Any
from TISControlProtocol.api import TISApi
from TISControlProtocol.BytesHelper import int_to_8_bit_binary as Z
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler as a
from homeassistant.components.light import ATTR_BRIGHTNESS as X,ATTR_RGB_COLOR as b,ATTR_RGBW_COLOR as c,ColorMode as I,LightEntity as P,LightEntityFeature as Y
from homeassistant.const import STATE_OFF as d,STATE_ON as e,STATE_UNKNOWN as L
from homeassistant.core import Event,HomeAssistant,callback as Q
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
J=a()
async def async_setup_entry(hass,entry,async_add_devices):
    H=alpha__("Z2F0ZXdheQ==");E=alpha__("aXNfcHJvdGVjdGVk");D=alpha__("ZGV2aWNlX2lk");C=async_add_devices;B=alpha__("Y2hhbm5lbHM=");A=entry.runtime_data.api;I=await A.get_entities(platform=alpha__("ZGltbWVy"))
    if I:L=[(C,F(G(A[B][0].values())),A[D],A[E],A[H])for A in I for(C,A)in A.items()];M=[f(tis_api=A,light_name=B,device_id=D,channel_number=C,gateway=E)for(B,C,D,F,E)in L];C(M)
    J=await A.get_entities(platform=alpha__("cmdi"))
    if J:N=[(C,F(G(A[B][0].values())),F(G(A[B][1].values())),F(G(A[B][2].values())),A[D],A[E],A[H])for A in J for(C,A)in A.items()];O=[g(tis_api=A,light_name=B,r_channel=C,g_channel=D,b_channel=E,device_id=F,gateway=G)for(B,C,D,E,F,H,G)in N];C(O)
    K=await A.get_entities(platform=alpha__("cmdidw=="))
    if K:P=[(C,F(G(A[B][0].values())),F(G(A[B][1].values())),F(G(A[B][2].values())),F(G(A[B][3].values())),A[D],A[E],A[H])for A in K for(C,A)in A.items()];Q=[h(tis_api=A,light_name=B,r_channel=C,g_channel=D,b_channel=E,w_channel=F,device_id=G,gateway=H)for(B,C,D,E,F,G,I,H)in P];C(Q)
class f(P):
    def __init__(A,tis_api,gateway,light_name,channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.channel_number=B(channel_number);A._attr_name=light_name;A._attr_state=M;A._attr_brightness=C;A.listener=C;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A.name, __var1=A.channel_number);A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={I.BRIGHTNESS};A._attr_color_mode=I.BRIGHTNESS;A._attr_supported_features=Y.TRANSITION;A.generate_light_packet=J.generate_light_control_packet;A.update_packet=J.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @Q
        async def handle_event(event):
            C=event
            if C.event_type==K(A.device_id):
                if C.data[E]==T:
                    D.info(beta__("Y2hhbm5lbCBudW1iZXIgZm9yIGxpZ2h0OiB7X192YXIwfQ==", __var0=A.channel_number));F=C.data[H][2];G=C.data[O]
                    if B(G)==A.channel_number:A._attr_state=B(F)!=0;A._attr_brightness=B(F/100*255)
                    A.async_write_ha_state()
                elif C.data[E]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):
                    I=ceil(C.data[H][0]/8);J=alpha__("").join(Z(C.data[H][A])for A in R(1,I+1))
                    if J[A.channel_number-1]==alpha__("MA=="):A._attr_state=M
                    A.async_write_ha_state()
                elif C.data[E]==U:N=C.data[H];A._attr_brightness=B(N[A.channel_number]/100*255);A._attr_state=e if A._attr_brightness>0 else d
                elif C.data[E]==V:A._attr_state=L
        A.listener=A.hass.bus.async_listen(K(A.device_id),handle_event);C=await A.api.protocol.sender.send_packet(A.update_packet)
    @A
    def brightness(self):return self._attr_brightness
    @A
    def color_mode(self):return self._attr_color_mode
    @A
    def supported_color_modes(self):return self._attr_supported_color_modes
    @A
    def supported_features(self):return self._attr_supported_features
    @A
    def is_on(self):return self._attr_brightness>0 if self._attr_brightness is not C else C
    @A
    def name(self):return self._attr_name
    async def async_turn_on(A,**D):
        try:E=D[X]
        except S:E=255
        F=A.generate_light_packet(A,B(E/255*100));G=await A.api.protocol.sender.send_packet_with_ack(F)
        if G:A._attr_state=W;A._attr_brightness=D.get(X,255)
        else:A._attr_state=C;A._attr_brightness=C
        A.async_write_ha_state()
    async def async_turn_off(A,**E):
        B=A.generate_light_packet(A,0);D=await A.api.protocol.sender.send_packet_with_ack(B)
        if D:A._attr_brightness=0;A._attr_state=M
        else:A._attr_state=C;A._attr_brightness=C
        A.async_write_ha_state()
class g(P):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=B(r_channel);A.g_channel=B(g_channel);A.b_channel=B(b_channel);A.rgb_value_flags=[0,0,0];A._attr_name=light_name;A._attr_state=C;A._attr_rgb_color=C;A.listener=C;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM30=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel);A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={I.RGB};A._attr_color_mode=I.RGB;A.generate_rgb_packets=J.generate_rgb_light_control_packet;A.update_packet=J.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @Q
        async def handle_event(event):
            F=event
            if F.event_type==K(A.device_id):
                if F.data[E]==T:
                    G=F.data[H][2];D=F.data[O]
                    if B(D)==A.r_channel:A._attr_rgb_color=B(G/100*255),A._attr_rgb_color[1],A._attr_rgb_color[2];A.rgb_values_flag[0]=1
                    elif B(D)==A.g_channel:A._attr_rgb_color=A._attr_rgb_color[0],B(G/100*255),A._attr_rgb_color[2];A.rgb_values_flag[1]=1
                    elif B(D)==A.b_channel:A._attr_rgb_color=A._attr_rgb_color[0],A._attr_rgb_color[1],B(G/100*255);A.rgb_values_flag[2]=1
                    if A.rgb_values_flag==[1,1,1]:A.rgb_values_flag=[0,0,0];A.async_write_ha_state()
                elif F.data[E]==U:
                    I=F.data[H];D=F.data[O]
                    if A._attr_rgb_color is C:A._attr_rgb_color=[0,0,0]
                    if D==A.r_channel:A._attr_rgb_color[0]=B(I[D]/100*255)
                    elif D==A.g_channel:A._attr_rgb_color[1]=B(I[D]/100*255)
                    elif D==A.b_channel:A._attr_rgb_color[2]=B(I[D]/100*255)
                    A._attr_state=bool(A.r_channel or A.g_channel or A.b_channel)
                elif F.data[E]==V:A._attr_state=L
        A.listener=A.hass.bus.async_listen(K(A.device_id),handle_event)
        for D in R(5):
            if A._attr_rgb_color is C:F=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_rgb_color is C:A._attr_state=L;A._attr_rgb_color=0,0,0
    @A
    def color_mode(self):return self._attr_color_mode
    @A
    def rgb_color(self):return self._attr_rgb_color
    @A
    def supported_color_modes(self):return self._attr_supported_color_modes
    @A
    def is_on(self):return self._attr_state
    @A
    def name(self):return self._attr_name
    async def async_turn_on(A,**F):
        D.info(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=F))
        try:
            E=F[b];E=N([B(A/255*100)for A in E]);G,H,I=A.generate_rgb_packets(A,E);D.info(beta__("Y29sb3IgKHBlcmNlbnQpOiB7X192YXIwfQ==", __var0=E));C=await A.api.protocol.sender.send_packet_with_ack(G)
            if not C:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=C, __var1=A.r_channel))
            C=await A.api.protocol.sender.send_packet_with_ack(H)
            if not C:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=C, __var1=A.g_channel))
            C=await A.api.protocol.sender.send_packet_with_ack(I)
            if not C:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=C, __var1=A.b_channel))
            A._attr_state=W;E=N([B(A/100*255)for A in E]);A._attr_rgb_color=E
        except S as J:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=J))
        A.async_write_ha_state()
    async def async_turn_off(A,**F):C,D,E=A.generate_rgb_packets(A,(0,0,0));B=await A.api.protocol.sender.send_packet_with_ack(D);B=await A.api.protocol.sender.send_packet_with_ack(C);B=await A.api.protocol.sender.send_packet_with_ack(E);A._attr_state=M;A._attr_rgb_color=0,0,0;A.async_write_ha_state()
class h(P):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,w_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=B(r_channel);A.g_channel=B(g_channel);A.b_channel=B(b_channel);A.w_channel=B(w_channel);A._attr_name=light_name;A._attr_state=C;A._attr_brightness=C;A._attr_rgbw_color=C;A.rgbw_value_flags=[0,0,0,0];A.listener=C;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM31fe19fdmFyNH0=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel, __var4=A.w_channel);A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={I.RGBW};A._attr_color_mode=I.RGBW;A._attr_supported_features=Y.TRANSITION;A.generate_rgbw_packets=J.generate_rgbw_light_control_packet;A.update_packet=J.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @Q
        async def handle_event(event):
            C=event
            if C.event_type==K(A.device_id):
                if C.data[E]==T:
                    D=C.data[H][2];F=C.data[O]
                    if B(F)==A.r_channel:A._attr_rgbw_color=B(D/100*255),A._attr_rgbw_color[1],A._attr_rgbw_color[2],A._attr_rgbw_color[3];A.rgbw_value_flags[0]=1
                    elif B(F)==A.g_channel:A._attr_rgbw_color=A._attr_rgbw_color[0],B(D/100*255),A._attr_rgbw_color[2],A._attr_rgbw_color[3];A.rgbw_value_flags[1]=1
                    elif B(F)==A.b_channel:A._attr_rgbw_color=A._attr_rgbw_color[0],A._attr_rgbw_color[1],B(D/100*255),A._attr_rgbw_color[3];A.rgbw_value_flags[2]=1
                    elif B(F)==A.w_channel:A._attr_rgbw_color=A._attr_rgbw_color[0],A._attr_rgbw_color[1],A._attr_rgbw_color[2],B(D/100*255);A.rgbw_value_flags[3]=1
                    if A.rgbw_value_flags==[1,1,1,1]:A.async_write_ha_state()
                elif C.data[E]==U:G=C.data[H];I=G[A.r_channel]/100*255;J=G[A.g_channel]/100*255;M=G[A.b_channel]/100*255;N=G[A.w_channel]/100*255;A._attr_rgbw_color=I,J,M,N;A._attr_state=bool(I or J or M or N)
                elif C.data[E]==V:A._attr_state=L
        A.listener=A.hass.bus.async_listen(K(A.device_id),handle_event)
        for D in R(5):
            if A._attr_rgbw_color is C:F=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_rgbw_color is C:A._attr_state=L;A._attr_rgbw_color=0,0,0,0
    @A
    def brightness(self):return self._attr_brightness
    @A
    def color_mode(self):return self._attr_color_mode
    @A
    def rgbw_color(self):return self._attr_rgbw_color
    @A
    def supported_color_modes(self):return self._attr_supported_color_modes
    @A
    def supported_features(self):return self._attr_supported_features
    @A
    def is_on(self):return self._attr_state
    @A
    def name(self):return self._attr_name
    async def async_turn_on(A,**F):
        D.info(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=F))
        try:
            E=F[c];E=N([B(A/255*100)for A in E]);G,H,I,J=A.generate_rgbw_packets(A,E);D.info(beta__("Y29sb3IgKHBlcmNlbnQpOiB7X192YXIwfQ==", __var0=E));C=await A.api.protocol.sender.send_packet_with_ack(G)
            if not C:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=C, __var1=A.r_channel))
            C=await A.api.protocol.sender.send_packet_with_ack(H)
            if not C:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=C, __var1=A.g_channel))
            C=await A.api.protocol.sender.send_packet_with_ack(I)
            if not C:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=C, __var1=A.b_channel))
            C=await A.api.protocol.sender.send_packet_with_ack(J)
            if not C:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=C, __var1=A.w_channel))
            A._attr_state=W;E=N([B(A/100*255)for A in E]);A._attr_rgbw_color=E
        except S as K:D.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=K))
        A.async_write_ha_state()
    async def async_turn_off(A,**G):C,D,E,F=A.generate_rgbw_packets(A,(0,0,0,0));B=await A.api.protocol.sender.send_packet_with_ack(C);B=await A.api.protocol.sender.send_packet_with_ack(D);B=await A.api.protocol.sender.send_packet_with_ack(E);B=await A.api.protocol.sender.send_packet_with_ack(F);A._attr_state=M;A._attr_rgbw_color=0,0,0,0;A.async_write_ha_state()