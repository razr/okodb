#!/usr/bin/env python3
import json
import os

def main():
    db_file = os.path.join(os.path.dirname(__file__), "..", "okodb.json")
    
    try:
        with open(db_file) as f:
            db = json.load(f)
    except FileNotFoundError:
        print(f"Database file not found: {db_file}")
        return
    except json.JSONDecodeError as e:
        print(f"Failed to parse {db_file}: {e}")
        return

    # Print summary
    errors = db.get("errors", [])
    fixes = db.get("fixes", [])
    repositories = db.get("repositories", [])
    sdks = db.get("sdks", [])

    print(f"OkodB contains:")
    print(f"  {len(errors)} errors")
    print(f"  {len(fixes)} fixes")
    print(f"  {len(repositories)} repositories")
    print(f"  {len(sdks)} SDKs")
    
    if errors:
        print("\nExample error:")
        e = errors[0]
        print(f"  ID: {e['id']}")
        print(f"  Message: {e['error_message']}")
        print(f"  Repository: {e['repository_id']}")
        print(f"  Fix: {e.get('fix_id', 'none')}")

    if fixes:
        print("\nExample fix:")
        f = fixes[0]
        print(f"  ID: {f['id']}")
        print(f"  Option: {f.get('option', '')}")
        print(f"  Description: {f.get('description', '')}")

if __name__ == "__main__":
    main()
