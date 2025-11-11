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
