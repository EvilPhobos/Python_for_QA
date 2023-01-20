def get_info_response() -> dict:
    return {
        "type": "object",
        "properties": {
            "type": {
                "type": "string"
            },
            "title": {
                "type": "string"
            },
            "id": {
                "type": "string",
                "format": "uuid"
            },
            "creation_date": {
                "type": "string",
                "format": "date"
            },
            "updated_date_time": {
                "type": "string",
                "format": "date-time"
            }
        },
        "required": [
            "creation_date",
            "id",
            "title",
            "type",
            "updated_date_time"
        ],
        "additionalProperties": False
    }


def get_info_response_neg() -> dict:
    return {
        "message": "There is no such book | books."
    }


def get_latest_response(item_count: int = 0) -> dict:
    return {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "id": {
                    "type": "string",
                    "format": "uuid"
                },
                "creation_date": {
                    "type": "string",
                    "format": "date"
                },
                "updated_date_time": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "creation_date",
                "id",
                "title",
                "type",
                "updated_date_time"
            ],
            "additionalProperties": False
        },
        "minItems": item_count
    }


def get_ids_response() -> dict:
    return {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "id": {
                    "type": "string",
                    "format": "uuid"
                },
                "creation_date": {
                    "type": "string",
                    "format": "date"
                },
                "updated_date_time": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "creation_date",
                "id",
                "title",
                "type",
                "updated_date_time"
            ],
            "additionalProperties": False
        },
        "minItems": 1
    }


def get_manipulation() -> dict:
    return {
        "message": "No implementation for `GET` method"
    }
