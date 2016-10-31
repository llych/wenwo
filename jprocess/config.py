from Server import Server

SERVERS = [
    Server(
        name='jumpserver',
        host='192.168.1.69',
        port=9001,
        user='user',
        password='123'
    ),
    Server(
        name='java-platform',
        host='192.168.1.58',
        port=9002,
        user='deploy',
        password='ODk4Nwo=15532OTk3Mgo='
    )
]

GROUPS = [
    {
        'name': 'jumpserver',
        'apps': ['jumpserver.jumpserver',]
    },
    {
        'name': 'java-platform',
        'apps': ['java-platform.wenwo-platform']
    }
]
