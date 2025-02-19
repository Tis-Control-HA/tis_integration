from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)
G=Exception
F=False
C=None
B=property
from typing import Any
import logging as E
from homeassistant.components.fan import FanEntity as H,FanEntityFeature as D
from homeassistant.core import Event,HomeAssistant,callback as I
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from TISControlProtocol.api import TISApi
from.import TISConfigEntry
import RPi.GPIO as A
J=D.SET_SPEED|D.TURN_OFF|D.TURN_ON
async def async_setup_entry(hass,entry,async_add_entities):A=entry.runtime_data.api;async_add_entities([K(hass,decode__("Q1BVX0Zhbg=="),decode__("Q1BVIEZhbiBTcGVlZCBDb250cm9sbGVy"),J,A)])
class K(H):
    _attr_should_poll=F;_attr_translation_key=decode__("Y3B1")
    def __init__(A,hass,unique_id,name,supported_features,api,pin=13,lower_threshold=40,higher_threshold=50):
        B=supported_features;A._pin=pin;A._state=True;A._higher_temperature_threshold=higher_threshold;A._lower_temperature_threshold=lower_threshold;A._listener=C;A._api=api;A.hass=hass;A._unique_id=unique_id;A._attr_supported_features=B;A._percentage=C;A._attr_name=name
        if B&D.OSCILLATE:A._oscillating=F
        if B&D.DIRECTION:A._direction=decode__("Zm9yd2FyZA==")
        A.setup_light()
    def setup_light(B):
        try:A.setmode(A.BCM);A.setup(B._pin,A.OUT);B._pwm=A.PWM(B._pin,100);B._pwm.start(50)
        except RuntimeError:E.error(decode__("R1BJTyBQV00gYWxyZWFkeSBpbiB1c2U="));B._pwm=C;B._attr_available=F
    async def async_added_to_hass(A):
        @I
        async def B(event):
            try:
                B=event.data.get(decode__("dGVtcGVyYXR1cmU="))
                if B is C:return
                if B>A._higher_temperature_threshold:await A.async_turn_on(percentage=100)
                elif B>A._lower_temperature_threshold:await A.async_turn_on(percentage=50)
                else:await A.async_turn_on(percentage=25)
            except G as D:E.error(format_str__("RXJyb3IgYWRqdXN0aW5nIGZhbiBzcGVlZDoge19fdmFyMH0=", __var0=D))
        A._listener=A.hass.bus.async_listen(decode__("Y3B1X3RlbXBlcmF0dXJl"),B)
    @B
    def name(self):return self._attr_name
    @B
    def icon(self):return decode__("bWRpOmZhbg==")
    @B
    def is_on(self):return self._state
    @B
    def unique_id(self):return self._unique_id
    @B
    def percentage(self):return self._percentage
    def log_fan_state(A):E.info(format_str__("RmFuIFN0YXRlIC0gUGVyY2VudGFnZToge19fdmFyMH0sIFRlbXBlcmF0dXJlIFJhbmdlOiB7X192YXIxfS17X192YXIyfQ==", __var0=A._percentage, __var1=A._lower_temperature_threshold, __var2=A._higher_temperature_threshold))
    @B
    def supported_features(self):return self._attr_supported_features
    async def async_will_remove_from_hass(B):
        if B._listener:B._listener()
        if B._pwm:
            try:B._pwm.stop();A.cleanup(B._pin)
            except G as C:E.error(format_str__("RXJyb3IgY2xlYW5pbmcgdXAgR1BJTzoge19fdmFyMH0=", __var0=C))
    async def async_set_percentage(A,percentage):A._percentage=percentage;A._pwm.ChangeDutyCycle(A._percentage);A._state=True;A.async_write_ha_state()
    async def async_turn_on(B,percentage=C,**D):
        A=percentage
        if A is C:A=50
        await B.async_set_percentage(A)
    async def async_turn_off(A,**B):A._pwm.ChangeDutyCycle(0);A._state=F;A.async_write_ha_state()