import random

def exporter_webpage(pico_temperature, pico_bme280_temperature, pico_bme280_humidity, pico_bme280_air_pressure ):
    html_template = f"""# HELP pico_temp Temperature in C
# TYPE pico_temp gauge
pico_temp {pico_temperature}
# HELP pico_rand An Indication of a random number
# TYPE pico_rand gauge
pico_rand {str(random.randint(0,99))}
# HELP pico_bme280_temperature Room temperature from the BME280 sensor
# TYPE pico_bme280_temperature gauge
pico_bme280_temperature {pico_bme280_temperature}
# HELP pico_bme280_humidity Humidity from the BME280 sensor
# TYPE pico_bme280_humidity gauge
pico_bme280_humidity {pico_bme280_humidity}
# HELP pico_bme280_air_pressure Air pressure from the BME280 sensor
# TYPE pico_bme280_air_pressure gauge
pico_bme280_air_pressure {pico_bme280_air_pressure}"""
    return str(html_template)

# HTML template for the webpage
def webpage(random_value, state):
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pico Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Raspberry Pi Pico Web Server</h1>
            <h2>Led Control</h2>
            <form action="./lighton">
                <input type="submit" value="Light on" />
            </form>
            <br>
            <form action="./lightoff">
                <input type="submit" value="Light off" />
            </form>
            <p>LED state: {state}</p>
            <h2>Fetch New Value</h2>
            <form action="./value">
                <input type="submit" value="Fetch value" />
            </form>
            <p>Fetched value: {random_value}</p>
        </body>
        </html>
        """
    return str(html)