import requests
import time


class MMA:
    def __init__(self):
        token = '5319097390:AAFUUPgyI7ZlI770vsEA-cdGsC9RnFDCC-U'
        self.url_base = f'https://api.telegram.org/bot{token}/'
