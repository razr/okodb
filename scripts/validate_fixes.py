#!/usr/bin/env python3
import os
import glob
import json
import argparse
from jsonschema import validate, ValidationError

def main():
    parser = argparse.ArgumentParser(
        description="Validate JSON fix records against a JSON schema."
    )
    parser.add_argument(
        "--schema",
        "-s",
        default=os.path.join(os.path.dirname(__file__), "..", "okodb", "schemas", "fix.schema.json"),
        help="Path to the JSON schema file"
    )
    parser.add_argument(
        "--records",
        "-r",
        default=os.path.join(os.path.dirname(__file__), "..", "okodb", "fixes", "*.json"),
        help="Glob pattern to match JSON fix records"
    )
    args = parser.parse_args()

    # Load schema
    try:
        with open(args.schema) as f:
            schema = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading schema {args.schema}: {e}")
        return

    # Validate each record
    for file_path in glob.glob(args.records):
        try:
            with open(file_path) as f:
                record = json.load(f)
            validate(instance=record, schema=schema)
            print(f"{file_path} ✅ valid")
        except (IOError, json.JSONDecodeError) as e:
            print(f"{file_path} ❌ cannot read/parse JSON: {e}")
        except ValidationError as e:
            print(f"{file_path} ❌ invalid: {e.message}")

if __name__ == "__main__":
    main()
