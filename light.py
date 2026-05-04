from __future__ import annotations
from TISControlProtocol import *
_H=alpha__("Y2hhbm5lbF9udW1iZXI=")
_G=alpha__("b2ZmbGluZV9kZXZpY2U=")
_F=alpha__("dXBkYXRlX3Jlc3BvbnNl")
_E=False
_D=True
_C=alpha__("YWRkaXRpb25hbF9ieXRlcw==")
_B=alpha__("ZmVlZGJhY2tfdHlwZQ==")
_A=None
import logging
from collections.abc import Callable
from math import ceil
from typing import Any
from homeassistant.components.light import ATTR_BRIGHTNESS,ATTR_COLOR_TEMP_KELVIN,ATTR_RGB_COLOR,ATTR_RGBW_COLOR,ColorMode,LightEntity,LightEntityFeature
from homeassistant.const import STATE_UNKNOWN
from homeassistant.core import Event,HomeAssistant,callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
from TISControlProtocol.api import TISApi
from TISControlProtocol.BytesHelper import int_to_8_bit_binary
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler
from.import TISConfigEntry
from.const import POLLING_INTERVAL
handler=TISProtocolHandler()
async def async_setup_entry(hass,entry,async_add_devices):
    F=alpha__("Z2F0ZXdheQ==");E=alpha__("aXNfcHJvdGVjdGVk");D=alpha__("ZGV2aWNlX2lk");C=async_add_devices;A=alpha__("Y2hhbm5lbHM=");B=entry.runtime_data.api;G=await B.get_entities(platform=alpha__("ZGltbWVy"))
    if G:K=[(C,next(iter(B[A][0].values())),B[D],B[E],B[F])for B in G for(C,B)in B.items()];L=[TISLight(tis_api=B,light_name=A,device_id=D,channel_number=C,gateway=E)for(A,C,D,F,E)in K];C(L)
    H=await B.get_entities(platform=alpha__("cmdi"))
    if H:M=[(C,next(iter(B[A][0].values())),next(iter(B[A][1].values())),next(iter(B[A][2].values())),B[D],B[E],B[F])for B in H for(C,B)in B.items()];N=[TISRGBLight(tis_api=B,light_name=A,r_channel=C,g_channel=D,b_channel=E,device_id=F,gateway=G)for(A,C,D,E,F,H,G)in M];C(N)
    I=await B.get_entities(platform=alpha__("cmdidw=="))
    if I:O=[(C,next(iter(B[A][0].values())),next(iter(B[A][1].values())),next(iter(B[A][2].values())),next(iter(B[A][3].values())),B[D],B[E],B[F])for B in I for(C,B)in B.items()];P=[TISRGBWLight(tis_api=B,light_name=A,r_channel=C,g_channel=D,b_channel=E,w_channel=F,device_id=G,gateway=H)for(A,C,D,E,F,G,I,H)in O];C(P)
    J=await B.get_entities(platform=alpha__("ZGFsaQ=="))
    if J:Q=[(C,next(iter(B[A][0].values())),next(iter(B[A][1].values())),B[D],B[E],B[F])for B in J for(C,B)in B.items()];R=[TISDaliLight(tis_api=B,light_name=A,brightness_channel=C,temperature_channel=D,device_id=E,gateway=F)for(A,C,D,E,G,F)in Q];C(R)
