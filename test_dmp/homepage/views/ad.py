__author__ = 'Spencer'
########This will go in Login
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO
'''#check the employee against Active Directory
# define the server and the connection
s = Server('IP_Address_here', port = 636, get_info = GET_ALL_INFO)
c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC, user=username, password=form.cleaned_data['password'], authentication=AUTH_SIMPLE)
print(s.info) # display info from the DSE. OID are decoded when recognized by the library
login(request, user)

You'll want to run this code in your is_valid() if statement for your login form'''

username = 'Spencer@colheritagefoundation.local'
pw = 'spencer24'

s = Server('colheritagefoundation.info', port=8889, get_info=GET_ALL_INFO)

c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user=username, password=pw, authentication=AUTH_SIMPLE)

print(c)
print(c.user)