```markdown
# 🌤️ Weather App

A simple weather application built with **Django** that fetches real-time weather data from the **OpenWeatherMap API**. Users can search for any city and view current conditions including temperature, humidity, atmospheric pressure, "feels like" temperature, and wind speed.

This is my first Django project, built to practice working with external APIs, Django views/templates, and basic frontend styling.

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Displays current temperature (°C)
- ☁️ Shows weather description and icon (e.g. "Clear Sky")
- 💧 Humidity percentage
- 🌬️ Wind speed
- 🌡️ "Feels like" temperature
- 📊 Atmospheric pressure (hPa)
- ⚠️ Graceful error handling for invalid or unknown city names

## 🛠️ Tech Stack

- **Backend:** Python, Django 
- **API:** [OpenWeatherMap](https://openweathermap.org/api)
- **HTTP Requests:** `requests` library
- **Frontend:** HTML, CSS (Django templates)

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8+
- pip
- A free API key from [OpenWeatherMap](https://openweathermap.org/api)

## 🚀 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
```

1. **Create and activate a virtual environment**
  ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
  ```
2. **Install dependencies**
  ```bash
   pip install django requests
  ```
3. **Add your OpenWeatherMap API key**
  Open `weather_app/views.py` and replace the placeholder with your own API key:
  > 💡 **Tip:** For better security, avoid hardcoding your API key. Consider storing it in an environment variable instead and loading it with `os.environ.get('OPENWEATHER_API_KEY')`.
4. **Run database migrations**
  ```bash
   python manage.py migrate
  ```
5. **Start the development server**
  ```bash
   python manage.py runserver
  ```
6. **Open the app**
  Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
weather_project/
├── weather_app/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── weather_project/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── README.md
```

## 🖼️ Screenshot

> `![Weather App Screenshot](images/weather-app-image.png)`

## 🔮 Future Improvements

- [ ] Geolocation-based weather (auto-detect user's city)
- [ ] Unit toggle (Celsius / Fahrenheit)
- [ ] Deploy live demo (e.g. on Render or PythonAnywhere)

## 🙏 Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Built with [Django](https://www.djangoproject.com/)

```

```

