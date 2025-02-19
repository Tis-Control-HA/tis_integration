from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)
a=decode__("c3RhdGU=")
Z=decode__("b3BlcmF0aW9uX3ZhbHVl")
Y=decode__("c3ViX29wZXJhdGlvbg==")
X=decode__("bnVtYmVy")
W=decode__("ZmVlZGJhY2tfdHlwZQ==")
V=decode__("dGFyZ2V0")
P=False
O=True
N=str
M=decode__("bWlu")
L=decode__("bWF4")
K=int
J=next
A=property
C=None
import logging as D
from typing import Any
from TISControlProtocol.api import TISApi
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler as b
from homeassistant.components.climate import ATTR_TEMPERATURE as R,FAN_AUTO as c,FAN_HIGH as d,FAN_LOW as e,FAN_MEDIUM as S,ClimateEntity as T,ClimateEntityFeature as F,HVACMode as B,UnitOfTemperature as I
from homeassistant.const import STATE_OFF as G,STATE_ON as H,STATE_UNKNOWN as Q
from homeassistant.core import Event,HomeAssistant,callback as U
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
from.const import FAN_MODES,TEMPERATURE_RANGES
E=b()
async def async_setup_entry(hass,entry,async_add_devices):
    H=decode__("Z2F0ZXdheQ==");G=decode__("aXNfcHJvdGVjdGVk");F=decode__("ZGV2aWNlX2lk");E=decode__("Y2hhbm5lbHM=");B=async_add_devices;A=entry.runtime_data.api;C=await A.get_entities(platform=decode__("YWM="))
    if C:I=[(C,J(iter(A[E][0].values())),A[F],A[G],A[H])for B in C for(C,A)in B.items()];K=[f(tis_api=A,ac_name=B,ac_number=C,device_id=D,gateway=E)for(B,C,D,F,E)in I];B(K)
    D=await A.get_entities(platform=decode__("Zmxvb3JfaGVhdGluZw=="))
    if D:L=[(C,J(iter(A[E][0].values())),A[F],A[G],A[H])for B in D for(C,A)in B.items()];M=[g(tis_api=A,heater_name=B,heater_number=C,device_id=D,gateway=E)for(B,C,D,F,E)in L];B(M)
