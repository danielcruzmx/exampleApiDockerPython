#________________________________________

# PROGRAMA PRINCIPAL
#________________________________________

import docker
import tarfile
import time
import os

from io import BytesIO
from Contenedor import Infraestructura, Imagenes

def _menu():
    opcs = ['A) Estado de los contenedores',
            'B) Crear contenedores',
            'C) Remover contenedores',
            'D) Parar contenedores',
            'E) Reiniciar contenedortes',
            'F) Crear archivos de App',
            'G) Crear base de datos',
            'H) Salir']
    print " "
    print "********************************************"
    print "* INFRAESTRUCTURA PARA PHP (Tome opcion)   *"
    print "********************************************"
    for o in opcs:
        print o
    print " "
    opc = raw_input(" Opcion -> ")
    return opc

def _crea_tarfile(nombrearchivo, contenido):
    pw_tarstream = BytesIO()
    pw_tar = tarfile.TarFile(fileobj=pw_tarstream, mode='w')
    file_data = contenido.encode('utf8')
    tarinfo = tarfile.TarInfo(name=nombrearchivo)
    tarinfo.size = len(file_data)
    tarinfo.mtime = time.time()
    pw_tar.addfile(tarinfo, BytesIO(file_data))
    pw_tar.close()
    pw_tarstream.seek(0)
    return pw_tarstream

def _actualiza_imagen_php(client):

    dockerfile = '''
        # App PHP
        FROM php:7.2-apache
        RUN apt-get update
        RUN docker-php-ext-install mysqli
    '''
    imgs = Imagenes(client)
    f = BytesIO(dockerfile.encode('utf-8'))
    print imgs._create(f, 'php_mysql:7.2-apache')

def __main__():

    client = docker.from_env(version="auto")

    _actualiza_imagen_php(client)

    INFRAESTRUCTURA = \
        [{'image': 'mysql:5.7',
          'name': 'cntr_mysql',
          'ports': {'3306/tcp': 3306},
          'links': (),
          'environment': ['MYSQL_ROOT_PASSWORD=passw']
          },
         {'image': 'php_mysql:7.2-apache',
          'name': 'cntr_php',
          'ports': {'80/tcp': 80},
          'links': {'cntr_mysql': 'db'},
           'environment': []
          },
         {'image': 'phpmyadmin/phpmyadmin',
          'name': 'cntr_phpmyadmin',
          'ports': {'80/tcp': 8080},
          'links': {'cntr_mysql': 'db'},
          'environment':[]
          }
         ]

    infra = Infraestructura(client, INFRAESTRUCTURA)
    infra._add_info()

    while 1:
        opc = _menu()
        if opc.upper() == 'A':
            a = 0
        elif opc.upper() == 'B':
            infra._create()
        elif opc.upper() == 'C':
            infra._remove()
        elif opc.upper() == 'D':
            infra._stop()
        elif opc.upper() == 'E':
            infra._start()
        elif opc.upper() == 'F':
            for dirname, dirnames, filenames in os.walk('miappphp/'):
                for a in filenames:
                    file = open('miappphp/{}'.format(a), 'r')
                    f = file.read()
                    infra._put_file('cntr_php', '/var/www/html', _crea_tarfile(a,f))
        elif opc.upper() == 'G':
            for dirname, dirnames, filenames in os.walk('basedatos/'):
                for a in filenames:
                    file = open('basedatos/{}'.format(a), 'r')
                    f = file.read()
                    infra._put_file('cntr_mysql', '/home', _crea_tarfile(a, f))
            infra._exec('cntr_mysql', ['chmod','+x','./creabd.sh'], '/home')
            infra._exec('cntr_mysql',['./creabd.sh'],'/home')
        elif opc.upper() == 'H':
            break

        infra._add_info()
        infra._print()

__main__()

#________________________________________
