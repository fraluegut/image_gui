
import os
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ImageViewer(App):
    def __init__(self, folder, **kwargs):
        super().__init__(**kwargs)
        self.folder = folder
        self.images = os.listdir(self.folder)
        self.current_image = 0
        self.title = ""
        self.description = ""

    def build(self):
        self.image = Image(source=self.images[self.current_image])

        self.title_label = Label(text=self.title, color=(0, 0,1, 1))
        self.description_label = Label(text=self.description, color=(0, 0, 0, 1))
        self.previous_button = Button(text="Previous", size_hint=(0.25, None), on_press=self.previous_image)
        self.next_button = Button(text="Next", size_hint=(0.25, None), on_press=self.next_image)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.description_label)
        self.layout.add_widget(self.previous_button)
        self.layout.add_widget(self.next_button)
        return self.layout

    def previous_image(self, instance):
        if self.current_image > 0:
            self.current_image -= 1
            self.image.source = self.images[self.current_image]
            self.title_label.text = self.title
            self.description_label.text = self.description

    def next_image(self, instance):
        if self.current_image < len(self.images) - 1:
            self.current_image += 1
            self.image.source = self.images[self.current_image]
            self.title_label.text = self.title
            self.description_label.text = self.description

if __name__ == "__main__":
    folder = "E:\PYTHON\image_gui"
    ImageViewer(folder).run()
