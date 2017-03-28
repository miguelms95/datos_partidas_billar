from BeautifulSoup import BeautifulSoup
import requests

listaDePartidas = []

def extraerdatos(url):
    page = requests.get(url);
    if (page.status_code == 200):
        html = BeautifulSoup(page.content.decode('utf-8', 'ignore'))
        todasLasFilas = html.findAll('tr');
        for fila in todasLasFilas:
            columnasDeCadaFila = fila.findAll('td');
            #print columnasDeCadaFila
            if(len(columnasDeCadaFila)>=12):
                imagenPaisIzq = columnasDeCadaFila[7].find('img')
                imagenPaisDer = columnasDeCadaFila[11].find('img')
                if(imagenPaisIzq != None and imagenPaisIzq.get('alt') == 'ESP'):    #Local que aparece a la izquierda
                    listaDePartidas.append(fila)
                    print fila
                if (imagenPaisDer != None and imagenPaisDer.get('alt') == 'ESP'):   #Visitante que aparece a la derecha
                    listaDePartidas.append(fila)
                    print fila

extraerdatos('http://billiardapps.com/drawresults.asp?db=epc&client=&eventnr=2017100&header=no&eventheader=yes&showtabs=yes&tab=Tournament&footer=yes&tournament=W10')