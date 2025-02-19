from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)
A=property
from datetime import timedelta as C
import logging as D
from TISControlProtocol.api import TISApi,TISPacket
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler as E
from homeassistant.components.weather import ATTR_CONDITION_CLOUDY,ATTR_CONDITION_EXCEPTIONAL,ATTR_CONDITION_FOG,ATTR_CONDITION_HAIL,ATTR_CONDITION_LIGHTNING,ATTR_CONDITION_LIGHTNING_RAINY,ATTR_CONDITION_PARTLYCLOUDY,ATTR_CONDITION_POURING,ATTR_CONDITION_RAINY,ATTR_CONDITION_SNOWY,ATTR_CONDITION_SNOWY_RAINY,ATTR_CONDITION_SUNNY,ATTR_CONDITION_WINDY,ATTR_CONDITION_WINDY_VARIANT,ATTR_FORECAST_CONDITION,ATTR_FORECAST_NATIVE_PRECIPITATION,ATTR_FORECAST_NATIVE_TEMP,ATTR_FORECAST_NATIVE_TEMP_LOW,ATTR_FORECAST_NATIVE_WIND_SPEED,ATTR_FORECAST_TIME,ATTR_FORECAST_WIND_BEARING,Forecast,UnitOfTemperature as B,WeatherEntity as F,WeatherEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import MATCH_ALL as G,CONF_LATITUDE,CONF_LONGITUDE,CONF_NAME,Platform,UnitOfLength,UnitOfPrecipitationDepth,UnitOfPressure,UnitOfSpeed,UnitOfTemperature as B
from homeassistant.core import Event,HomeAssistant,callback as H
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as I
from.import TISConfigEntry
J=E()
async def async_setup_entry(hass,entry,async_add_devices):A=entry.runtime_data.api;B=[K(api=A,device_id=[1,254],gateway=decode__("MTkyLjE2OC4xLjQ="))];async_add_devices(B,update_before_add=True)
class K(F):
    def __init__(A,api,device_id,gateway):A.api=api;A.device_id=device_id;A.gateway=gateway;A.update_packet=J.generate_weather_update_packet(A);A.listener=None;A._attr_unit_of_measurement=B.CELSIUS;A._attr_update_interval=C(seconds=10);I(A.api.hass,A.async_update,A._attr_update_interval)
    async def async_added_to_hass(A):
        @H
        def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[decode__("ZmVlZGJhY2tfdHlwZQ==")]==decode__("d2VhdGhlcl9mZWVkYmFjaw=="):A._attr_uv_index=float(B.data[decode__("dXY=")]);A._attr_native_temperature=B.data[decode__("dGVtcGVyYXR1cmU=")];D.info(format_str__("ZXZlbnQgZGF0YSB7X192YXIwfQ==", __var0=B.data))
            A.schedule_update_ha_state()
        A.listener=A.hass.bus.async_listen(G,B)
    async def async_will_remove_from_hass(A):A.listener=None
    async def async_update(A,*B,**C):await A.api.protocol.sender.send_packet(A.update_packet)
    @A
    def name(self):return decode__("VElTIFdlYXRoZXIgU3RhdGlvbg==")
    @A
    def wind_bearing(self):return self._attr_wind_bearing
    @A
    def native_temperature(self):return self._attr_native_temperature
    @A
    def native_temperature_unit(self):return B.CELSIUS
    @A
    def humidity(self):return self._attr_humidity
    @A
    def native_wind_speed(self):return self._attr_native_wind_speed
    @A
    def native_wind_gust_speed(self):return self._attr_native_wind_gust_speed
    @A
    def uv_index(self):return self._attr_uv_index
    @A
    def condition(self):return self._attr_condition