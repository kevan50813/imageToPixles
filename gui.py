import imageManipulator as im
import PySimpleGUI as sg
import os.path

def makeGUI():
    file_list_column = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

    image_viewer_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-",filename='')],
        [sg.Image(key="-IMAGEPIXLEATED-",filename='')],
        [sg.Image(key="-IMAGECARTOON-",filename='')],
        [sg.Image(key="-IMAGESKETECH-",filename='')],
    ]

    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

    window = sg.Window("Image transformation", layout)
    while True:
        event,values = window.read()

        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".png", ".gif", ".jpeg"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the list box
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)
                images = im.trasnformImages(filename)
                window["-IMAGEPIXLEATED-"].update(filename="pixel.png")
                window["-IMAGECARTOON-"].update(filename="sketch.png")
                window["-IMAGESKETECH-"].update(filename="cartoon.png")
            except:
                pass

        if event == sg.WIN_CLOSED:
            break

    window.close()
    im.cleanup()