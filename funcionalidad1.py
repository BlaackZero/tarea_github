import datetime
import pytz
#pip install pytz

# Obtener la hora actual en Chile
chile_timezone = pytz.timezone('Chile/Continental')
chile_time = datetime.datetime.now(chile_timezone)
print("Hora en Chile:", chile_time.strftime("%Y-%m-%d %H:%M:%S"))

# Obtener la hora actual en Japón
japan_timezone = pytz.timezone('Asia/Tokyo')
japan_time = datetime.datetime.now(japan_timezone)
print("Hora en Japón:", japan_time.strftime("%Y-%m-%d %H:%M:%S"))


# Obtener la hora actual en Canada
canada_timezone = pytz.timezone('Canada/Pacific')
canada_time = datetime.datetime.now(canada_timezone)
print("Hora en Canada:", canada_time.strftime("%Y-%m-%d %H:%M:%S"))