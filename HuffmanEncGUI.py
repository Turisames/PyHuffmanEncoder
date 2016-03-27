import tkinter as tk, winsound
import tkinter.filedialog as filedialog
import program, os.path
'''
A class for providing a graphical user interface to my
Huffman Encoder.
You can choose a file from the dialogue, and the software
will perform a Huffman Encoding.
'''
class mainWindow:
    def __init__(self):

        self.__root = tk.Tk()
        self.__root.title( "Huffman Encoder" )
        self.__root.iconbitmap("oneup.ico")

        self.__button = tk.Button( self.__root, text="Choose a file.", command=self.choose_file )
        self.__button.pack(  )

        self.__text = tk.Text( self.__root )
        self.__text.pack()

        self.__root.mainloop()

    def choose_file(self):
        myFile = filedialog.askopenfilename( filetypes=[ ("text files", ".txt") ] )

        # In case filedialogue is interrupted.
        if myFile == None or myFile == "":
            return

        charDict = program.create_dict( myFile )
        vektor = program.chars_in_order( charDict )

        self.__text.delete( 1.0, tk.END )

        myFile = os.path.basename( myFile )

        # Start writing information.
        self.__text.insert( tk.END, myFile + "\n" )
        for rivi in vektor:
            self.__text.insert( tk.END, rivi + "\n" )

        return myFile
#
mainWindow()