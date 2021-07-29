import dateutil
import json
from dateutil import parser
import pandas as pd
import matplotlib.pyplot as plt


with open('swelldata.json', 'r') as f:
    x = json.loads(f.read())

tf_data = x['hours']
df = pd.DataFrame(columns=['time', 'Swell direction', 'Swell Height'])
for i in range(len(tf_data)):
    timestamp = str(tf_data[i]['time'])

    dtobj = parser.parse(timestamp)
    dtobj = dtobj.astimezone(dateutil.tz.gettz('US/Eastern'))

    df.loc[len(df.index)] = [ str(dtobj), str(tf_data[i]['swellDirection']['noaa']), str(tf_data[i]['swellHeight']['noaa'])]
    #print(" at " + str(dtobj) + ": sw dir = " + str(tf_data[i]['swellDirection']['noaa'])+ ", sw height = "+ str(tf_data[i]['swellHeight']['noaa']))


df = df.set_index('time')
df = df.astype('float')
print(df.head())
plt.plot(df['Swell Height'])
plt.show()
