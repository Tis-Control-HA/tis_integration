<<<<<<< Updated upstream
from __future__ import annotations
from TISControlProtocol import *
import logging,voluptuous as vol
from homeassistant.config_entries import ConfigFlow,ConfigFlowResult
from homeassistant.const import CONF_PORT
from homeassistant.core import callback
from.const import DOMAIN
_LOGGER=logging.getLogger(__name__)
schema=vol.Schema({vol.Required(CONF_PORT):int},required=True)
class TISConfigFlow(ConfigFlow,domain=DOMAIN):
    VERSION=1
    async def async_step_user(C,user_input=None):
        A=user_input;B={}
        if A is not None:
            logging.info(beta__("cmVjZWl2ZWQgdXNlciBpbnB1dCB7X192YXIwfQ==", __var0=A));D=await C.validate_port(A[CONF_PORT])
            if not D:B[alpha__("YmFzZQ==")]=alpha__("aW52YWxpZF9wb3J0");logging.error(beta__("UHJvdmlkZWQgcG9ydCBpcyBpbnZhbGlkOiB7X192YXIwfQ==", __var0=A[CONF_PORT]))
            if not B:return C.async_create_entry(title=alpha__("VElTIENvbnRyb2wgQnJpZGdl"),data=A)
            else:logging.error(beta__("RXJyb3JzIG9jY3VycmVkOiB7X192YXIwfQ==", __var0=B));return C._show_setup_form(B)
        return C._show_setup_form(errors=B)
    @callback
    def _show_setup_form(self,errors=None):A=errors;return self.async_show_form(step_id=alpha__("dXNlcg=="),data_schema=schema,errors=A if A else{})
    async def validate_port(A,port):
        if isinstance(port,int):
            if 1<=port<=65535:return True
=======
<<<<<<< HEAD
from __future__ import annotations
from TISControlProtocol import *
import logging,voluptuous as vol
from homeassistant.config_entries import ConfigFlow,ConfigFlowResult
from homeassistant.const import CONF_PORT
from homeassistant.core import callback
from.const import DOMAIN
_LOGGER=logging.getLogger(__name__)
schema=vol.Schema({vol.Required(CONF_PORT):int},required=True)
class TISConfigFlow(ConfigFlow,domain=DOMAIN):
    VERSION=1
    async def async_step_user(A,user_input=None):
        B=user_input;C={}
        if B is not None:
            D=beta__("dGlzX2NvbnRyb2w6e19fdmFyMH0=", __var0=B[CONF_PORT]);await A.async_set_unique_id(D);A._abort_if_unique_id_configured();_LOGGER.info(beta__("cmVjZWl2ZWQgdXNlciBpbnB1dCB7X192YXIwfQ==", __var0=B));E=await A.validate_port(B[CONF_PORT])
            if not E:C[alpha__("YmFzZQ==")]=alpha__("aW52YWxpZF9wb3J0");_LOGGER.error(beta__("UHJvdmlkZWQgcG9ydCBpcyBpbnZhbGlkOiB7X192YXIwfQ==", __var0=B[CONF_PORT]))
            if not C:return A.async_create_entry(title=alpha__("VElTIENvbnRyb2wgQnJpZGdl"),data=B)
            else:_LOGGER.error(beta__("RXJyb3JzIG9jY3VycmVkOiB7X192YXIwfQ==", __var0=C));return A._show_setup_form(C)
        return A._show_setup_form(errors=C)
    @callback
    def _show_setup_form(self,errors=None):A=errors;return self.async_show_form(step_id=alpha__("dXNlcg=="),data_schema=schema,errors=A if A else{})
    async def validate_port(A,port):
        if isinstance(port,int):
            if 1<=port<=65535:return True
=======
from __future__ import annotations
from TISControlProtocol import *
import logging,voluptuous as vol
from homeassistant.config_entries import ConfigFlow,ConfigFlowResult
from homeassistant.const import CONF_PORT
from homeassistant.core import callback
from.const import DOMAIN
_LOGGER=logging.getLogger(__name__)
schema=vol.Schema({vol.Required(CONF_PORT):int},required=True)
class TISConfigFlow(ConfigFlow,domain=DOMAIN):
    VERSION=1
    async def async_step_user(C,user_input=None):
        A=user_input;B={}
        if A is not None:
            logging.info(beta__("cmVjZWl2ZWQgdXNlciBpbnB1dCB7X192YXIwfQ==", __var0=A));D=await C.validate_port(A[CONF_PORT])
            if not D:B[alpha__("YmFzZQ==")]=alpha__("aW52YWxpZF9wb3J0");logging.error(beta__("UHJvdmlkZWQgcG9ydCBpcyBpbnZhbGlkOiB7X192YXIwfQ==", __var0=A[CONF_PORT]))
            if not B:return C.async_create_entry(title=alpha__("VElTIENvbnRyb2wgQnJpZGdl"),data=A)
            else:logging.error(beta__("RXJyb3JzIG9jY3VycmVkOiB7X192YXIwfQ==", __var0=B));return C._show_setup_form(B)
        return C._show_setup_form(errors=B)
    @callback
    def _show_setup_form(self,errors=None):A=errors;return self.async_show_form(step_id=alpha__("dXNlcg=="),data_schema=schema,errors=A if A else{})
    async def validate_port(A,port):
        if isinstance(port,int):
            if 1<=port<=65535:return True
>>>>>>> f263abcb1da29b0f40c48adec4186527495f5dce
>>>>>>> Stashed changes
        return False