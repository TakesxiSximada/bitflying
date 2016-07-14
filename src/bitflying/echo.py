import furl
import requests


class EchoAPIClient(object):
    def price(self):
        endpoint = 'https://bitflyer.jp/'
        api_path = 'api/echo/price'
        url = furl.urljoin(endpoint, api_path)
        return requests.get(url)
