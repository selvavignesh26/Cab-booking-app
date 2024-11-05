from tkinter import *
from tkinter import ttk, messagebox, filedialog
import sqlite3
import time

Item4 = 0

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()

# main Class
class user:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome " + self.username.get()
            self.head.configure(fg="White", bg="black", font=("MV Boli", 30, "bold"))
            self.head.pack(fill=X)
            application = travel(root)

        else:
            messagebox.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            messagebox.showerror('Error!', 'Username Already Taken!')
        else:
            messagebox.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

    # Frame Packing Methods
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='Login Panel', font=('', 20), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=1, font=('', 15), padx=5, pady=5, command=self.login, bg="green").grid()
        Button(self.logf, text=' Create Account ', bd=1, font=('', 15), padx=5, pady=5, command=self.cr,
               bg="red").grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=1, font=('', 15), padx=5, pady=5, command=self.new_user,
               bg="green").grid()
        Button(self.crf, text='Go to Login', bd=1, font=('', 15), padx=5, pady=5, command=self.log,
               bg="red").grid(row=2, column=1)


class travel:

    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.configure(background='black')
        self.root.resizable(width=False, height=False)

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        journeyType = IntVar()
        carType = IntVar()

        varl1 = StringVar()
        varl2 = StringVar()
        varl3 = StringVar()
        reset_counter = 0

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Mobile = StringVar()
        Telephone = StringVar()
        Email = StringVar()

        CabTax = StringVar()
        Km = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        Receipt = StringVar()

        Standard = StringVar()
        FordGalaxy = StringVar()
        FordMondeo = StringVar()

        CabTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")

        Standard.set("0")
        FordGalaxy.set("0")
        FordMondeo.set("0")

        # ===============Define Function==================

        def Reset():
            iMs = messagebox.askyesno("Prompt!", "Do you want to book?")
            if iMs > 0:
                messagebox.showinfo("Prompt!", "Booking Successful!!! Thank you for using our service")

        def Cab_Tax():
            global Item1
            if var1.get() == 1:
                self.txtCabTax.configure(state=NORMAL)
                Item1 = float(50)
                CabTax.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtCabTax.configure(state=DISABLED)
                CabTax.set("0")
                Item1 = 0

        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "CHENNAI":
                    switch = {"COIMBATORE": 450, "TRICHY": 350, "DINDIGUL": 380, "CHENNAI": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "COIMBATORE":
                    switch = {"COIMBATORE": 0, "TRICHY": 300, "DINDIGUL": 340, "CHENNAI": 450}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "TRICHY":
                    switch = {"COIMBATORE": 300, "TRICHY": 0, "DINDIGUL": 40, "CHENNAI": 350}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "DINDIGUL":
                    switch = {"COIMBATORE": 350, "TRICHY": 40, "DINDIGUL": 0, "CHENNAI": 450}
                    Km.set(switch[varl2.get()])

        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state=NORMAL)
                Item3 = float(10)
                Travel_Ins.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtTravel_Ins.configure(state=DISABLED)
                Travel_Ins.set("0")
                Item3 = 0

        def Total_Paid():
            global Item1
            if journeyType.get() == 1:
                Item2 = Km.get()
                Item1 = CabTax.get()  # Set Item1 based on the value of CabTax
                Cost_of_fare = (float(Item1) + (float(Item2) * 2) + Item3 + Item4)
                Cost_of_fare = (Item1 + (float(Item2) * 2) + Item3 + Item4)

                Tax = "Rs " + str('%.2f' % ((Cost_of_fare) * 0.09))
                ST = "Rs " + str('%.2f' % ((Cost_of_fare)))
                TT = "Rs " + str('%.2f' % (Cost_of_fare + ((Cost_of_fare) * 0.9)))
            elif journeyType.get() == 2:
                Item2 = Km.get()
                Cost_of_fare = (Item1 + (float(Item2) * 2) * 1.5 + Item3 + Item4)

                Tax = "Rs " + str('%.2f' % ((Cost_of_fare) * 0.09))
                ST = "Rs " + str('%.2f' % ((Cost_of_fare)))
                TT = "Rs " + str('%.2f' % (Cost_of_fare + ((Cost_of_fare) * 0.9)))
            else:
                Item2 = Km.get()
                Cost_of_fare = (Item1 + (float(Item2) * 3) * 2 + Item3 + Item4)

                Tax = "Rs " + str('%.2f' % ((Cost_of_fare) * 0.09))
                ST = "Rs " + str('%.2f' % ((Cost_of_fare)))
                TT = "Rs " + str('%.2f' % (Cost_of_fare + ((Cost_of_fare) * 0.9)))

            PaidTax.set(Tax)
            SubTotal.set(ST)
            TotalCost.set(TT)

        def save_booking_details():
            booking_details = f"Firstname: {Firstname.get()}\n" \
                              f"Surname: {Surname.get()}\n" \
                              f"Address: {Address.get()}\n" \
                              f"Postcode: {Postcode.get()}\n" \
                              f"Mobile: {Mobile.get()}\n" \
                              f"Email: {Email.get()}\n" \
                              f"Pickup: {varl1.get()}\n" \
                              f"Drop: {varl2.get()}\n" \
                              f"Pooling: {varl3.get()}\n" \
                              f"Base Charge: {CabTax.get()}\n" \
                              f"Distance(KMs): {Km.get()}\n" \
                              f"Travelling Insurance: {Travel_Ins.get()}\n" \
                              f"Paid Tax: {PaidTax.get()}\n" \
                              f"Sub Total: {SubTotal.get()}\n" \
                              f"Total Cost: {TotalCost.get()}"

            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if file_path:
                with open(file_path, "w") as file:
                    file.write(booking_details)
                    messagebox.showinfo("Information", "Booking details saved successfully!")

        # ===================mainframe================================
        MainFrame = Frame(self.root)
        MainFrame.pack(fill=BOTH, expand=True)

        Tops = Frame(MainFrame, bd=10, bg="black", width=800, relief=RIDGE)
        Tops.pack(side=TOP, fill=BOTH)

        self.lblTitle = Label(Tops, font=('MV Boli', 30, 'bold'), text="\t   Taxi Booking System ", bg="black",
                              fg="white", bd=10, anchor='w')
        self.lblTitle.grid()

        # =====================customerframedetail=================================
        CustomerDetailsFrame = LabelFrame(MainFrame, width=400, height=400, bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        FrameDetails = Frame(CustomerDetailsFrame, width=480, height=300, bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT, fill=BOTH, expand=True)

        CustomerName = LabelFrame(FrameDetails, width=150, height=250, bd=10, font=('arial', 12, 'bold'),
                                   text="Customer Info", relief=RIDGE)
        CustomerName.grid(row=0, column=0)

        TravelFrame = LabelFrame(FrameDetails, bd=10, width=300, height=250, font=('arial', 12, 'bold'),
                                  text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0, column=1)

        CostFrame = LabelFrame(FrameDetails, width=300, height=150, bd=5, relief=FLAT)
        CostFrame.grid(row=1, column=1)

        # =====================book===================
        Receipt_BottonFrame = LabelFrame(CustomerDetailsFrame, bd=10, width=350, height=300, relief=SUNKEN)
        Receipt_BottonFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        Receipt_BottonFrame.picture = PhotoImage(r"C:\Users\krish\OneDrive\Desktop\taxi.png")
        Receipt_BottonFrame.label = Label(Receipt_BottonFrame, image=Receipt_BottonFrame.picture)
        Receipt_BottonFrame.label.pack()

        # =================CustomerName=========================
        self.lblFirstname = Label(CustomerName, font=('arial', 14, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Firstname, bd=7, insertwidth=2,
                                  justify=RIGHT)
        self.txtFirstname.grid(row=0, column=1)

        self.lblSurname = Label(CustomerName, font=('arial', 14, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=1, column=0, sticky=W)
        self.txtSurname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Surname, bd=7, insertwidth=2,
                                justify=RIGHT)
        self.txtSurname.grid(row=1, column=1, sticky=W)

        self.lblAddress = Label(CustomerName, font=('arial', 14, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Address, bd=7, insertwidth=2,
                                justify=RIGHT)
        self.txtAddress.grid(row=2, column=1)

        self.lblPostcode = Label(CustomerName, font=('arial', 14, 'bold'), text="Postcode", bd=7)
        self.lblPostcode.grid(row=3, column=0, sticky=W)
        self.txtPostcode = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Postcode, bd=7, insertwidth=2,
                                  justify=RIGHT)
        self.txtPostcode.grid(row=3, column=1)

        self.lblMobile = Label(CustomerName, font=('arial', 14, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Mobile, bd=7, insertwidth=2,
                                justify=RIGHT)
        self.txtMobile.grid(row=5, column=1)

        self.lblEmail = Label(CustomerName, font=('arial', 14, 'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Email, bd=7, insertwidth=2,
                               justify=RIGHT)
        self.txtEmail.grid(row=6, column=1)

        # Cab Information
        self.lblPickup = Label(TravelFrame, font=('arial', 14, 'bold'), text="Pickup", bd=7)
        self.lblPickup.grid(row=0, column=0, sticky=W)

        self.cboPickup = ttk.Combobox(TravelFrame, textvariable=varl1, state='readonly',
                                       font=('arial', 20, 'bold'), width=14)
        self.cboPickup['value'] = ('', 'CHENNAI', 'COIMBATORE', 'THENI', 'DINDIGUL','TRICHY','THANJAVUR')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0, column=1)

        self.lblDrop = Label(TravelFrame, font=('arial', 14, 'bold'), text="Drop", bd=7)
        self.lblDrop.grid(row=1, column=0, sticky=W)

        self.cboDrop = ttk.Combobox(TravelFrame, textvariable=varl2, state='readonly',
                                      font=('arial', 20, 'bold'), width=14)
        self.cboDrop['value'] = ('','CHENNAI', 'COIMBATORE', 'THENI', 'DINDIGUL','TRICHY','THANJAVUR')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1, column=1)

        self.lblPooling = Label(TravelFrame, font=('arial', 14, 'bold'), text="Pooling", bd=7)
        self.lblPooling.grid(row=2, column=0, sticky=W)

        self.cboPooling = ttk.Combobox(TravelFrame, textvariable=varl3, state='readonly',
                                         font=('arial', 20, 'bold'), width=14)
        self.cboPooling['value'] = ('', '1', '2', '3', '4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2, column=1)

        # Cab Information
        self.chkCabTax = Checkbutton(TravelFrame, text="Base Charge *", variable=var1, onvalue=1, offvalue=0,
                                       font=('arial', 16, 'bold'), command=Cab_Tax).grid(row=3, column=0, sticky=W)
        self.txtCabTax = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=CabTax, bd=6, width=18,
                                 bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtCabTax.grid(row=3, column=1)

        self.chkKm = Checkbutton(TravelFrame, text="Distance(KMs) *", variable=var2, onvalue=1, offvalue=0,
                                   font=('arial', 16, 'bold'), command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Km, bd=6, width=18, bg="white",
                              state=DISABLED, justify=RIGHT, relief=SUNKEN, highlightthickness=0)
        self.txtKm.grid(row=4, column=1)

        self.chkTravel_Ins = Checkbutton(TravelFrame, text="Travelling Insurance *", variable=var3, onvalue=1,
                                            offvalue=0, font=('arial', 16, 'bold'), command=Travelling).grid(row=5,
                                                                                                                column=0,
                                                                                                                sticky=W)
        self.txtTravel_Ins = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Travel_Ins, bd=6, width=18,
                                       bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5, column=1)

        # payment information
        self.lblPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), text="Paid Tax\t\t", bd=7)
        self.lblPaidTax.grid(row=0, column=1, sticky=W)
        self.txtPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7, bg="white", relief=SUNKEN,
                                   justify=RIGHT)
        self.txtPaidTax.grid(row=0, column=2, sticky=W)

        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="Sub Total\t\t", bd=7)
        self.lblSubTotal.grid(row=1, column=1, sticky=W)
        self.txtSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7, bg="white",
                                    relief=SUNKEN, justify=RIGHT)
        self.txtSubTotal.grid(row=1, column=2, sticky=W)

        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="Total Cost\t\t", bd=7)
        self.lblTotalCost.grid(row=2, column=1, sticky=W)
        self.txtTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, bg="white",
                                      relief=SUNKEN, justify=RIGHT)
        self.txtTotalCost.grid(row=2, column=2, sticky=W)

        # ======================paymentinformation=====================================

        self.btnTotal = Button(TravelFrame, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4,
                                  text="Total", bg="green", command=Total_Paid).grid(row=6, column=0, sticky=W)

       # self.btnReset = Button(TravelFrame, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4,
                                   #text="Reset", bg="red", command=Reset).grid(row=6, column=1, sticky=W)

        self.btnExit = Button(TravelFrame, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4,
                                  text="Exit", bg="blue", command=self.root.destroy).grid(row=6, column=2, sticky=W)

        self.btnSave = Button(TravelFrame, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4,
                                   text="Save", bg="yellow", command=save_booking_details).grid(row=6, column=3, sticky=W)


# creating object
root = Tk()
# passing root to start main frame and all
obj = user(root)
# keep window open
root.mainloop()
