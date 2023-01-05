import syn10
from syn10 import utils
from syn10.api_requestor import APIRequestor


class Informable:
    @staticmethod
    def get_endpoint():
        raise NotImplementedError

    def get_id(self):
        raise NotImplementedError

    @property
    def info(self):
        requestor = APIRequestor(token=utils.find_token())
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}"
        resp = requestor._request("GET", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        return resp.json()