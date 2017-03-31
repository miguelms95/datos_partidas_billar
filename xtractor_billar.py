# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import requests

def extraerdatos(url):
    listaDePartidas = []
    page = requests.get(url);
    if (page.status_code == 200):   # la página web ha cargado correctamente
        html = BeautifulSoup(page.content.decode('utf-8', 'ignore'))
        todasLasFilas = html.findAll('tr');
        for fila in todasLasFilas:
            columnasDeCadaFila = fila.findAll('td');
            if(len(columnasDeCadaFila)>=12):
                imagenPaisIzq = columnasDeCadaFila[7].find('img')
                imagenPaisDer = columnasDeCadaFila[11].find('img')
                if(imagenPaisIzq != None and imagenPaisIzq.get('alt') == 'ESP'):    #Local que aparece a la izquierda
                    listaDePartidas.append(fila)
                    #print(fila)
                if (imagenPaisDer != None and imagenPaisDer.get('alt') == 'ESP'):   #Visitante que aparece a la derecha
                    listaDePartidas.append(fila)
                    #print(fila)
        return listaDePartidas
def extractDataFromTable(list):
    for item in list:
        cadena_fila = ''
        row_content = item.findAll('td')
        for column in row_content:
            if(column.find('a') != None):
                if(column.find('a').find('strong') != None):
                    cadena_fila += column.find('a').find('strong').string
                else:
                    cadena_fila += column.find('a').string
            elif(column.find('img') != None):
                try:
                    cadena_fila += column.find('img').get('alt')
                    print cadena_fila
                except TypeError:
                    cadena_fila += ' '
        #print '\n'

print 'Match | Date | Time | D | T | RT | \t \t == Match =='
extractDataFromTable(extraerdatos('http://billiardapps.com/drawresults.asp?db=epc&client=&eventnr=2017100&header=no&eventheader=yes&showtabs=yes&tab=Tournament&footer=yes&tournament=W10'))
#print(extraerdatos('http://billiardapps.com/drawresults.asp?db=epc&client=&eventnr=2017100&header=no&eventheader=yes&showtabs=yes&tab=Tournament&footer=yes&tournament=W10'))