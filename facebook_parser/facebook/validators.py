
import json
from jsonschema import validate, ValidationError


def validate_json_schema(uploaded_file):
    schema = {
        "type": "object",
        "properties": {
            "participants": {"type": "array"},
            "messages": {"type": "array"},
            "title": {"type": "string"},
            "is_still_participant": {"type": "boolean"},
            "thread_type": {"type": "string"},
            "thread_path": {"type": "string"}
        }
    }
    if uploaded_file.content_type != "application/json":
        with open(uploaded_file) as json_file:
            fb_chat = json.load(json_file)
            try:
                validate(instance=fb_chat, schema=schema)
            except ValidationError as valid_error:
                return f"{valid_error} Your file is corrupted. Try another one"
