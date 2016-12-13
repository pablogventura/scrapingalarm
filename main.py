import mechanize
import time
import BeautifulSoup
import os
    
def play(time,freq):
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( time, freq))


while True:

    br = mechanize.Browser()

    br.set_handle_robots(False)

    br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98;)')]
    s="http://articulo.mercadolibre.com.ar/MLA-630381204-combo-raspberry-pi-3-gabinete-_JM"
    p="http://articulo.mercadolibre.com.ar/MLA-619762860-fuente-switching-metalica-24v-25a-600w-led-super-oferta-_JM"
    resp= br.open(p)

    pagina = BeautifulSoup.BeautifulSoup(resp)

    if not "pausada" in str(pagina.getString):
        while True:
            time.sleep(1)
            play(0.5,440)
    print "esperando..."
    time.sleep(60)

