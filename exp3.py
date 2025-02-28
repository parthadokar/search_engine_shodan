import shodan
import requests
import os

SHODAN_API_KEY = os.environ.get('SHODAN_API_KEY', 'API KEY')  # Default for testingprint(SHODAN_API_KEY)
api = shodan.Shodan(SHODAN_API_KEY)

domain = 'www.python.org'

dnsResolve = f"https://api.shodan.io/dns/resolve?hostname={domain}&key={SHODAN_API_KEY}"

try:
    resolved = requests.get(dnsResolve)
    hostIP = resolved.json()[domain]

    host = api.host(hostIP)
    print("IP:%s" %host['ip_str'])
    print("Organization: %s" % host.get('org','n/a'))
    print("Operating System: %s" % host.get('os','n/a'))
    
    for item in host['data']:
        print("Port: %s" % item['port'])
        print("Banner: %s" % item['data'])

except shodan.APIError as exception:
    print("Error: %s" % Exception) 