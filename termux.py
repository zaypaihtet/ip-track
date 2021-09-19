import json
from urllib import request

print("\n IP-TRACKER by RED_Z\n")
url = "http://ip-api.com/json/"
ip = input("Input the IP Address : ")
request = request.urlopen(url + ip)
data_json = json.loads(request.read())

if data_json['status'] == "success":
	print(f"IP : {data_json['query']}")
	print(f"Country : {data_json['country']}")
	print(f"Region : {data_json['regionName']}")
	print(f"City : {data_json['city']}")
	print(f"Latitude : {data_json['lat']}")
	print(f"Longitude : {data_json['lon']}")
	print(f"ISP : {data_json['isp']}")
	print(f"Zip : {data_json['zip']}")
	print(f"AS : {data_json['as']}")
else:
	print("Failed to find the IP informations.")
