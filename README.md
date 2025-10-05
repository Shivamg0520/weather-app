# Weather App (CLI)

> A lightweight command-line Python tool that fetches current weather information for any city using WeatherAPI.

---

## 🔍 About
This is a small, easy-to-use CLI weather application written in Python. It calls the WeatherAPI (https://www.weatherapi.com/) to retrieve current weather data (temperature, conditions, humidity, wind, local time, etc.) for a city you specify.

The included `weather_app.py` is a minimal example to help you learn working with APIs and building small utility scripts.

---

## ✨ Features
- Query current weather for any city.
- Shows: city, region, country, timezone, local time, temperature (°C), condition, wind speed (kph), humidity, and "feels like" temperature.
- Minimal dependencies (only `requests`).

---

## 🚀 Quickstart

### 1. Prerequisites
- Python 3.8+
- `requests` library

Install dependencies with:
```bash
pip install requests
```

### 2. Get a WeatherAPI Key
Sign up at https://www.weatherapi.com/ and get a free API key.

### 3. Set your API key
Open `weather_app.py` and replace:
```py
api_key = "API-KEY"  # Replace with your actual API key
```
with your real key, or modify the script to read the key from an environment variable:

```py
import os
api_key = os.getenv("WEATHERAPI_KEY")
```

To set the environment variable (Linux/macOS):
```bash
export WEATHERAPI_KEY="your_real_key_here"
```
Windows (PowerShell):
```powershell
setx WEATHERAPI_KEY "your_real_key_here"
```

### 4. Run the app
```bash
python /path/to/weather_app.py
```
Then enter the city name when prompted, for example:
```
Enter city name: Mumbai
```

---

## 🧩 Suggested Improvements
If you want to make it more production-ready, consider:
- Read API key from an environment variable or config file (avoid hardcoding).
- Add CLI arguments with `argparse` (e.g., `--city`, `--units`).
- Add error handling for network/timeouts and invalid city names.
- Allow output formats (plain text, JSON) for easier integration.
- Add unit tests and CI (GitHub Actions).

---

## ♻️ Example output
```
City: Mumbai
Region: Maharashtra
Country: India
Time Zone: Asia/Kolkata
Local Time: 2025-10-05 14:20
Temperature (C): 30.0
Condition: Partly cloudy
Wind Speed (kph): 15.8
Humidity: 70
Feels Like (C): 33.0
```

---

## 📁 Files
- `weather_app.py` — main script (provided)

---

## 📜 License
This repository is a good fit for the **MIT License**. Add a `LICENSE` file with the MIT text if you want to make it open-source and permissive.

---

## 🤝 Contributing
Feel free to open issues or submit PRs. For small scripts like this, keep changes focused, add tests for new features, and update the README with usage examples.

---

## ✅ Repo name suggestions
- `cli-weather-app`
- `simple-weather-cli`
- `weather-api-demo`
- `py-weather-tool`

---

If you want, I can also:
- Turn the script into a more robust CLI with `argparse`.
- Create a GitHub-ready repo structure (`README`, `LICENSE`, `.gitignore`, `requirements.txt`).
- Add a ready-to-use `README.md` file tailored to your preferred repo name and license.

