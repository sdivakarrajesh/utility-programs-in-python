import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title = "PDF Cruncher")
        self.set_border_width(30)
        layout = Gtk.Box(spacing = 0)
        self.add(layout)

        button = Gtk.Button("Choose File")
        button.connect("clicked",self.on_file_clicked)
        layout.add(button)
    def on_file_clicked(self,widget):
        dialog = Gtk.FileChooserDialog("Select a PDF File",self,Gtk.FileChooserAction.OPEN,('Cancel',Gtk.ResponseType.CANCEL,"OK",Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("You selected a File")
            print("File selected" + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("User didn't select a file")
        dialog.destroy()


window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
