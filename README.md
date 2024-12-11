# Fat Finisher
**Fat Finisher** is a calorie and exercise tracking app. It helps users:
- Track calories gained from food items and portion sizes.  
- Track calories burned from exercises based on weight and duration.  
- Estimate calories burned while walking or biking between two locations using Google Maps.

## Features
1. **Calorie Tracker**: Log food items and portion sizes to calculate total calories consumed.  
2. **Exercise Tracker**: Track calories burned from exercises like running, cycling, or swimming.  
3. **Map-Based Activity Tracking**: Use Google Maps to estimate calories burned while traveling.

## Requirements
- **Python 3.8+**  
- **Dependencies**: Install the required libraries using `r.txt`.  

## How to Run
- [Download the project](https://github.com/Ruthlesstoadface/FatFinisher/archive/refs/heads/main.zip) and extract it.  
- Install the required packages by running the following command in the project folder:
   ```bash
   pip install -r r.txt
   ```
- Start the application by running the UI. Do not run the `ryan_app.py` - it is just the backend.
   ```bash
   streamlit run ryan_ui.py
   ```
- The application will run in your default browser.

## Usage
- **Calorie Tracker**: Log food items and portion sizes to track calorie intake.  
- **Exercise Tracker**: Enter your weight, select exercises, and input duration to calculate calories burned.  
- **Distance and Calorie Tracker**: Input starting and ending locations, select travel mode (walking or biking), and calculate calories burned.
