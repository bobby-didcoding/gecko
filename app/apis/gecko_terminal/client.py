import logging
from django.conf import settings
import requests

logger = logging.getLogger(__name__)


class Client:
    """
    This handles all API calls to Gecko Terminal endpoints
    """

    def __init__(self, *args, **kwargs):
        self.base_url = settings.GECKO_URL
        self.network = kwargs.get("network")
        self.dex = kwargs.get("dex")
        self.address = kwargs.get("address")

    def networks(self) -> str:
        return f"{self.base_url}/networks"

    def dexes(self) -> str:
        return f"{self.base_url}/networks/{self.network}/dexes"

    def pools(self) -> str:
        return f"{self.base_url}/networks/{self.network}/pools"

    def token_info(self) -> str:
        return f"{self.base_url}/networks/{self.network}/tokens/{self.address}/info"

    def trending_pools(self) -> str:
        if self.network:
            return f"{self.base_url}/networks/{self.network}/trending_pools"
        return f"{self.base_url}/networks/trending_pools"

    def get_networks(self) -> list:
        next = self.networks()
        data = []
        while True:
            response = requests.get(next)
            match response.status_code:
                case 200:
                    rsp = response.json()
                    try:
                        next_url = rsp["links"]["next"]
                    except KeyError:
                        next_url = None
                    for p in rsp["data"]:
                        p["external_id"] = p.pop("id")
                        data.append(p)
                    if next_url:
                        next = next_url
                    else:
                        break
        return data

    def get_dexes(self) -> list:
        next = self.dexes()
        data = []
        while True:
            response = requests.get(next)
            match response.status_code:
                case 200:
                    rsp = response.json()
                    try:
                        next_url = rsp["links"]["next"]
                    except KeyError:
                        next_url = None
                    for p in rsp["data"]:
                        p["external_id"] = p.pop("id")
                        data.append(p)
                    if next_url:
                        next = next_url
                    else:
                        break
        return data

    def get_trending_pools(self) -> list:
        next = self.trending_pools()
        data = []
        while True:
            response = requests.get(next)
            match response.status_code:
                case 200:
                    rsp = response.json()
                    try:
                        next_url = rsp["links"]["next"]
                    except KeyError:
                        next_url = None
                    for p in rsp["data"]:
                        p["external_id"] = p.pop("id")
                        data.append(p)
                    if next_url:
                        next = next_url
                    else:
                        break
        return data

    def get_token_info(self) -> list:
        url = self.token_info()
        response = requests.get(url)
        match response.status_code:
            case 200:
                rsp = response.json()
                data = rsp["data"]
                data["external_id"] = data.pop("id")
                return data
        return []
