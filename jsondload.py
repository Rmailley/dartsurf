import requests, json

response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 39.970806,
    'lng': -73.967408,
    'params': 'windSpeed,windDirection,swellDirection,swellHeight,swellPeriod',
  },
  headers={
    'Authorization': '91a11066-eefc-11eb-862d-0242ac130002-91a110e8-eefc-11eb-862d-0242ac130002'
  }
)

# Do something with response data.
json_data = response.json()

with open('swelldata.json', 'w') as f:
    f.write(json.dumps(json_data, indent=3))
