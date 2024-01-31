from cerberus import Validator

def validate_input(steps, path):
    # Validation of input data
    schema = {'steps': {'type': 'integer', 'min': 2, 'max': 10**6},
              'path': {'type': 'string', 'regex': '^[UD]*$'}}
    v = Validator(schema)
    if not v.validate({'steps': steps, 'path': path}):
        errors = [f"{error}: {message}" for error, message in v.errors.items()]
        raise ValueError("Error in input data:\n" + '\n'.join(errors))

def counting_valleys(steps, path):
    # Convert the path to a list of integers representing altitude changes
    elevation_changes = [0]  # Start at sea level
    for step in path:
        if step == 'U':
            elevation_changes.append(elevation_changes[-1] + 1)
        else:
            elevation_changes.append(elevation_changes[-1] - 1)

    # Count the number of times a valley is crossed
    valleys = 0
    in_valley = False

    for i in range(1, len(elevation_changes)):
        if elevation_changes[i-1:i+1] == [0, -1] and not in_valley:  # Entry to a valley
            in_valley = True
        elif elevation_changes[i-1:i+1] == [-1, 0] and in_valley:  # Exit from a valley
            valleys += 1
            in_valley = False

    return valleys
