import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

final_note_to_save=""
class Notes(Widget):
	notes=ObjectProperty(None)

	def Savenotes(self):
		global final_note_to_save
		print(type(self.notes))
		print(self.notes.text)
		
		s="\n"+self.notes.text+"\n"
		final_note_to_save=s
		
	def cleartf(self):
		global final_note_to_save
		self.notes.text=""
		final_note_to_save=""

class NotepadApp(App):
	def build(self):
		return Notes()

if __name__ == "__main__":
	NotepadApp().run()

	print("Final line to print and saving notes to file")
	f=open("notes","a")
	f.write(final_note_to_save)
	f.close