class TISLight(LightEntity):
    def __init__(A,tis_api,gateway,light_name,channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.channel_number=int(channel_number);A._attr_name=light_name;A._attr_state=_A;A._attr_brightness=_A;A.listener=_A;A.broadcast_channel=255;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A.name, __var1=A.channel_number);A._update_task_unsub=_A;A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.BRIGHTNESS};A._attr_color_mode=ColorMode.BRIGHTNESS;A._attr_supported_features=LightEntityFeature.TRANSITION;A.update_packet=handler.generate_control_update_packet(A)
    def _start_polling(A):
        if not A._update_task_unsub:logging.info(beta__("U3RhcnRpbmcgc3RhdGUgcG9sbGluZyBmb3IgbGlnaHQge19fdmFyMH0=", __var0=A.name));A._update_task_unsub=async_track_time_interval(A.hass,A._async_poll_for_state,POLLING_INTERVAL)
    def _stop_polling(A):
        if A._update_task_unsub:logging.info(beta__("U3RvcHBpbmcgc3RhdGUgcG9sbGluZyBmb3IgbGlnaHQge19fdmFyMH0=", __var0=A.name));A._update_task_unsub();A._update_task_unsub=_A
    async def _async_poll_for_state(A,now=_A):logging.info(beta__("UG9sbGluZyBmb3Igc3RhdGUgb2YgbGlnaHQge19fdmFyMH0=", __var0=A.name));await A.api.protocol.sender.send_packet(A.update_packet)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event;C=A._attr_state;D=A._attr_brightness
            if B.event_type==str(A.device_id):
                if B.data[_B]==alpha__("Y29udHJvbF9yZXNwb25zZQ=="):
                    F=B.data[_H]
                    if int(F)==A.channel_number:E=B.data[_C][2];C=int(E)!=0;D=int(E/100*255)
                elif A.channel_number!=A.broadcast_channel:
                    if B.data[_B]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):
                        G=ceil(B.data[_C][0]/8);H=alpha__("").join(int_to_8_bit_binary(B.data[_C][A])for A in range(1,G+1))
                        if H[A.channel_number-1]==alpha__("MA=="):C=_E;D=0
                        else:C=_D
                    elif B.data[_B]==_F:I=B.data[_C];D=int(I[A.channel_number]/100*255);C=D>0
                elif B.data[_B]==_G:C=_A;D=_A
                if A._attr_state!=C or A._attr_brightness!=D:
                    A._attr_state=C;A._attr_brightness=D
                    if A._attr_state in(_D,_E):A._stop_polling()
                    elif A._attr_state is _A:A._start_polling()
                    A.async_write_ha_state()
        try:A.listener=A.hass.bus.async_listen(str(A.device_id),B);await A._async_poll_for_state();A._start_polling()
        except Exception as C:logging.error(beta__("RXJyb3IgaW4gYXN5bmNfYWRkZWRfdG9faGFzcyBmb3IgbGlnaHQge19fdmFyMH06IHtfX3ZhcjF9", __var0=A.name, __var1=C))
    async def async_will_remove_from_hass(A):
        if A.listener:A.listener();A.listener=_A
        A._stop_polling()
    @property
    def brightness(self):return self._attr_brightness
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def supported_features(self):return self._attr_supported_features
    @property
    def is_on(self):return self._attr_state
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**B):
        A._attr_state=_A;A._start_polling()
        try:
            C=B.get(ATTR_BRIGHTNESS,255);D=handler.generate_light_control_packet(A,int(C/255*100));E=await A.api.protocol.sender.send_packet_with_ack(D)
            if not E:logging.warning(beta__("Tm8gQUNLIHJlY2VpdmVkIGZvciB0dXJuaW5nIG9uIGxpZ2h0IHtfX3ZhcjB9LiBEZXZpY2UgbWF5IGJlIG9mZmxpbmUu", __var0=A.name))
        except Exception as F:logging.error(beta__("RXJyb3IgaW4gYXN5bmNfdHVybl9vbiBmb3IgbGlnaHQge19fdmFyMH06IHtfX3ZhcjF9", __var0=A.name, __var1=F))
        A.async_write_ha_state()
    async def async_turn_off(A,**E):
        A._attr_state=_A;A._start_polling()
        try:
            B=handler.generate_light_control_packet(A,0);C=await A.api.protocol.sender.send_packet_with_ack(B)
            if not C:logging.warning(beta__("Tm8gQUNLIHJlY2VpdmVkIGZvciB0dXJuaW5nIG9mZiBsaWdodCB7X192YXIwfS4gRGV2aWNlIG1heSBiZSBvZmZsaW5lLg==", __var0=A.name))
        except Exception as D:logging.error(beta__("RXJyb3IgaW4gYXN5bmNfdHVybl9vZmYgZm9yIGxpZ2h0IHtfX3ZhcjB9OiB7X192YXIxfQ==", __var0=A.name, __var1=D))
        A.async_write_ha_state()
