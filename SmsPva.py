import requests

class SmsPva:
    def __init__(self):
        self.url = http://smspva.com/priemnik.php
        self.api_key = 'your api_key'
        self.method_type = 'get'
        self.query_string = {}
       

    def get_number(self, id=1, country='ru', service='opt29'):
        """
        Request for receiving a phone number for a certain service
        :return:
        """
        self.query_string = {'metod': 'get_number', 'country': country, 'service': service, 'id': id,
                             'apikey': self.api_key}
        result = self.__make_request()
        return result

    def get_sms(self, id, country='ru', service='opt29'):
        """
        Receiving a SMS for a certain service
        :return:
        """
        self.query_string = {'metod': 'get_sms', 'country': country, 'service': service, 'id': id,
                             'apikey': self.api_key}
        result = self.__make_request()
        return result

    def get_balance(self, service='opt29'):
        """
        User's balance request
        :param service:
        :return:
        """
        self.query_string = {'metod': 'get_balance', 'service': service, 'apikey': self.api_key}
        result = self.__make_request()
        return result

    def get_userinfo(self,service='opt29'):
        """
        User's balance request and karma (Your rating)
        :return:
        """
        self.query_string = {'metod': 'get_userinfo', 'service': service, 'apikey': self.api_key}
        result = self.__make_request()
        return result

    def get_count_new(self,service='opt29',country='ru'):
        """
        Request for the amount of free activations for a certain service
        :param country:
        :param service:
        :return:
        """
        self.query_string = {'metod': 'get_count_new', 'service': service , 'country':country, 'apikey': self.api_key}
        result = self.__make_request()
        return result

    def denial(self, id, country='ru', service='opt29'):
        """
        Cancel the order to number you got
        :return:
        """
        self.query_string = {'metod': 'denial', 'country': country, 'service': service, 'id': id,
                             'apikey': self.api_key}
        result = self.__make_request()
        return result

    def __make_request(self):
        """
        make request post or get , ...
        :return:
        """

        try:
            if self.method_type == 'get':
                response = requests.get(self.url, self.query_string)
            elif self.method_type == 'post':
                pass

            if response.status_code == 200:
                return response.json()
            else:
                return response

        except Exception as e:
            return e
