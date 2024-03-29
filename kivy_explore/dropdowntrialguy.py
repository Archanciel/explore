from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class CustomDropDown(DropDown):
    
    def firstItem(self):
        """
        Display second menu item
        """
        self.gridlayoutSecondItem.height = self.secondItemButton.height

    def secondItem(self):
        """
        Hide second menu item
        """
        self.gridlayoutSecondItem.height = 0

    def thirdItem(self):
        print('CustomDropDown.thirdItem() called')

class DropDownTrialGUY(BoxLayout):
    #dropD = CustomDropDown() #menu not displaying if CustomDropDown not instanciated in __inie__ !

    def __init__(self, **kwargs):
        super(DropDownTrialGUY, self).__init__(**kwargs)
        self.dropD = CustomDropDown() #this is the right place for instanciating the CustomDropDown !

        
    def openMenu(self, widget):
        self.dropD.open(widget)
        
class DropDownTrialGUYApp(App):
    def build(self):
        return DropDownTrialGUY()
        
    def on_start(self):
        content = Button(text='Close me!')
        popup = Popup(title='CryptoPricer WARNING', content=content, auto_dismiss=False,size_hint=(None, None), size=(600, 300) )

        # bind the on_press event of the button to the dismiss function
        content.bind(on_press=popup.dismiss)

        # open the popup
        popup.open()
 

if __name__== '__main__':
    dbApp = DropDownTrialGUYApp()
 
    dbApp.run()
