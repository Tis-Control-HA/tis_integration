from __future__ import annotations
from TISControlProtocol import *
F=None
import logging as C,voluptuous as A
from homeassistant.config_entries import ConfigFlow as B,ConfigFlowResult
from homeassistant.const import CONF_PORT as E
from homeassistant.core import callback as D
from.const import DOMAIN
H=C.getLogger(__name__)
G=A.Schema({A.Required(E):int},required=True)
class I(B,domain=DOMAIN):
    VERSION=1
    async def async_step_user(D,user_input=F):
        A=user_input;B={}
        if A is not F:
            C.info(beta__("cmVjaWV2ZWQgdXNlciBpbnB1dCB7X192YXIwfQ==", __var0=A));G=await D.validate_port(A[E])
            if not G:B[alpha__("YmFzZQ==")]=alpha__("aW52YWxpZF9wb3J0");C.error(beta__("UHJvdmlkZWQgcG9ydCBpcyBpbnZhbGlkOiB7X192YXIwfQ==", __var0=A[E]))
            if not B:return D.async_create_entry(title=alpha__("VElTIENvbnRyb2wgQnJpZGdl"),data=A)
            else:C.error(beta__("RXJyb3JzIG9jY3VycmVkOiB7X192YXIwfQ==", __var0=B));return D._show_setup_form(B)
        return D._show_setup_form(errors=B)
    @D
    def _show_setup_form(self,errors=F):A=errors;return self.async_show_form(step_id=alpha__("dXNlcg=="),data_schema=G,errors=A if A else{})
    async def validate_port(A,port):
        if isinstance(port,int):
            if 1<=port<=65535:return True
        return False