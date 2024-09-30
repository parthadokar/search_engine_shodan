import shodan

SHODAN_API_KEY = 'API KEY'
api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Look for shodan
    results = api.search('IIS')
    # Show results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['date'])
        print('')
except Exception as exception:
    print('Error : {}'.format(exception))