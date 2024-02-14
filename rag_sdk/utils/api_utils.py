import httpx
import requests
from fake_useragent import UserAgent


class RequestSender:

    def __init__(self, headers: dict = None):
        self.ua = UserAgent()
        self._set_default_headers(headers)
        self.default_retries = 3
        self.default_timeout = 90
        self.default_wait_seconds = 0.5

    def _set_default_headers(self, headers: dict = None):
        if headers:
            self.headers = headers
        else:
            self.headers = {
                "User-Agent": self.ua.google,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

    def send_request(
        self, method: str, url: str, params: dict = None, data: dict = None, **kwargs
    ):
        response = request.request(
            method, url, headers=self.headers, params=params, data=data, **kwargs
        )
        return response.json()

    def send_streaming_request(
        self, method: str, url: str, params: dict = None, data: dict = None, **kwargs
    ):
        try_num = 0
        while try_num <= self.default_retries:
            try:

                with httpx.stream(
                    method,
                    url,
                    headers=self.headers,
                    params=params,
                    json=data,
                    timeout=self.default_timeout,
                ) as r:
                    for text in r.iter_text():
                        yield text
                break

            except Exception as ex:
                print(f"Invalid chunk encoding {str(ex)}")
                sleep(self.default_wait_seconds)
                try_num += 1
