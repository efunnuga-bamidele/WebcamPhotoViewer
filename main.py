import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer
from kivy.core.clipboard import Clipboard
import time

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_control_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_control_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "image_screen"

        # self.manager.current_screen.ids.img.widget.size_hint = (0.7, 1.0)
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_msg = "Create a link first!"
    def create_link(self):
        """Accesses the photo filepath, uploads the image to the web via API and insert the         file link to the Label widget """
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath=file_path)

        try:
            self.url = fileshare.share()
            self.ids.link.text = self.url
        except:
            self.ids.link.text = "Unable to upload the file!"

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_msg

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_msg


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
