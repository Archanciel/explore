from kivy.app import App
#kivy.require("1.9.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect

class MyWidget(BoxLayout):
    '''
    This app demonstrvates two thibgs:
        1/ the use validate = False on the Kivy UrlRequest to alvoid Cryptocompare
        data query to fail. Note that in PriceRequester, since urllib.Requedst is used,
        the same effect is obtained with the use of ssl context.
        2/ the use of ScrollEffect coupled to a $croll$crollview embedding an InputTextView
        to avoid over scrolling
    '''
    def __init__(self,**kwargs):
        super(MyWidget,self).__init__(**kwargs)
        self.scrollView = ScrollView()
        self.scrollView.size_hint = (1, 1)
        self.scrollView.effect_cls = ScrollEffect #avoid overscrolling

        self.output = TextInput()
        self.output.size_hint = (1, 2)
        self.output.height = max(self.output.minimum_height, self.scrollView.height)

        self.scrollView.add_widget(self.output)
        self.add_widget(self.scrollView)
        coin = 'BTC' 
        fiat = 'USD'
        timeStampUTCStr = '1504389050'
        exchange = 'BitTrex'
        limit = 93
        search_url = "https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate=1&toTs={}&e={}".format(coin, fiat, limit, timeStampUTCStr, exchange)
        self.printToOutput(str(search_url))
        self.request = UrlRequest(search_url, on_success=self.res, on_error=self.resError, verify=False)


    def res(self, req, result):
        for d in result['Data']:
            line = 'time: {0} high: {1:.2f} low: {2:.2f}'.format(d['time'], d['high'], d['low'])
            self.printToOutput(line)
            

    def resError(self,*args):
        self.printToOutput("Result: after error")
        self.printToOutput(str(self.request.error))


    def printToOutput(self, str):
        if str != None:
            self.output.text = self.output.text + '\n' + str
        
        
class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
