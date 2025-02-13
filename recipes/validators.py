from django.core.exceptions import ValidationError

valid_unit_of_measurements = ['oz', 'lbs', 'pounds', 'gram']

def validate_unit_of_measurement(value):
    if value not in valid_unit_of_measurements:
        raise ValidationError(f"{value} is not a valid unit of measurement")