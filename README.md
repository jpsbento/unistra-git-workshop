# unistra-git-workshop
An example repository for a git workshop

## Astronomy Calculator App

A simple Flask web application that provides basic astronomy calculations. Perfect for students to practice Git collaboration skills!

### Features

- Get current Sun position (Right Ascension and Declination)
- Convert between absolute and apparent magnitudes
- Calculate distances from magnitude measurements
- Calculate brightness ratios from magnitude differences

### Setup

1. Clone the repository:
```bash
git clone https://github.com/jpsbento/unistra-git-workshop.git
cd unistra-git-workshop
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Flask server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### API Endpoints

#### Get Sun Position
```bash
curl http://localhost:5000/sun
```

#### Convert Absolute to Apparent Magnitude
```bash
curl "http://localhost:5000/magnitude/absolute-to-apparent?M=4.83&distance=10"
```

#### Convert Apparent to Absolute Magnitude
```bash
curl "http://localhost:5000/magnitude/apparent-to-absolute?m=-26.74&distance=0.0000158"
```

#### Calculate Distance from Magnitudes
```bash
curl "http://localhost:5000/magnitude/distance?m=-26.74&M=4.83"
```

#### Calculate Brightness Ratio
```bash
curl "http://localhost:5000/magnitude/brightness-ratio?mag_diff=5"
```

### Project Structure

- `app.py` - Main Flask application with API endpoints
- `astronomy.py` - Astronomy calculation functions
- `utils.py` - Utility functions for formatting and validation
- `requirements.txt` - Python dependencies

### Contributing

This repository is designed for learning Git! Feel free to:
- Add new astronomy calculations
- Improve error handling
- Add unit tests
- Enhance documentation
- Create a web interface

### License

See LICENSE file for details.
