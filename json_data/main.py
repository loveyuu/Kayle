# encoding=utf-8
from jsonschema import validate, exceptions


def ac():
    data = {
        "order_id": ['1'],
        "gps": {
            "latitude": "31.2",
            "longitude": "121.2",
            "gps_kind": 3
        }
    }

    st = {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1,
            },
            "gps": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "string"},
                    "longitude": {"type": "string"},
                    "gps_kind": {"type": "integer"},
                },
                "required": ["latitude", "longitude", "gps_kind"]
            },
        },
        "required": ["order_id"]
    }
    try:
        print validate(data, st)
    except exceptions.ValidationError as err:
        print err.validator

ac()
