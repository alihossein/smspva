import requests

class SmsPva:
    def __init__(self):
        self._url = http://smspva.com/priemnik.php
        self._api_key = 'your api_key'
        self._method_type = 'get'
        self._query_string = {}
       

    def get_number(self, id=1, country='ru', service='opt29'):
        """
        Request for receiving a phone number for a certain service
        :return:
        """
        self._query_string = {'metod': 'get_number', 'country': country, 'service': service, 'id': id,
                             'apikey': self._api_key}
        result = self.__make_request()
        return result

    def get_sms(self, id, country='ru', service='opt29'):
        """
        Receiving a SMS for a certain service
        :return:
        """
        self._query_string = {'metod': 'get_sms', 'country': country, 'service': service, 'id': id,
                             'apikey': self._api_key}
        result = self.__make_request()
        return result

    def get_balance(self, service='opt29'):
        """
        User's balance request
        :param service:
        :return:
        """
        self._query_string = {'metod': 'get_balance', 'service': service, 'apikey': self._api_key}
        result = self.__make_request()
        return result

    def get_userinfo(self,service='opt29'):
        """
        User's balance request and karma (Your rating)
        :return:
        """
        self._query_string = {'metod': 'get_userinfo', 'service': service, 'apikey': self._api_key}
        result = self.__make_request()
        return result

    def get_count_new(self,service='opt29',country='ru'):
        """
        Request for the amount of free activations for a certain service
        :param country:
        :param service:
        :return:
        """
        self.query_string = {'metod': 'get_count_new', 'service': service , 'country':country, 'apikey': self._api_key}
        result = self.__make_request()
        return result

    def denial(self, id, country='ru', service='opt29'):
        """
        Cancel the order to number you got
        :return:
        """
        self._query_string = {'metod': 'denial', 'country': country, 'service': service, 'id': id,
                             'apikey': self._api_key}
        result = self.__make_request()
        return result

    def __make_request(self):
        """
        make request post or get , ...
        :return:
        """

        try:
            if self._method_type == 'get':
                response = requests.get(self._url, self._query_string)
            elif self._method_type == 'post':
                pass

            if response.status_code == 200:
                return response.json()
            else:
                return response

        except Exception as e:
            return e
