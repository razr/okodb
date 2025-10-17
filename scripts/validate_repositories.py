import json
import glob
from jsonschema import validate, ValidationError

schema_file = "okodb/schemas/repository.schema.json"
records_dir = "okodb/repositories/*.json"

with open(schema_file) as f:
    schema = json.load(f)

for file_path in glob.glob(records_dir):
    with open(file_path) as f:
        record = json.load(f)
    try:
        validate(instance=record, schema=schema)
        print(f"{file_path} ✅ valid")
    except ValidationError as e:
        print(f"{file_path} ❌ invalid: {e.message}")

