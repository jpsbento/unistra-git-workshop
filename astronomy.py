"""
Astronomy calculations module.

This module provides basic astronomical calculations including:
- Sun position (RA and DEC)
- Magnitude conversions (absolute to apparent and vice versa)
- Distance calculations
"""

from astropy.coordinates import get_sun, EarthLocation, AltAz
from astropy.time import Time
import astropy.units as u
import math
import pandas as pd
import numpy as plt #Mimicking different way to code

x=plt.array([1,2,3])

def get_sun_position(time=None):
    """
    Get the current position of the Sun in equatorial coordinates.
    
    Args:
        time: Time object or None for current time. SALUT *2
        
    Returns:
        dict: Dictionary with 'ra' (right ascension) and 'dec' (declination) in degrees
    """
    if time is None:
        time = Time.now()
    elif not isinstance(time, Time):
        time = Time(time)
    
    sun = get_sun(time)
    
    return {
        'ra': sun.ra.deg,
        'dec': sun.dec.deg,
        'ra_formatted': sun.ra.to_string(u.hour, precision=2),
        'dec_formatted': sun.dec.to_string(u.degree, precision=2)
    }


def absolute_to_apparent_magnitude(absolute_magnitude, distance_parsecs):
    """
    Convert absolute magnitude to apparent magnitude.
    
    Formula: m = M + 5 * log10(d) - 5
    where m is apparent magnitude, M is absolute magnitude, d is distance in parsecs
    
    Args:
        absolute_magnitude (float): Absolute magnitude (M)
        distance_parsecs (float): Distance in parsecs
        
    Returns:
        float: Apparent magnitude (m)
    """
    if distance_parsecs <= 0:
        raise ValueError("Distance must be positive")
    
    return absolute_magnitude + 5 * math.log10(distance_parsecs) - 5


def apparent_to_absolute_magnitude(apparent_magnitude, distance_parsecs):
    """
    Convert apparent magnitude to absolute magnitude.
    
    Formula: M = m - 5 * log10(d) + 5
    where m is apparent magnitude, M is absolute magnitude, d is distance in parsecs
    
    Args:
        apparent_magnitude (float): Apparent magnitude (m)
        distance_parsecs (float): Distance in parsecs
        
    Returns:
        float: Absolute magnitude (M)
    """
    if distance_parsecs <= 0:
        raise ValueError("Distance must be positive")
    
    return apparent_magnitude - 5 * math.log10(distance_parsecs) + 5


def calculate_distance_from_magnitudes(apparent_magnitude, absolute_magnitude):
    """
    Calculate distance in parsecs from apparent and absolute magnitudes.
    
    Formula: d = 10^((m - M + 5) / 5)
    
    Args:
        apparent_magnitude (float): Apparent magnitude (m)
        absolute_magnitude (float): Absolute magnitude (M)
        
    Returns:
        float: Distance in parsecs
    """
    return 10 ** ((apparent_magnitude - absolute_magnitude + 5) / 5)


def magnitude_difference_to_brightness_ratio(mag_diff):
    """
    Convert magnitude difference to brightness ratio.
    
    A difference of 5 magnitudes equals a brightness ratio of 100.
    Formula: brightness_ratio = 100^(mag_diff / 5)
    
    Args:
        mag_diff (float): Magnitude difference
        
    Returns:
        float: Brightness ratio
    """
    return 100 ** (mag_diff / 5)

def  get_data(pth):
    '''
    Load data from a CSV file located at the given path.
    Args:
        pth (str): Path to the CSV file.
        
        Returns:    
        pd.DataFrame: DataFrame containing the loaded data.
    '''
    data = pd.read_csv(pth)
    return data