class TISRGBLight(LightEntity):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=int(r_channel);A.g_channel=int(g_channel);A.b_channel=int(b_channel);A.rgb_value_flags=[0,0,0];A._attr_name=light_name;A._attr_state=_A;A._attr_rgb_color=_A;A._attr_brightness=_A;A.listener=_A;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM30=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel);A.default_color=0,0,0;A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.RGB};A._attr_color_mode=ColorMode.RGB;A.generate_rgb_packets=handler.generate_rgb_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            C=event
            if C.event_type==str(A.device_id):
                if C.data[_B]==_F:
                    D=C.data[_C];B=C.data[_H]
                    if A._attr_rgb_color is _A:A._attr_rgb_color=[0,0,0]
                    if B==A.r_channel:A._attr_rgb_color[0]=int(D[B]/100*255)
                    elif B==A.g_channel:A._attr_rgb_color[1]=int(D[B]/100*255)
                    elif B==A.b_channel:A._attr_rgb_color[2]=int(D[B]/100*255)
                    A._attr_state=bool(A.r_channel or A.g_channel or A.b_channel)
                elif C.data[_B]==_G:A._attr_state=STATE_UNKNOWN
        A.listener=A.hass.bus.async_listen(str(A.device_id),B)
        for C in range(5):
            if A._attr_rgb_color is _A:D=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_rgb_color is _A:A._attr_state=STATE_UNKNOWN;A._attr_rgb_color=0,0,0
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def brightness(self):return self._attr_brightness
    @property
    def rgb_color(self):return self._attr_rgb_color
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def is_on(self):return self._attr_state
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**G):
        try:
            B=G.get(ATTR_RGB_COLOR,_A);C=G.get(ATTR_BRIGHTNESS,_A);logging.info(beta__("Y29sb3I6IHtfX3ZhcjB9", __var0=B));logging.info(beta__("YnJpZ2h0bmVzczoge19fdmFyMH0=", __var0=C))
            if B is not _A:B=tuple([int(A/255*100)for A in B]);D,E,F=A.generate_rgb_packets(A,B);await A.api.protocol.sender.send_packet(D);await A.api.protocol.sender.send_packet(E);await A.api.protocol.sender.send_packet(F);A._attr_state=_D;B=tuple([int(A/100*255)for A in B]);A._attr_rgb_color=B;A.default_color=B;logging.info(beta__("bmV3IGRlZmF1bHQgY29sb3I6IHtfX3ZhcjB9", __var0=B))
            elif C is not _A:C=max(1,min(255,C));C/=255;B=A.default_color or(0,0,0);logging.info(beta__("ZGVmYXVsdCBjb2xvcjoge19fdmFyMH0=", __var0=B));B=tuple([int(C*A*100/255)for A in B]);D,E,F=A.generate_rgb_packets(A,B);await A.api.protocol.sender.send_packet(D);await A.api.protocol.sender.send_packet(E);await A.api.protocol.sender.send_packet(F);logging.info(beta__("YnJpZ2h0ZW5lZCBjb2xvcjoge19fdmFyMH0=", __var0=B))
            else:logging.info(alpha__("TmVpdGhlciBjb2xvciBub3IgYnJpZ2h0bmVzcyBwcm92aWRlZCwgdXNpbmcgZGVmYXVsdCBjb2xvci4="));B=A.default_color or(0,0,0);A._attr_state=_D if A.default_color and A.default_color!=(0,0,0)else _E;A._attr_rgb_color=B;B=tuple([int(A*100/255)for A in B]);D,E,F=A.generate_rgb_packets(A,B);await A.api.protocol.sender.send_packet(D);await A.api.protocol.sender.send_packet(E);await A.api.protocol.sender.send_packet(F)
        except KeyError as H:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=H))
        A.async_write_ha_state()
    async def async_turn_off(A,**B):logging.info(alpha__("dHVybmluZyBvZmY="));logging.info(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=B));C,D,E=A.generate_rgb_packets(A,(0,0,0));await A.api.protocol.sender.send_packet(D);await A.api.protocol.sender.send_packet(C);await A.api.protocol.sender.send_packet(E);A._attr_state=_E;A._attr_rgb_color=0,0,0;A.async_write_ha_state()
