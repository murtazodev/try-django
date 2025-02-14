from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError

valid_unit_of_measurements = ['oz', 'lbs', 'pounds', 'gram']

def validate_unit_of_measurement(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{e} is not a valid unit of measurement")
    except:
        raise ValidationError(f"{value} is not a valid unit of measurement")