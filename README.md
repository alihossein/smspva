# simple class for working with smspva.com site #
This class helps developers to easily work with [smspva](http://smspva.com/) site in python applications.

## Methods ##
 - get_number (Request for receiving a phone number for a certain service )
 - get_sms ( Receiving a SMS for a certain service )
 - get_balance (User's balance request)
 - get_userinfo( User's balance request and your rating)
 - get_count_new (Request for the amount of free activations for a certain service)
 - denial ( Cancel the order to number you got )
 
 
## Examples ##
``` python
pva=SmsPva();
balance=pva.get_balance()  #result  {'response': '1', 'balance': '0.360'}
userinfo=pva.get_userinfo() # result {'karma': '99.825', 'response': '1', 'balance': '0.360'}

```

## License

This class is released under the [MIT License](http://alihossein.mit-license.org/).