class TISRGBWLight(LightEntity):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,w_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=int(r_channel);A.g_channel=int(g_channel);A.b_channel=int(b_channel);A.w_channel=int(w_channel);A._attr_name=light_name;A._attr_state=_A;A._attr_brightness=_A;A._attr_rgbw_color=_A;A.rgbw_value_flags=[0,0,0,0];A.listener=_A;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM31fe19fdmFyNH0=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel, __var4=A.w_channel);A.default_color=0,0,0,0;A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.RGBW};A._attr_color_mode=ColorMode.RGBW;A._attr_supported_features=LightEntityFeature.TRANSITION;A.generate_rgbw_packets=handler.generate_rgbw_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_B]==_F:logging.info(beta__("UkdCVyBldmVudCBkYXRhOiB7X192YXIwfQ==", __var0=B.data));C=B.data[_C];D=C[A.r_channel]/100*255;E=C[A.g_channel]/100*255;F=C[A.b_channel]/100*255;G=C[A.w_channel]/100*255;A._attr_rgbw_color=D,E,F,G;A._attr_state=bool(D or E or F or G)
                elif B.data[_B]==_G:A._attr_state=STATE_UNKNOWN
        A.listener=A.hass.bus.async_listen(str(A.device_id),B)
        for C in range(5):
            if A._attr_rgbw_color is _A:D=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_rgbw_color is _A:A._attr_state=STATE_UNKNOWN;A._attr_rgbw_color=0,0,0,0
    @property
    def brightness(self):return self._attr_brightness
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def rgbw_color(self):return self._attr_rgbw_color
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def supported_features(self):return self._attr_supported_features
    @property
    def is_on(self):return self._attr_state
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**D):
        try:
            B=D.get(ATTR_RGBW_COLOR,_A);C=D.get(ATTR_BRIGHTNESS,_A);logging.warning(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=D))
            if B is not _A:B=tuple([int(A/255*100)for A in B]);E,F,G,H=A.generate_rgbw_packets(A,B);logging.info(beta__("Y29sb3IgKHBlcmNlbnQpOiB7X192YXIwfQ==", __var0=B));await A.api.protocol.sender.send_packet(E);await A.api.protocol.sender.send_packet(F);await A.api.protocol.sender.send_packet(G);await A.api.protocol.sender.send_packet(H);A._attr_state=_D;B=tuple([int(A/100*255)for A in B]);A._attr_rgbw_color=B;A.default_color=B
            elif C is not _A:C=max(1,min(255,C));logging.warning(beta__("YnJpZ2h0bmVzczoge19fdmFyMH0sIHNlbGYuX2F0dHJfYnJpZ2h0bmVzczoge19fdmFyMX0=", __var0=C, __var1=A._attr_brightness));A._attr_brightness=C;C/=255;B=A.default_color or(0,0,0,0);logging.info(beta__("ZGVmYXVsdCBjb2xvcjoge19fdmFyMH0=", __var0=B));B=tuple([int(C*A*100/255)for A in B]);E,F,G,H=A.generate_rgbw_packets(A,B);await A.api.protocol.sender.send_packet(E);await A.api.protocol.sender.send_packet(F);await A.api.protocol.sender.send_packet(G);await A.api.protocol.sender.send_packet(H);A._attr_state=_D;B=tuple([int(A/100*255)for A in B]);A._attr_rgbw_color=B
        except KeyError as I:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=I))
        A.async_write_ha_state()
    async def async_turn_off(A,**F):B,C,D,E=A.generate_rgbw_packets(A,(0,0,0,0));await A.api.protocol.sender.send_packet(B);await A.api.protocol.sender.send_packet(C);await A.api.protocol.sender.send_packet(D);await A.api.protocol.sender.send_packet(E);A._attr_state=_E;A._attr_rgbw_color=0,0,0,0;A.async_write_ha_state()
