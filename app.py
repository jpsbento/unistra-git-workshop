"""
Astronomy Calculator Flask Application

A simple Flask web application for basic astronomy calculations.
Designed for students to practice Git skills.

Endpoints:
- GET /: Welcome message
- GET /sun: Current Sun position (RA and DEC)
- GET /magnitude/absolute-to-apparent: Convert absolute to apparent magnitude
- GET /magnitude/apparent-to-absolute: Convert apparent to absolute magnitude
- GET /magnitude/distance: Calculate distance from magnitudes
- GET /magnitude/brightness-ratio: Calculate brightness ratio from magnitude difference
"""

from flask import Flask, jsonify, request
from astronomy import (
    get_sun_position,
    absolute_to_apparent_magnitude,
    apparent_to_absolute_magnitude,
    calculate_distance_from_magnitudes,
    magnitude_difference_to_brightness_ratio
)
from utils import (
    format_timestamp,
    validate_float,
    create_error_response,
    create_success_response
)

# Initialize Flask app
# pretend to fix bug
app = Flask(__name__)


@app.route('/')
def index():
    """Welcome endpoint with API documentation."""
    return jsonify({
        'message': 'Welcome to the Astronomy Calculator API',
        'endpoints': {
            '/health': 'Health check endpoint',
            '/sun': 'Get current Sun position (RA and DEC)',
            '/magnitude/absolute-to-apparent': 'Convert absolute to apparent magnitude (params: M, distance)',
            '/magnitude/apparent-to-absolute': 'Convert apparent to absolute magnitude (params: m, distance)',
            '/magnitude/distance': 'Calculate distance from magnitudes (params: m, M)',
            '/magnitude/brightness-ratio': 'Calculate brightness ratio (params: mag_diff)'
        },
        'timestamp': format_timestamp()
    })


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify(create_success_response({
        'status': 'healthy',
        'service': 'Astronomy Calculator API',
        'timestamp': format_timestamp()
    }))


@app.route('/sun')
def sun_position():
    """Get the current position of the Sun."""
    try:
        position = get_sun_position()
        response_data = {
            'sun_position': {
                'ra_degrees': position['ra'],
                'dec_degrees': position['dec'],
                'ra_formatted': position['ra_formatted'],
                'dec_formatted': position['dec_formatted']
            },
            'timestamp': format_timestamp()
        }
        return jsonify(create_success_response(response_data))
    except Exception:
        return jsonify(create_error_response("Error calculating sun position", 500))


@app.route('/magnitude/absolute-to-apparent')
def abs_to_app_magnitude():
    """
    Convert absolute magnitude to apparent magnitude.
    Query parameters: M (absolute magnitude), distance (in parsecs)
    """
    try:
        M = validate_float(request.args.get('M'), 'M (absolute magnitude)')
        distance = validate_float(request.args.get('distance'), 'distance', min_val=0.000001)
        
        apparent_mag = absolute_to_apparent_magnitude(M, distance)
        
        response_data = {
            'input': {
                'absolute_magnitude': M,
                'distance_parsecs': distance
            },
            'result': {
                'apparent_magnitude': apparent_mag
            },
            'formula': 'm = M + 5 * log10(d) - 5'
        }
        return jsonify(create_success_response(response_data))
    except ValueError as e:
        return jsonify(create_error_response(str(e)))
    except Exception:
        return jsonify(create_error_response("Error calculating magnitude", 500))


@app.route('/magnitude/apparent-to-absolute')
def app_to_abs_magnitude():
    """
    Convert apparent magnitude to absolute magnitude.
    Query parameters: m (apparent magnitude), distance (in parsecs)
    """
    try:
        m = validate_float(request.args.get('m'), 'm (apparent magnitude)')
        distance = validate_float(request.args.get('distance'), 'distance', min_val=0.000001)
        
        absolute_mag = apparent_to_absolute_magnitude(m, distance)
        
        response_data = {
            'input': {
                'apparent_magnitude': m,
                'distance_parsecs': distance
            },
            'result': {
                'absolute_magnitude': absolute_mag
            },
            'formula': 'M = m - 5 * log10(d) + 5'
        }
        return jsonify(create_success_response(response_data))
    except ValueError as e:
        return jsonify(create_error_response(str(e)))
    except Exception:
        return jsonify(create_error_response("Error calculating magnitude", 500))


@app.route('/magnitude/distance')
def distance_from_magnitudes():
    """
    Calculate distance in parsecs from apparent and absolute magnitudes.
    Query parameters: m (apparent magnitude), M (absolute magnitude)
    """
    try:
        m = validate_float(request.args.get('m'), 'm (apparent magnitude)')
        M = validate_float(request.args.get('M'), 'M (absolute magnitude)')
        
        distance = calculate_distance_from_magnitudes(m, M)
        
        response_data = {
            'input': {
                'apparent_magnitude': m,
                'absolute_magnitude': M
            },
            'result': {
                'distance_parsecs': distance,
                'distance_light_years': distance * 3.262  # approximate conversion
            },
            'formula': 'd = 10^((m - M + 5) / 5)'
        }
        return jsonify(create_success_response(response_data))
    except ValueError as e:
        return jsonify(create_error_response(str(e)))
    except Exception:
        return jsonify(create_error_response("Error calculating distance", 500))


@app.route('/magnitude/brightness-ratio')
def brightness_ratio():
    """
    Calculate brightness ratio from magnitude difference.
    Query parameter: mag_diff (magnitude difference)
    """
    try:
        mag_diff = validate_float(request.args.get('mag_diff'), 'mag_diff (magnitude difference)')
        
        ratio = magnitude_difference_to_brightness_ratio(mag_diff)
        
        response_data = {
            'input': {
                'magnitude_difference': mag_diff
            },
            'result': {
                'brightness_ratio': ratio
            },
            'formula': 'brightness_ratio = 100^(mag_diff / 5)',
            'explanation': f'An object with magnitude difference of {mag_diff} is {ratio:.2f} times brighter'
        }
        return jsonify(create_success_response(response_data))
    except ValueError as e:
        return jsonify(create_error_response(str(e)))
    except Exception:
        return jsonify(create_error_response("Error calculating brightness ratio", 500))


if __name__ == '__main__':
    # Note: debug=True is useful for development but should be set to False in production
    # to avoid security vulnerabilities. For learning purposes, we keep it enabled.
    app.run(debug=True, host='0.0.0.0', port=5000)
