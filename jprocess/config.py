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
    ),
   Server(
        name='Web-server',
        host='104.224.134.223',
        port=9001,
        user='user',
        password='123'
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
    },
    {
        'name': 'Web-server',
        'apps': ['Web-server.django','Web-server.ssserver','Web-server.celery']
    }
]
