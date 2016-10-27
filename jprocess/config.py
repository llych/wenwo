from Server import Server

SERVERS = [
    Server(
        name='jumpserver',
        host='192.168.1.69',
        port=9001,
        user='user',
        password='123'
    ),
    #Server(
    #    name='celery2',
    #    host='remote.supervisor.com',
    #    port=12345,
    #    user='admin',
    #    password='admin'
    #)
]

GROUPS = [
    {
        'name': 'jumpserver',
        'apps': ['jumpserver.jumpserver',]
    },
    #{
    #    'name': 'flower',
    #    'apps': ['celery1.flower']
    #}
]
