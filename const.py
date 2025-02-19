from __future__ import annotations
import base64

def decode__(s):
    return base64.b64decode(s).decode()

def format_str__(encoded_template, **kwargs):
    template = base64.b64decode(encoded_template).decode()
    return template.format(**kwargs)


from homeassistant.components.climate import (
    ATTR_TEMPERATURE,
    FAN_AUTO,
    FAN_HIGH,
    FAN_LOW,
    FAN_MEDIUM,
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
    UnitOfTemperature,
)

DOMAIN = decode__("dGlzX2NvbnRyb2w=")

DEVICES_DICT = {
    (0x1B, 0xBA): decode__("UkNVLThPVVQtOElO"),
    (0x0B, 0xE9): decode__("U0VDLVNN"),
    (0x80, 0x58): decode__("SVAtQ09NLVBPUlQ="),
    (0x01, 0xA8): decode__("UkxZLTRDSC0xMA=="),
    (0x23, 0x32): decode__("TFVOQS1URlQtNDM="),
    (0x80, 0x25): decode__("VkVOLTNTLTNSLUhDLUJVUw=="),
    (0x80, 0x38): decode__("QlVTLUVTLUlS"),
    (0x02, 0x5A): decode__("RElNLTJDSC02QQ=="),
    (0x02, 0x58): decode__("RElNLTZDSC0yQQ=="),
    (0x00, 0x76): decode__("NERJLUlO"),
    (0x80, 0x2B): decode__("MjRSMjBa"),
    (0x20, 0x58): decode__("RElNLTZDSC0yQQ=="),
    (0x1B, 0xB6): decode__("VElTLVRFLURJTS00Q0gtMUE="),
    (0x80, 0x2D): decode__("VElTLVJDVS0yME9VVC0yMElO"),
    (0x01, 0xB8): decode__("VElTLVZMQy0xMkNILTEwQQ=="),
    (0x01, 0xAA): decode__("VElTLVZMQy02Q0gtM0E="),
}

TEMPERATURE_RANGES = {
    HVACMode.COOL: {
        decode__("bWlu"): (15.0, 59.0),
        decode__("bWF4"): (26.0, 79.0),
        decode__("dGFyZ2V0"): (20.0, 68.0),
        decode__("cGFja2V0X21vZGVfaW5kZXg="): 0,
    },
    HVACMode.HEAT: {
        decode__("bWlu"): (20.0, 68.0),
        decode__("bWF4"): (35.0, 95.0),
        decode__("dGFyZ2V0"): (28.0, 82.0),
        decode__("cGFja2V0X21vZGVfaW5kZXg="): 1,
    },
    HVACMode.FAN_ONLY: {
        decode__("bWlu"): (15.0, 59.0),
        decode__("bWF4"): (26.0, 79.0),
        decode__("dGFyZ2V0"): (20.0, 68.0),
        decode__("cGFja2V0X21vZGVfaW5kZXg="): 2,
    },
    HVACMode.AUTO: {
        decode__("bWlu"): (15.0, 59.0),
        decode__("bWF4"): (35.0, 95.0),
        decode__("dGFyZ2V0"): (25.0, 77.0),
        decode__("cGFja2V0X21vZGVfaW5kZXg="): 3,
    },
    # off
    HVACMode.OFF: {
        decode__("bWlu"): (15.0, 59.0),
        decode__("bWF4"): (26.0, 79.0),
        decode__("dGFyZ2V0"): (20.0, 68.0),
        decode__("cGFja2V0X21vZGVfaW5kZXg="): 0,
    },
}
FAN_MODES = {
    FAN_AUTO: 0,
    FAN_HIGH: 1,
    FAN_MEDIUM: 2,
    FAN_LOW: 3,
}