class TISDaliLight(LightEntity):
    def __init__(A,tis_api,gateway,light_name,brightness_channel,temperature_channel,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.brightness_channel=int(brightness_channel);A.temperature_channel=int(temperature_channel);A._attr_name=light_name;A._attr_state=_A;A._attr_brightness=_A;A._attr_color_temp_kelvin=_A;A.listener=_A;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn0=", __var0=A.name, __var1=A.brightness_channel, __var2=A.temperature_channel);A.default_temperature=4000;A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.COLOR_TEMP};A._attr_color_mode=ColorMode.COLOR_TEMP;A._attr_supported_features=LightEntityFeature.TRANSITION;A.generate_dali_packets=getattr(handler,alpha__("Z2VuZXJhdGVfZGFsaV9saWdodF9jb250cm9sX3BhY2tldA=="),_A);A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_B]==_F:C=B.data[_C];F=C[A.temperature_channel];D=C[A.brightness_channel];A._attr_brightness=int(D/100*255);E=2700;G=6500;A._attr_color_temp_kelvin=int(E+F/100*(G-E));A._attr_state=bool(D>0)
                elif B.data[_B]==_G:A._attr_state=STATE_UNKNOWN
        A.listener=A.hass.bus.async_listen(str(A.device_id),B)
        for C in range(5):
            if A._attr_state is _A:D=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_state is _A:A._attr_state=STATE_UNKNOWN
    @property
    def brightness(self):return self._attr_brightness
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def color_temp_kelvin(self):return self._attr_color_temp_kelvin
    @property
    def min_color_temp_kelvin(self):return 2700
    @property
    def max_color_temp_kelvin(self):return 6500
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def supported_features(self):return self._attr_supported_features
    @property
    def is_on(self):return bool(self._attr_state)
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**E):
        try:
            B=E.get(ATTR_COLOR_TEMP_KELVIN,_A);C=E.get(ATTR_BRIGHTNESS,_A)
            if C is _A:
                if A._attr_brightness is not _A and A._attr_brightness>0:C=A._attr_brightness
                else:C=255
            if B is _A:
                if A._attr_color_temp_kelvin is not _A:B=A._attr_color_temp_kelvin
                else:B=A.default_temperature
            F=2700;G=6500;D=int((B-F)/(G-F)*100);D=max(0,min(100,D));H=int(C/255*100)
            if A.generate_dali_packets:I,J=A.generate_dali_packets(A,H,D);await A.api.protocol.sender.send_packet(I);await A.api.protocol.sender.send_packet(J)
            A._attr_state=_D;A._attr_brightness=C;A._attr_color_temp_kelvin=B
        except Exception as K:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=K))
        A.async_write_ha_state()
    async def async_turn_off(A,**G):
        B=0
        if A._attr_color_temp_kelvin is not _A:C=2700;D=6500;B=int((A._attr_color_temp_kelvin-C)/(D-C)*100);B=max(0,min(100,B))
        if A.generate_dali_packets:E,F=A.generate_dali_packets(A,0,B);await A.api.protocol.sender.send_packet(E);await A.api.protocol.sender.send_packet(F)
        A._attr_state=_E;A._attr_brightness=0;A.async_write_ha_state()