class f(T):
    def __init__(A,tis_api,ac_name,ac_number,device_id,gateway):A.api=tis_api;A._name=ac_name;A.device_id=device_id;A.ac_number=K(ac_number)-1;A._attr_unique_id=format_str__("YWNfe19fdmFyMH1fe19fdmFyMX0=", __var0=A.device_id, __var1=A.ac_number);A.gateway=gateway;A._attr_temperature_unit=I.CELSIUS;A._unit_index=0 if A._attr_temperature_unit==I.CELSIUS else 1;A.update_packet=E.generate_ac_update_packet(A);A.listener=C;A._attr_state=G;A._attr_target_temperature=C;A._attr_current_temperature=C;A._attr_max_temp=C;A._attr_min_temp=C;A._attr_target_temperature_step=C;A.setup_ac()
    def setup_ac(A):A._attr_hvac_mode=B.COOL;A._attr_fan_mode=S;A._attr_max_temp=TEMPERATURE_RANGES[A._attr_hvac_mode][L][A._unit_index];A._attr_min_temp=TEMPERATURE_RANGES[A._attr_hvac_mode][M][A._unit_index];A._attr_target_temperature=TEMPERATURE_RANGES[A._attr_hvac_mode][V][A._unit_index];A._attr_target_temperature_step=1 if A._unit_index==0 else 2;A._attr_hvac_modes=[B.OFF,B.HEAT,B.COOL,B.AUTO,B.FAN_ONLY];A._attr_supported_features=F.FAN_MODE|F.TARGET_TEMPERATURE|F.TURN_OFF|F.TURN_ON;A._attr_fan_modes=[c,e,S,d];A.mode_target_temperatures={B.COOL:20,B.HEAT:30,B.FAN_ONLY:C,B.AUTO:20,B.OFF:C}
    async def async_added_to_hass(A):
        @U
        async def E(event):
            Q=decode__("cGFja2V0X21vZGVfaW5kZXg=");F=event
            if F.event_type==N(A.device_id):
                P=F.data.get(W,C)
                if P==decode__("YWNfZmVlZGJhY2s="):
                    R=F.data[X];I=F.data[Y];E=F.data[Z]
                    if A.ac_number==K(R):
                        D.info(format_str__("QUMgZmVlZGJhY2sgZXZlbnQ6IHtfX3ZhcjB9", __var0=F.data))
                        if I==3:
                            if E==0:A._attr_state=G;A._attr_hvac_mode=B.OFF;D.info(decode__("QUMgdHVybmVkIG9mZg=="))
                        else:
                            A._attr_state=H
                            if I==4:A._attr_hvac_mode=B.COOL;A._attr_target_temperature=E;A._attr_current_temperature=E;D.info(format_str__("Q29vbCBtb2RlIHRlbXBlcmF0dXJlIHVwZGF0ZWQgdG8ge19fdmFyMH0=", __var0=E))
                            elif I==5:A._attr_fan_mode=J(A for(A,B)in FAN_MODES.items()if B==E);D.info(format_str__("RmFuIHNwZWVkIHVwZGF0ZWQgdG8ge19fdmFyMH0=", __var0=E))
                            elif I==6:A._attr_hvac_mode=J((A for(A,B)in TEMPERATURE_RANGES.items()if B[Q]==E),C);D.info(format_str__("SFZBQyBtb2RlIGNoYW5nZWQgdG8ge19fdmFyMH0=", __var0=E))
                            elif I==7:A._attr_hvac_mode=B.HEAT;A._attr_target_temperature=E;A._attr_current_temperature=E;D.info(format_str__("SGVhdGluZyBtb2RlIHRlbXBlcmF0dXJlIHVwZGF0ZWQgdG8ge19fdmFyMH0=", __var0=E))
                            elif I==8:A._attr_hvac_mode=B.AUTO;A._attr_target_temperature=E;A._attr_current_temperature=E;D.info(format_str__("QXV0byBtb2RlIHRlbXBlcmF0dXJlIHVwZGF0ZWQgdG8ge19fdmFyMH0=", __var0=E))
                            else:D.error(format_str__("VW5rbm93biBzdWIgb3BlcmF0aW9uIGZvciBBQyBmZWVkYmFjazoge19fdmFyMH0=", __var0=I))
                elif P==decode__("dXBkYXRlX2ZlZWRiYWNr"):
                    if F.data[decode__("YWNfbnVtYmVy")]==A.ac_number:
                        if F.data[a]==0:A._attr_state=G;A._attr_hvac_mode=B.OFF
                        else:
                            A._attr_state=H;A._attr_hvac_mode=J((A for(A,B)in TEMPERATURE_RANGES.items()if B[Q]==F.data[decode__("aHZhY19tb2Rl")]),C);A._attr_fan_mode=J(A for(A,B)in FAN_MODES.items()if B==F.data[decode__("ZmFuX3NwZWVk")]);A._attr_min_temp=TEMPERATURE_RANGES[A.hvac_mode][M][A._unit_index];A._attr_max_temp=TEMPERATURE_RANGES[A.hvac_mode][L][A._unit_index]
                            if A._attr_hvac_mode==B.COOL:A._attr_target_temperature=F.data[decode__("Y29vbF90ZW1w")]
                            elif A._attr_hvac_mode==B.HEAT:A._attr_target_temperature=F.data[decode__("aGVhdF90ZW1w")]
                            elif A._attr_hvac_mode==B.AUTO:A._attr_target_temperature=F.data[decode__("YXV0b190ZW1w")]
                            else:A._attr_target_temperature=C
            A.async_write_ha_state();await A.async_update_ha_state(O)
        A.listener=A.hass.bus.async_listen(N(A.device_id),E);await A.api.protocol.sender.send_packet(A.update_packet)
    @A
    def name(self):return self._name
    @A
    def is_on(self):
        if self._attr_state==H:return O
        elif self._attr_state==G:return P
        else:return
    @A
    def temperature_unit(self):return self._attr_temperature_unit
    @A
    def current_temperature(self):return self._attr_target_temperature
    @A
    def target_temperature(self):return self._attr_target_temperature
    @A
    def hvac_mode(self):return self._attr_hvac_mode
    @A
    def hvac_modes(self):return self._attr_hvac_modes
    @A
    def fan_modes(self):return self._attr_fan_modes
    @A
    def should_poll(self):return P
    async def async_set_hvac_mode(A,hvac_mode):
        F=hvac_mode
        if F==B.OFF:I=G;J=C;K=C;N=C
        else:I=H;K=TEMPERATURE_RANGES[F][M][A._unit_index];N=TEMPERATURE_RANGES[F][L][A._unit_index];J=A.mode_target_temperatures[F]
        O=E.generate_ac_control_packet(A,TEMPERATURE_RANGES,FAN_MODES,target_state=I,target_temperature=J,target_mode=F);P=await A.api.protocol.sender.send_packet_with_ack(O)
        if P:A._attr_hvac_mode=F;A._attr_state=I;A._attr_min_temp=K;A._attr_max_temp=N;A._attr_current_temperature=A._attr_target_temperature=J
        else:D.error(decode__("RmFpbGVkIHRvIHNldCBodmFjIG1vZGU="));A._attr_state=Q;A._attr_hvac_mode=C
        A.async_write_ha_state()
    async def async_set_fan_mode(A,fan_mode):
        B=fan_mode;F=E.generate_ac_control_packet(A,TEMPERATURE_RANGES,FAN_MODES,target_fan_mode=B);G=await A.api.protocol.sender.send_packet_with_ack(F)
        if G:A._attr_fan_mode=B
        else:D.error(decode__("RmFpbGVkIHRvIHNldCBmYW4gbW9kZQ=="));A._attr_state=Q;A._attr_fan_mode=C
        A.async_write_ha_state()
    async def async_set_temperature(A,**F):
        B=F.get(R);G=E.generate_ac_control_packet(A,TEMPERATURE_RANGES,FAN_MODES,target_temperature=B);H=await A.api.protocol.sender.send_packet_with_ack(G)
        if H:A._attr_current_temperature=A._attr_target_temperature=B;A.mode_target_temperatures[A.hvac_mode]=B if B else A.target_temperature
        else:A._attr_state=Q;D.error(decode__("RmFpbGVkIHRvIHNldCB0ZW1wZXJhdHVyZQ=="));A._attr_target_temperature=C;A._attr_hvac_mode=C;A._attr_current_temperature=C
        A.async_write_ha_state()
