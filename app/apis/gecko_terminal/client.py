import logging
from django.conf import settings
import requests

logger = logging.getLogger(__name__)

class Client:
    '''
    This handles all API calls to Gecko Terminal endpoints
    '''

    def __init__(self, *args, **kwargs):
        self.base_url = settings.GECKO_URL
        self.network = kwargs.get("network")
        self.dex = kwargs.get("dex")
        self.address = kwargs.get("address")

    def networks(self) -> str:
        return f'{self.base_url}/networks'
    
    def dexes(self) -> str:
        return f'{self.base_url}/networks/{self.network}/dexes'
    
    def pools(self) -> str:
        return f'{self.base_url}/networks/{self.network}/pools'
    
    def trending_pools(self) -> str:
        if self.network:
            return f'{self.base_url}/networks/{self.network}/trending_pools'
        return f'{self.base_url}/networks/trending_pools'
    

    def get_trending_pools(self) -> list:
        url = self.trending_pools()
        response = requests.get(url)
        match response.status_code:
            case 200:
                rsp = response.json()
                data = rsp["data"]
                for p in data:
                    p["external_id"] = p.pop("id")
                return data
        return []




    