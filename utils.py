
import hashlib
import json


def calculate_hash(data):
    """Convert data into a deterministic SHA-256 hash."""
    encoded_data = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    ).encode("utf-8")

    return hashlib.sha256(encoded_data).hexdigest()
