from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown

class CustomDropDown(DropDown):
    pass
    
class DropDownTrialGUI(BoxLayout):
    #dropD = CustomDropDown() #menu not displaying if CustomDropDown not instanciated in __inie__ !

    def __init__(self, **kwargs):
        super(DropDownTrialGUI, self).__init__(**kwargs)
        self.dropD = CustomDropDown() #this is the right place for instanciating the CustomDropDown !

        
    def openMenu(self, widget):
        self.dropD.open(widget)
                             
                                           
class DropDownTrialGUIApp(App):
    def build(self):
        return DropDownTrialGUI()
 

if __name__== '__main__':
    dbApp = DropDownTrialGUIApp()
 
    dbApp.run()
