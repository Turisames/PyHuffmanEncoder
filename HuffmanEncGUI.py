import tkinter as tk, winsound
import tkinter.filedialog as filedialog
'''
A class for providing a graphical user interface to my
Huffman Encoder.
You can choose a file from the dialogue, and the software
will perform a Huffman Encoding.
'''
class mainWindow:
    def __init__(self):

        self.__root = tk.Tk()

        self.__button = tk.Button( self.__root, text="Choose a file.", command=self.choose_file )
        self.__button.pack(  )

        self.__root.mainloop()

    def choose_file(self):
        myFile = filedialog.askopenfile( filetypes=[ ("text files", ".txt") ] )

        return myFile
#
mainWindow()