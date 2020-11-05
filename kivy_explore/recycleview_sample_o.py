
# Program to explain how to use recycleview in kivy 
  
# import the kivy module 
from kivy.app import App 
  
# The ScrollView widget provides a scrollable view  
from kivy.uix.recycleview import RecycleView 
  
  
# Define the Recycleview class which is created in .kv file 
class ExampleViewer(RecycleView): 
    def __init__(self, **kwargs): 
        super(ExampleViewer, self).__init__(**kwargs) 
        self.data = [{'text': str(x)} for x in range(20)] 
  
# Create the App class with name of your app. 
class RVSampleOApp(App): 
    def build(self): 
        return ExampleViewer() 
  
# run the App 
RVSampleOApp().run()