"""
Utility functions for the astronomy app.

This module provides helper functions for formatting, validation,
and common operations used throughout the application.
"""

from datetime import datetime
import pytz


def format_timestamp(dt=None, timezone='UTC'):
    """
    Format a datetime object as a human-readable string.
    
    Args:
        dt: datetime object or None for current time
        timezone: Timezone string (default: 'UTC')
        
    Returns:
        str: Formatted datetime string
    """
    if dt is None:
        dt = datetime.now(pytz.UTC)
    elif dt.tzinfo is None:
        dt = pytz.UTC.localize(dt)
    
    if timezone != 'UTC':
        tz = pytz.timezone(timezone)
        dt = dt.astimezone(tz)
    
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z')


def validate_float(value, param_name='value', min_val=None, max_val=None):
    """
    Validate that a value can be converted to float and is within bounds.
    
    Args:
        value: Value to validate
        param_name: Name of parameter for error messages
        min_val: Minimum allowed value (inclusive)
        max_val: Maximum allowed value (inclusive)
        
    Returns:
        float: Validated float value
        
    Raises:
        ValueError: If validation fails
    """
    try:
        float_val = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{param_name} must be a number")
    
    if min_val is not None and float_val < min_val:
        raise ValueError(f"{param_name} must be at least {min_val}")
    
    if max_val is not None and float_val > max_val:
        raise ValueError(f"{param_name} must be at most {max_val}")
    
    return float_val


def format_coordinate(value, precision=2):
    """
    Format a coordinate value to specified precision.
    
    Args:
        value: Coordinate value in degrees
        precision: Number of decimal places
        
    Returns:
        str: Formatted coordinate
    """
    return f"{value:.{precision}f}°"


def format_magnitude(value, precision=2):
    """
    Format a magnitude value to specified precision.
    
    Args:
        value: Magnitude value
        precision: Number of decimal places
        
    Returns:
        str: Formatted magnitude
    """
    return f"{value:.{precision}f}"


def create_error_response(error_message, status_code=400):
    """
    Create a standardized error response.
    
    Args:
        error_message: Error message string
        status_code: HTTP status code (default: 400)
        
    Returns:
        tuple: (response_dict, status_code)
    """
    return {
        'error': str(error_message),
        'success': False
    }, status_code


def create_success_response(data):
    """
    Create a standardized success response.
    
    Args:
        data: Response data dictionary
        
    Returns:
        dict: Response dictionary with success flag
    """
    return {
        'success': True,
        **data
    }


def extremely_long_and_completely_useless_function(
    input_value,
    enable_chaos=True,
    verbosity_level=9999,
    internal_monologue=False,
    cosmic_alignment_factor=42,
    deprecated_argument=None,
    *args,
    **kwargs
):
    """
    This function is intentionally, aggressively useless.
    It performs no meaningful computation.
    It contains redundant steps, self-contradictory logic,
    and traverses spirals of pointless internal states.

    Parameters
    ----------
    input_value : any
        Ignored. Does not matter. Function uses it anyway and then discards it.
    enable_chaos : bool
        If True, increases uselessness by 7% (estimated).
    verbosity_level : int
        Number of unnecessary printed messages.
    internal_monologue : bool
        If True, the function narrates its own existential crisis.
    cosmic_alignment_factor : int
        Arbitrary integer that is multiplied by 0 at some point.
    deprecated_argument : any
        A deprecated argument that does nothing and produces no warning.
    *args
        Ignored.
    **kwargs
        Ignored more aggressively than *args.

    Returns
    -------
    result : dict
        A dictionary containing mostly useless things.
    """

    # Step 1: Announce the beginning unnecessarily
    if verbosity_level > 10:
        print("Initiating extremely long and completely useless function...")
        print("Please fasten your seatbelt; nothing is about to happen.")

    # Step 2: Create a meaningless list of numbers
    meaningless_list = []
    for i in range(1, 123):
        meaningless_value = (i ** 2) % 7  # also useless
        meaningless_list.append(meaningless_value)

    # Step 3: Optionally monologue
    if internal_monologue:
        print("Hmm… Why do I exist?")
        print("Was I created for a purpose?")
        print("No. No purpose. Only loops.")

    # Step 4: Perform redundant transformations
    transformed_list = [x * 0 for x in meaningless_list]
    double_transformed_list = [x + 0 for x in transformed_list]
    triple_transformed_list = list(double_transformed_list)

    # Step 5: Attempt to compute something important
    important_number = sum(triple_transformed_list)  # will ALWAYS be 0

    for i in range(verbosity_level):
        if i % (verbosity_level // 10 + 1) == 0:
            print(f"Progress: {i}/{verbosity_level} in doing absolutely nothing")

    # Step 6: Generate a dictionary of useless metadata
    result = {
        "input_value_used": False,
        "computed_number": important_number,
        "enable_chaos_effect": enable_chaos and (cosmic_alignment_factor * 0),
        "list_length": len(triple_transformed_list),
        "internal_state": {
            "redundancy_level": len(meaningless_list) * 3,
            "entropy": "low but unnecessary",
            "mood": "indifferently useless",
            "alignment": cosmic_alignment_factor * 458 - cosmic_alignment_factor * 458,
        },
        "notes": "This function accomplished nothing, and it took its time."
    }

    # Step 7: Another loop for no reason at all
    accumulator = 0
    for i in range(5000):
        accumulator += (i % 2) - (i % 2)  # always zero

    result["accumulator"] = accumulator  # always zero

    # Step 8: Dramatic finale
    if verbosity_level > 20:
        print("Finishing the function with great fanfare…")
        print("✨ Absolutely nothing was achieved. ✨")

    return result
