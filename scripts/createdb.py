#!/usr/bin/env python3
import os
import json
import argparse

def load_json_files(directory):
    """Load all JSON files from a directory into a list."""
    data = []
    if not os.path.exists(directory):
        return data
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, "r") as file:
                    data.append(json.load(file))
            except json.JSONDecodeError as e:
                print(f"Error decoding {filepath}: {e}")
    return data

def main():
    parser = argparse.ArgumentParser(
        description="Combine OkodB JSON files into a single database."
    )
    parser.add_argument(
        "--output",
        "-o",
        default=os.path.join(os.path.dirname(__file__), "..", "okodb.json"),
        help="Path to output JSON file (default: okodb.json in project root)"
    )
    parser.add_argument(
        "--okodb-dir",
        default=os.path.join(os.path.dirname(__file__), "..", "okodb"),
        help="Path to OkodB directory containing errors, fixes, repositories, sdks"
    )
    args = parser.parse_args()

    base_dir = args.okodb_dir

    # Aggregate data
    db = {}
    subdirs = [
        d for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d))
    ]

    for subdir in subdirs:
        dir_path = os.path.join(base_dir, subdir)
        db[subdir] = load_json_files(dir_path)

    # Write combined JSON
    try:
        with open(args.output, "w") as file:
            json.dump(db, file, indent=2)
        print(f"Combined database written to {args.output}")
    except IOError as e:
        print(f"Error writing {args.output}: {e}")

if __name__ == "__main__":
    main()

