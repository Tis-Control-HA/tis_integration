from __future__ import annotations
from TISControlProtocol import *
L=alpha__("bmlnaHQ=")
K=alpha__("YXdheQ==")
J=alpha__("dmFjYXRpb24=")
I=ValueError
F=True
C=alpha__("ZGlzYXJt")
A=property
D=None
from homeassistant.components.select import SelectEntity as M
from TISControlProtocol.api import TISApi
from homeassistant.const import MATCH_ALL as N,STATE_UNAVAILABLE as O
from homeassistant.core import callback as P,Event,HomeAssistant
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler as G
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
import logging as B
H={J:1,K:2,L:3,C:6}
E={1:J,2:K,3:L,6:C}
Q=G()
async def async_setup_entry(hass,entry,async_add_devices):
    A=entry.runtime_data.api;B=await A.get_entities(platform=alpha__("c2VjdXJpdHk="))
    if B:D=[(C,next(iter(A[alpha__("Y2hhbm5lbHM=")][0].values())),A[alpha__("ZGV2aWNlX2lk")],A[alpha__("Z2F0ZXdheQ==")])for B in B for(C,A)in B.items()];E=[S(api=A,name=B,options=list(H.keys()),initial_option=C,channel_number=D,device_id=E,gateway=F)for(B,D,E,F)in D];async_add_devices(E)
R=G()
class S(M):
    def __init__(A,api,name,options,initial_option,channel_number,device_id,gateway):A._name=name;A.api=api;A.unique_id=beta__("c2VsZWN0X3tfX3ZhcjB9", __var0=A.name);A._attr_options=options;A._attr_current_option=A._state=initial_option;A._attr_icon=alpha__("bWRpOnNoaWVsZA==");A._attr_is_protected=F;A._attr_read_only=F;A._listener=D;A.channel_number=int(channel_number);A.device_id=device_id;A.gateway=gateway;A.update_packet=R.generate_update_security_packet(A)
    async def async_added_to_hass(A):
        @P
        async def handle_event(event):
            G=alpha__("ZmVlZGJhY2tfdHlwZQ==");C=event
            if C.event_type==alpha__("YWRtaW5fbG9jaw=="):
                B.info(beta__("YWRtaW4gbG9jayBldmVudDoge19fdmFyMH0=", __var0=C.data))
                if C.data.get(alpha__("bG9ja2Vk")):A.protect()
                else:A.unprotect()
            if C.data.get(G)==alpha__("c2VjdXJpdHlfZmVlZGJhY2s=")or C.data.get(G)==alpha__("c2VjdXJpdHlfdXBkYXRl"):
                B.info(beta__("c2VjdXJpdHkgZmVlZGJhY2sgZXZlbnQ6IHtfX3ZhcjB9", __var0=C.data))
                if A.channel_number==C.data[alpha__("Y2hhbm5lbF9udW1iZXI=")]:
                    D=C.data[alpha__("bW9kZQ==")]
                    if D in E:F=E[D];B.info(beta__("bW9kZToge19fdmFyMH0sIG9wdGlvbjoge19fdmFyMX0=", __var0=D, __var1=F));A._state=A._attr_current_option=F
            A.async_write_ha_state()
        A._listener=A.hass.bus.async_listen(N,handle_event);await A.api.protocol.sender.send_packet(A.update_packet);B.info(beta__("dXBkYXRlIHBhY2tldCBzZW50OiB7X192YXIwfQ==", __var0=A.update_packet));B.info(beta__("bGlzdGVuZXIgYWRkZWQ6IHtfX3ZhcjB9", __var0=A._listener))
    @A
    def name(self):return self._name
    @A
    def options(self):return self._attr_options
    @A
    def current_option(self):return self._attr_current_option if self._attr_current_option in E.values()else D
    def protect(A):A._attr_read_only=F
    def unprotect(A):A._attr_read_only=False
    async def async_select_option(A,option):
        C=option
        if A._attr_is_protected:
            if A._attr_read_only:A._state=A._attr_current_option=O;B.error(alpha__("cmVzZXR0aW5nIHN0YXRlIHRvIGxhc3Qga25vd24gc3RhdGU="));await A.api.protocol.sender.send_packet(A.update_packet);A.async_write_ha_state();raise I(alpha__("VGhlIHNlY3VyaXR5IG1vZHVsZSBpcyBwcm90ZWN0ZWQgYW5kIHJlYWQgb25seQ=="))
            else:
                B.info(beta__("c2V0dGluZyBzZWN1cml0eSBtb2RlIHRvIHtfX3ZhcjB9", __var0=C));E=H.get(C,D)
                if E:
                    B.info(beta__("bW9kZToge19fdmFyMH0=", __var0=E));F=Q.generate_control_security_packet(A,E);G=await A.api.protocol.sender.send_packet_with_ack(F);B.info(beta__("Y29udHJvbF9wYWNrZXQ6IHtfX3ZhcjB9", __var0=F));B.info(beta__("YWNrOiB7X192YXIwfQ==", __var0=G))
                    if G:B.info(beta__("c2V0dGluZyBzdGF0ZSB0byB7X192YXIwfQ==", __var0=C));A._state=A._attr_current_option=C;A.async_write_ha_state()
                    else:B.warning(beta__("RmFpbGVkIHRvIHNldCBzZWN1cml0eSBtb2RlIHRvIHtfX3ZhcjB9", __var0=C));A._state=A._attr_current_option=D;A.async_write_ha_state()
        if C not in A._attr_options:raise I(beta__("SW52YWxpZCBvcHRpb246IHtfX3ZhcjB9IChwb3NzaWJsZSBvcHRpb25zOiB7X192YXIxfSk=", __var0=C, __var1=A._attr_options))