import shodan
import os

SHODAN_API_KEY = os.environ.get('SHODAN_API_KEY', 'API KEY')  # Default for testingprint(SHODAN_API_KEY)
shodan = shodan.Shodan(SHODAN_API_KEY)

try:
    resultados = shodan.search('nginx')
    print("Results:",resultados.items())
except Exception as exception:
    print(str(exception))