class g(T):
    def __init__(A,tis_api,heater_name,heater_number,device_id,gateway):A.api=tis_api;A._name=heater_name;A.device_id=device_id;A.heater_number=K(heater_number)-1;A._attr_unique_id=format_str__("Zmxvb3JfaGVhdGVyX3tfX3ZhcjB9X3tfX3ZhcjF9", __var0=A.device_id, __var1=A.heater_number);A.gateway=gateway;A._attr_temperature_unit=I.CELSIUS;A._unit_index=0 if A._attr_temperature_unit==I.CELSIUS else 1;A.update_packet=E.generate_floor_update_packet(A);A.listener=C;A._attr_state=G;A._attr_target_temperature=C;A._attr_current_temperature=C;A._attr_max_temp=C;A._attr_min_temp=C;A._attr_target_temperature_step=C;A.setup_heater()
    def setup_heater(A):A._attr_hvac_mode=B.HEAT;A._attr_max_temp=TEMPERATURE_RANGES[A._attr_hvac_mode][L][A._unit_index];A._attr_min_temp=TEMPERATURE_RANGES[A._attr_hvac_mode][M][A._unit_index];A._attr_target_temperature=TEMPERATURE_RANGES[A._attr_hvac_mode][V][A._unit_index];A._attr_target_temperature_step=1 if A._unit_index==0 else 2;A._attr_hvac_modes=[B.OFF,B.HEAT];A._attr_supported_features=F.TARGET_TEMPERATURE|F.TURN_OFF|F.TURN_ON;A.mode_target_temperatures={B.HEAT:30,B.OFF:C}
    async def async_added_to_hass(A):
        @U
        async def E(event):
            E=event
            if E.event_type==N(A.device_id):
                J=E.data.get(W,C)
                if J==decode__("Zmxvb3JfZmVlZGJhY2s="):
                    D.info(format_str__("Zmxvb3IgaGVhdGluZyBmZWVkYmFjayBldmVudDoge19fdmFyMH0=", __var0=E.data));P=E.data[X];I=E.data[Y];F=E.data[Z]
                    if A.heater_number==K(P):
                        if I==20:
                            if F==0:A._attr_state=G;A._attr_hvac_mode=B.OFF;D.info(decode__("SGVhdGVyIHR1cm5lZCBvZmY="))
                            else:A._attr_state=H;A._attr_hvac_mode=B.HEAT;A._attr_target_temperature=F;A._attr_current_temperature=F;D.info(format_str__("SGVhdGluZyBtb2RlIHRlbXBlcmF0dXJlIHVwZGF0ZWQgdG8ge19fdmFyMH0=", __var0=F))
                        elif I==24:A._attr_target_temperature=F;A._attr_current_temperature=F
                        else:D.error(format_str__("VW5rbm93biBzdWIgb3BlcmF0aW9uIGZvciBBQyBmZWVkYmFjazoge19fdmFyMH0=", __var0=I))
                elif J==decode__("Zmxvb3JfdXBkYXRl"):
                    D.info(format_str__("Zmxvb3IgaGVhdGluZyB1cGRhdGUgZXZlbnQ6IHtfX3ZhcjB9", __var0=E.data))
                    if E.data[decode__("aGVhdGVyX251bWJlcg==")]==A.heater_number:
                        if E.data[a]==0:A._attr_state=G;A._attr_hvac_mode=B.OFF
                        else:
                            A._attr_state=H;A._attr_hvac_mode=B.HEAT;A._attr_min_temp=TEMPERATURE_RANGES[A.hvac_mode][M][A._unit_index];A._attr_max_temp=TEMPERATURE_RANGES[A.hvac_mode][L][A._unit_index]
                            if A._attr_hvac_mode==B.HEAT:A._attr_target_temperature=E.data[decode__("dGVtcA==")]
                            else:A._attr_target_temperature=C
            A.async_write_ha_state();await A.async_update_ha_state(O)
        A.listener=A.hass.bus.async_listen(N(A.device_id),E);await A.api.protocol.sender.send_packet(A.update_packet)
    @A
    def name(self):return self._name
    @A
    def is_on(self):
        if self._attr_state==H:return O
        elif self._attr_state==G:return P
        else:return
    @A
    def temperature_unit(self):return self._attr_temperature_unit
    @A
    def current_temperature(self):return self._attr_target_temperature
    @A
    def target_temperature(self):return self._attr_target_temperature
    @A
    def hvac_mode(self):return self._attr_hvac_mode
    @A
    def hvac_modes(self):return self._attr_hvac_modes
    @A
    def should_poll(self):return P
    async def async_set_hvac_mode(A,hvac_mode):C=E.generate_floor_on_off_packet(A,0 if hvac_mode==B.OFF else 1);await A.api.protocol.sender.send_packet(C)
    async def async_set_temperature(A,**C):D=C.get(R);B=E.generate_floor_on_off_packet(A,0 if A._attr_state==G else 1);await A.api.protocol.sender.send_packet(B);B=E.generate_floor_set_temp_packet(A,K(D));await A.api.protocol.sender.send_packet_with_ack(B)