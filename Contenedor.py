# _____________

# Contenedor.py

# _____________

class Infraestructura:


    def __init__(self, client, contenedores):
        self.client = client
        self.contenedores = contenedores


    def _print(self):
        print " "
        print "{:15} {:20} {:10} {:25}".format("Id","Nombre","Estado","Imagen")
        for c in self.contenedores:
            print "{:15}{:20}{:10}{:25}".format(\
                str(c['Id'])[:10], c['name'], c['state'], c['image'])
        print " "


    def _add_info(self):
        for mc in self.contenedores:
            existe = False
            nombre = mc['name']
            for c in self.client.containers.list(all=True):
                if nombre == c.attrs['Name'].split('/')[1]:
                    existe = True
                    mc.update({'state': c.attrs['State']['Status']})
                    mc.update({'Id': c.attrs['Id']})
                    break
            if existe == False:
                mc.update({'state': None})
                mc.update({'Id': 0})


    def _remove(self):
        for mc in self.contenedores:
            id = mc['Id']
            for c in self.client.containers.list(all=True):
                if id == c.attrs['Id']:
                    if not c.attrs['State']['Status'] == 'running':
                        self.client.containers.model.remove(c)
                        print "Contenedor", id, "removido"
                    else:
                        print "El contenedor ", mc['name'], " esta en ejecucion. "
                    break


    def _create(self):
        for x in self.contenedores:
            if x['state'] == None:
                self.client.containers.create( image=x['image'], \
                                               name=x['name'],   \
                                               ports=x['ports'], \
                                               links=x['links'], \
                                               environment=x['environment'])
            else:
                print " El contenedor ", x['name'], " ya existe. "


    def _stop(self):
        for mc in self.contenedores:
            id = mc['Id']
            for c in self.client.containers.list(all=True):
                if id == c.attrs['Id']:
                    if c.attrs['State']['Status'] == 'running':
                        self.client.containers.model.stop(c)
                    else:
                        print " El contenedor ", mc['name'], " no esta en ejecucion. "
                    break


    def _start(self):
        for mc in self.contenedores:
            id = mc['Id']
            for c in self.client.containers.list(all=True):
                if id == c.attrs['Id']:
                    if not c.attrs['State']['Status'] == 'running':
                        self.client.containers.model.start(c)
                    else:
                        print "El contenedor ", mc['name'], " esta en ejecucion. "
                    break


    def _exec(self, contenedor, command, pathdir):
        for mc in self.contenedores:
            nombre = mc['name']
            id = mc['Id']
            if nombre == contenedor:
                for c in self.client.containers.list(all=True):
                    if id == c.attrs['Id']:
                        if c.attrs['State']['Status'] == 'running':
                            print self.client.containers.model.\
                                exec_run(c, cmd=command, tty=True, workdir=pathdir)
                        else:
                            print " El contenedor ", contenedor, " no esta en ejecucion. "
                        break


    def _put_file(self, contenedor, dir, datos):
        for mc in self.contenedores:
            nombre = mc['name']
            id = mc['Id']
            if nombre == contenedor:
                for c in self.client.containers.list(all=True):
                    if id == c.attrs['Id']:
                        if c.attrs['State']['Status'] == 'running':
                            self.client.containers.model.\
                                put_archive(c, path=dir, data=datos)
                        else:
                            print " El contenedor ", contenedor, " no esta en ejecucion. "
                        break


class Imagenes:
    def __init__(self, client):
        self.client = client


    def _exists(self, imagen):
        for c in self.client.images.list():
            if c.attrs['RepoTags']:
                if imagen == c.attrs['RepoTags'][0]:
                    return c.attrs['Size']/1000000


    def _list(self, contenedores):
        print ""
        for mc in contenedores:
            tam = self._exists(mc['image'])
            if tam:
                print "Existe imagen {} con {} MB".format(mc['image'], tam)
            else:
                print "No existe imagen {} ".format(mc['image'])


    def _create(self, f, tagname):
        response = [line for line in \
                    self.client.images.build(fileobj=f, \
                    rm=True, tag=tagname)]
        return response

