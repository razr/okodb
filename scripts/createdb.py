import os
import json

def load_json_files(directory):
    """Load all JSON files from a directory into a list."""
    data = []
    if not os.path.exists(directory):
        return data
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                try:
                    data.append(json.load(file))
                except json.JSONDecodeError as e:
                    print(f"Error decoding {filepath}: {e}")
    return data

def main():
    # Define base directory and subdirectories
    base_dir = "okodb"
    subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    # Aggregate data
    db = {}
    for subdir in subdirs:
        dir_path = os.path.join(base_dir, subdir)
        db[subdir] = load_json_files(dir_path)

    # Output to okodb.json
    output_file = "okodb.json"
    with open(output_file, "w") as file:
        json.dump(db, file, indent=2)

    print(f"Combined database written to {output_file}")

if __name__ == "__main__":
    main()
