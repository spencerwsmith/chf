__author__ = 'Spencer'
########This will go in Login

from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO

username = 'COLHERITAGE\Spencer'
pw = 'spencer24'

s = Server('colheritagefoundation.info', port=389, get_info=GET_ALL_INFO)

c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='cn=%s' % username, password=pw)

print(c)
print(c.user)