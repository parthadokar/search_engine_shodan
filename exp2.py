from shodan import Shodan

api = Shodan('API KEY')

# Check for IP

ipinfo = api.host('8.8.8.8')
print(ipinfo)

# Search hacked websites

for banner in api.search_cursor('http.title:"hacked by"'):
    print(banner)

# Get total number of industrial control systems on the internet 

ics_services = api.count('tag:ics')
print('Industrial Control Systems: {}'.format(ics_services['total']))
