import cookielib
import urllib
import urllib2
from bs4 import BeautifulSoup
import datetime

class Malica(object):

    def __init__(self, uporabniskoIme, geslo):

        self.uporabniskoIme = uporabniskoIme
        self.geslo = geslo
        
        #Poskusimo se prijaviti v portal
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPRedirectHandler(),urllib2.HTTPHandler(debuglevel=0),urllib2.HTTPSHandler(debuglevel=0),urllib2.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; ' 'Windows NT 5.2; .NET CLR 1.1.4322)'))]
        login_data = urllib.urlencode({'UserName' : uporabniskoIme,'Password' : geslo,'RememberMe' : 'false',})
        response = self.opener.open("https://malica.scng.si/Account/LogOn?ReturnUrl=%2f", login_data)
        html = BeautifulSoup(response.read(), "html.parser")
        
        error = html.find("div", {"class":"validation-summary-errors"})
        if error:
            raise Exception("Prijava neuspesna", error.text)
        else:
            uporabnik = html.find("label", {"class":"accent"})
            self.imePriimek = uporabnik.text.strip()

    def pridobiPodatkeTaTeden(self):
        #Dobimo danasnji datum in poiscemo prvi ponedeljek po nazaj
        today = datetime.date.today()
        datum = (today - datetime.timedelta(days=today.weekday())).strftime("%d.%m.%Y")
        return self.pridobiPodatke(datum)

    def pridobiPodatke(self, datum):
        dat = datetime.datetime.strptime(datum, "%d.%m.%Y")
        pretvorjenDatum = dat.strftime("%m/%d/%Y")
        response = self.opener.open("https://malica.scng.si/Home/Test?nextDateStart=" + urllib.quote(pretvorjenDatum))
        html = BeautifulSoup(response.read(), "html.parser")
        teden = []
        tabela = html.findAll('td')
        for stolpec in tabela:
            teden.append(stolpec.text.strip())    
        teden = teden[2:]
        return teden

    def odjava(self, datum):
        hrana = urllib.urlencode({'dnevi' : 'td_231_2_' + datum, 'hid2' : '', 'act' : 'ODJ'})
        response = self.opener.open("https://malica.scng.si/Home/OdjaviSpremembeMeni", hrana)

    def prijava(self, datum):
        hrana = urllib.urlencode({'dnevi' : 'td_231_2_' + datum, 'hid2' : '', 'act' : 'PRJ'})
        response = self.opener.open("https://malica.scng.si/Home/PrijaviSpremembeMeni", hrana)

    def zamenjava(self, datum, tip="SUH"):
        #Tip je lahko le SUH in OSN
        hrana = urllib.urlencode({'dnevi' : 'td_231_2_' + datum, 'hid2' : tip, 'act' : 'ZAM'})
        response = self.opener.open("https://malica.scng.si/Home/ZamenjajSpremembeMeni", hrana)
