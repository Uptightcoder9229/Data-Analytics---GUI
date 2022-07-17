import os
from tkinter import messagebox, ttk, filedialog
from tkinter import *
from tasks import task2, task3, task4, task5And6
from os import path


class GuiLoad():
# Button click Functions
    def myclick2a(self):
        if self.VisID.get().strip():
            messagebox.showinfo("Disclamer", "Vistor ID not Required for this task")
        if self.DocID.get().strip():
            task2.task2a(self.filename).VeiwCountry(self.DocID.get().strip())
        else:
            messagebox.showinfo("Error", "Enter a Subject document ID")

        return None;

    def myclick2b(self):
        if self.VisID.get().strip():
            messagebox.showinfo("Disclamer", "Vistor ID not Required for this task")
        if self.DocID.get().strip():
            task2.task2b(self.filename).VeiwContient(self.DocID.get().strip())
        else:
            messagebox.showinfo("Error", "Enter a Subject document ID")

        return None;

    def myclick4d(self):
        if self.VisID.get().strip():
            messagebox.showinfo("Disclamer", "Vistor ID not Required for this task")

        if self.DocID.get().strip():
            messagebox.showinfo("Disclamer", "Subject Document ID not Required for this task")

        dta = task4.task4d(self.filename).avid_readers()
        self.loadData(dta)

        return None;

    def myclick3a(self):
        if self.VisID.get().strip():
            messagebox.showinfo("Disclamer", "Vistor ID not Required for this task")

        if self.DocID.get().strip():
            k = task3.task3a(self.filename).VeiwBrowserDoc(self.DocID.get().strip())
        else:
            k = task3.task3a(self.filename).VeiwBrowser()
        return;

    def myclick3b(self):
        if self.VisID.get().strip():
            messagebox.showinfo("Disclamer", "Vistor ID not Required for this task")

        if self.DocID.get().strip():
            k = task3.task3b(self.filename).VeiwBrowserNameDoc(self.DocID.get().strip())
        else:
            k = task3.task3b(self.filename).VeiwBrowserName()
        return;

    def myclick5(self):
        if self.DocID.get().strip():
            a = task5And6.task5(self.filename).AlsoLikes(self.DocID.get().strip(), self.VisID.get().strip())
            self.loadData(a)
        else:
            messagebox.showinfo("Error", "Enter a Subject document ID")

        return;

    def myclick6(self):
        if self.DocID.get().strip():
            task5And6.task6(self.filename).DotPlot(self.DocID.get().strip(), self.VisID.get().strip())

        else:
            messagebox.showinfo("Error", "Enter a Subject document ID")

        return;
    def myclick7(self):
        if self.DocID.get():
            self.DocID.delete(0, END)

        if self.VisID.get():
            self.VisID.delete(0, END)

        return


    def loadData(self, df):
        # Clears any value in treeview if used before
        self.tv1.delete(*self.tv1.get_children())

        # Loads data into treeview
        self.tv1["column"] = list(df.columns)
        self.tv1["show"] = "headings"
        for column in self.tv1["columns"]:
            self. tv1.heading(column, text=column)  # let the column heading = column name

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            self.tv1.insert("", "end", values=row)  # inserts each list into the treeview.

        return

    def myfileClear(self):
        self.fileLabel["text"] = './Data/sample_100k_lines.json'
        self.pathLabel["text"] = 'sample_100k_lines.json'
        self.pathlabel["text"] = 'Selected File:'
        self.filename = './Data/sample_100k_lines.json'
        messagebox.showinfo("Success", "Using Default File")
        return;

    def File_dialog(self):

    #This Function will open the file explorer and assign the chosen file path to label_file

        try:
            filename = filedialog.askopenfilename(initialdir="/",
                                      title="Select A File",
                                      filetype=(("Json files", "*.json"), ("All Files", "*.*")))
            self.fileLabel["text"] = filename
        except:
             messagebox.showinfo("Error", "No file selected, Using Default")


        if self.fileLabel["text"]:
            self.pathLabel["text"] = os.path.basename(self.fileLabel["text"])
            self.pathlabel["text"] = 'Selected File'
        else:
            messagebox.showinfo("Error", "No file selected, Using Default")
            if self.filename:
                self.fileLabel["text"] = self.filename
                self.pathLabel["text"] = os.path.basename(self.fileLabel["text"])
            else:

                self.fileLabel["text"] = './Data/sample_100k_lines.json'
                self.pathLabel["text"] = 'sample_100k_lines.json'
                self.pathlabel["text"] = 'Working File:'
        return
    def checkFile(self, status):

        if status == False:
            messagebox.showinfo("Error", "file Error, Using Default file")
            self.fileLabel["text"] = './Data/sample_100k_lines.json'
            self.pathLabel["text"] = 'sample_100k_lines.json'
            self.pathlabel["text"] = 'Working File:'
            self.filename = './Data/sample_100k_lines.json'



    def fileSelected(self):
        if self.fileLabel["text"]:
           self.filename = self.fileLabel["text"]
           self.pathlabel["text"] = 'Working File:'
        else:
            messagebox.showinfo("Error", "No file selected,")
        return;

    def __init__(self, filename, docid=None, userid=None, task=None):
        self.filename = filename
        self.root = Tk()

        self.root.title("Data Analytics")

        win_width = 750
        win_height = 500
        # Settings For Root Screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        start_x = int((screen_width / 2) - (win_width / 2))
        start_y = int((screen_height / 2) - (win_height / 2))

        self.root.geometry('{}x{}+{}+{}'.format(win_width, win_height,
                                           start_x, start_y))

        # Frame for TreeView
        outputframe= LabelFrame(self.root, text="Output")
        outputframe.place(relx=0.9, x=70, y=3, height=470, width=315, anchor=NE)

        # Frame for open file dialog
        fileframe = LabelFrame(self.root, text="File Manager")
        fileframe.place(relx=0, x=15, y=270, height=200, width=400, anchor=NW)
        filelabel = ttk.Label(fileframe, text="Path of File:")
        filelabel.place(relx=0, x=0, y=10, anchor=NW)
        self.pathlabel = ttk.Label(fileframe, text="Selected File:")
        self.pathlabel.place(relx=0, x=0, y=70, anchor=NW)
        self.fileLabel = ttk.Label(fileframe)

        self.pathLabel = ttk.Label(fileframe)

        if (self.filename):
            self.fileLabel["text"] = self.filename
            self.pathLabel["text"] = os.path.basename(self.filename)
            self.pathlabel["text"] = 'Working File:'
        else:
            self.fileLabel["text"] = './Data/sample_100k_lines.json'
            self.pathLabel["text"] = 'sample_100k_lines.json'
            self.pathlabel["text"] = 'Working File:'
        self.fileLabel.place(relx=0, x=0, y=40, anchor=NW)
        self.pathLabel.place(relx=0, x=100, y=70, anchor=NW)

        # Entry(Input) For DocID
        DocLabel = ttk.Label(self.root, text="Enter Document ID:")
        DocLabel.place(relx=0, x=0, y=10, anchor=NW)
        self.DocID = Entry(self.root, width=45)
        self.DocID.place(relx=0, x=110, y=10, anchor=NW)

        # Entry(Input) For VisID For Task 5
        VisLabel = ttk.Label(self.root, text="Enter Visitor ID:")
        VisLabel.place(relx=0, x=0, y=45, anchor=NW)
        self.VisID = Entry(self.root, width=45)
        self.VisID.place(relx=0, x=110, y=45, anchor=NW)

        # TreeView container to view pandas
        self.tv1 = ttk.Treeview(outputframe)
        self.tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

        treescrolly = Scrollbar(outputframe, orient="vertical",
                                command=self.tv1.yview)  # command means update the yaxis view of the widget
        treescrollx = Scrollbar(outputframe, orient="horizontal",
                                command=self.tv1.xview)  # command means update the xaxis view of the widget
        self.tv1.configure(xscrollcommand=treescrollx.set,
                      yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
        treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
        treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

        # Buttons for the tasks 2a, 2b, , 3a, 3b, 4d, 5, 6
        t2a = Button(self.root, text="2a", padx=15, pady=15, command=self.myclick2a)
        t2a.place(relx=0.1, x=70, y=105, anchor=CENTER)

        t2b = Button(self.root, text="2b", padx=15, pady=15, command=self.myclick2b)
        t2b.place(relx=0.1, x=170, y=105, anchor=CENTER)

        t3a = Button(self.root, text="3a", padx=15, pady=15, command=self.myclick3a)
        t3a.place(relx=0.1, x=70, y=165, anchor=CENTER)

        t3b = Button(self.root, text="3b", padx=15, pady=15, command=self.myclick3b)
        t3b.place(relx=0.1, x=170, y=165, anchor=CENTER)

        t4d = Button(self.root, text="4", padx=18, pady=15, command=self.myclick4d)
        t4d.place(relx=0.1, x=270, y=165, anchor=CENTER)

        t5 = Button(self.root, text="5d", padx=15, pady=15, command=self.myclick5)
        t5.place(relx=0.1, x=70, y=225, anchor=CENTER)

        t6 = Button(self.root, text="6", padx=18, pady=15, command=self.myclick6)
        t6.place(relx=0.1, x=170, y=225, anchor=CENTER)

        clearBut = Button(self.root, text="Clear", padx=18, pady=15, command=self.myclick7)
        clearBut.place(relx=0.1, x=270, y=225, anchor=CENTER)

        fileman = Button(fileframe, text="Open File Manager", padx=18, pady=15, command=self.File_dialog)
        fileman.place(relx=0.1, x=50, y=125, anchor=CENTER)

        selectfile = Button(fileframe, text="Select File", padx=18, pady=15, command=self.fileSelected)
        selectfile.place(relx=0.1, x=190, y=125, anchor=CENTER)

        clearFil = Button(fileframe, text="Clear", padx=18, pady=15, command=self.myfileClear)
        clearFil.place(relx=0.1, x=300, y=125, anchor=CENTER)

        self.root.mainloop()






class GuiDOCLi():

    def __init__(self, filename, docid=None, userid=None, task=None):
        self.filename = filename


        self.docid = docid
        self.userid = userid
        self.task = task

    def Guiload(self):
        if  not (self.filename is None):
            if path.exists(self.filename):
              GuiLoad(self.filename)
        else:
            GuiLoad('./Data/sample_100k_lines.json')


    def GuiLoadData(self, df):
        GuiLoad(self.filename).loadData(df)