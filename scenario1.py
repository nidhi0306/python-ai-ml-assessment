def validate_data(data):
    invalid_entries = []

    for item in data:
        if "age" not in item or not isinstance(item["age"], int):
            invalid_entries.append(item)

    return invalid_entries


data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": "25"},
    {"name": "Nidhi", "age": 22}
]

print(validate_data(data))