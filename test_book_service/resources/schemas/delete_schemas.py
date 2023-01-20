def delete_response() -> dict:
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


def delete_response_neg() -> dict:
    return {
        "message": "There is no such book | books."
    }
