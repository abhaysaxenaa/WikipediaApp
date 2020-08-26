import wikipediaapi
import PySimpleGUI as sg
wiki_wiki = wikipediaapi.Wikipedia('en')

sg.theme('DarkPurple') #Color
# All the stuff inside your window.
layout = [  [sg.Text('Enter Search Command:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Wikipedia Search Engine', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    page_py = wiki_wiki.page(values[0])
    print(values[0])
    print("Searching for: %s" % page_py.title.upper())
    #Print "Searching for: "

    print("Page - Summary: %s" % page_py.summary[0:250])
    #Print "Page - Summary: "


window.close()
