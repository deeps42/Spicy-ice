from tkinter import *
import random

temp = 1


class Bill_App:
    def __init__(self, root):
        cust_detail_fg="#ffff99"
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1350, height=750)
        self.root.minsize(width=1350, height=750)
        self.root.title("ICE-SPICE______(created by - AMIT SINGH)")
        self.root.configure(bg=cust_detail_fg)

        # ====================Variables========================
        self.cus_name = StringVar()
        self.c_phone = StringVar()

        # For Generating Random Bill Numbers for the random bill no for instant use only
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()

        # Setting bill no to a random variable
        self.c_bill_no.set(x)

        self.choclate = IntVar()
        self.strawberry = IntVar()
        self.vanilla = IntVar()
        self.cone = IntVar()
        self.stick = IntVar()
        self.fries = IntVar()
        self.noodles = IntVar()
        self.burger = IntVar()
        self.veg_roll = IntVar()
        self.pani_puri = IntVar()
        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()
        self.total_temp= StringVar()

        # ===================================
        bg_color = "#339933"
        fg_color = "white"
        lbl_color = 'white'
        spice_frame_color= "#cc3300"
        ice_item_fg = "#00c8ff"

        # Title of App
        title = Label(self.root, text="~~~~~~ ICE - SPICE ~~~~~~", bd=12, relief=GROOVE, fg="#ffcc00", bg=bg_color,
                      font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        # ==========Customers Details Frame==========#
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(F1, text="Bill No : ", bg=bg_color, fg=cust_detail_fg, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=0, padx=10, pady=5)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=1, ipadx=30, ipady=4, pady=5)

        # ===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name : ", bg=bg_color, fg=cust_detail_fg,
                          font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=30)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=3, ipady=4, ipadx=20, pady=15)

        # =================Customer Phone==============#
        cphon_lbl = Label(F1, text="Phone No : ", bg=bg_color, fg=cust_detail_fg, font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=5, ipady=4, ipadx=30, pady=5)

        # ==================ICE Frame=====================#
        F2 = LabelFrame(self.root, text='ICE', bd=10, relief=GROOVE, bg=bg_color, fg="#00ffff",
                        font=("times new roman", 23, "bold","underline"))
        F2.place(x=40, y=185, width=360, height=390)

        # ===========Frame Content
        #==========  choclate
        bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=ice_item_fg, bg=bg_color, text="CHOCLATE :")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.choclate)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # ======= strawberry
        face_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=ice_item_fg, bg=bg_color, text="STRAW-BERRY :")
        face_lbl.grid(row=1, column=0, padx=10, pady=20)
        face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.strawberry)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # ======== vanilla
        wash_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=ice_item_fg, bg=bg_color, text="VANILLA :")
        wash_lbl.grid(row=2, column=0, padx=10, pady=20)
        wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.vanilla)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ======== cone
        hair_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=ice_item_fg, bg=bg_color, text="CONE :")
        hair_lbl.grid(row=3, column=0, padx=10, pady=20)
        hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.cone)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============ stick
        lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=ice_item_fg, bg=bg_color, text="STICK :")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.stick)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ================== Spice Frame =====================#
        F2 = LabelFrame(self.root, text='SPICE', bd=10, relief=GROOVE, bg=bg_color, fg="#ff3300",
                        font=("times new roman", 23, "bold","underline"))
        F2.place(x=480, y=185, width=350, height=390)

        # ===========Frame Content
        fries_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=spice_frame_color, bg=bg_color, text="VEG-ROLL :")
        fries_lbl.grid(row=0, column=0, padx=10, pady=20)
        fries_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.fries)
        fries_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=spice_frame_color, bg=bg_color, text="BURGER :")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.burger)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        daal_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=spice_frame_color, bg=bg_color, text="NOODLES :")
        daal_lbl.grid(row=2, column=0, padx=10, pady=20)
        daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.noodles)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        veg_roll_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=spice_frame_color, bg=bg_color, text="FRIES :")
        veg_roll_lbl.grid(row=3, column=0, padx=10, pady=20)
        veg_roll_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.veg_roll)
        veg_roll_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        pani_puri_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=spice_frame_color, bg=bg_color, text="PANI-PURI :")
        pani_puri_lbl.grid(row=4, column=0, padx=10, pady=20)
        pani_puri_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.pani_puri)
        pani_puri_en.grid(row=4, column=1, ipady=5, ipadx=5)



        # ====== created by frame

        F2 = LabelFrame(self.root,bd=5, relief=FLAT, bg=bg_color, fg="gold",
                        font=("times new roman", 10, "bold"))
        F2.place(x=1125, y=12, width=210, height=40)

        # ===========Frame Content
        fries_lbl = Label(F2, font=("times new roman", 12, "bold","underline"), fg="#ffcc00", bg=bg_color, text="created by ~ AMIT SINGH")
        fries_lbl.grid(row=0, column=0, padx=10, pady=10)




       # ===================Bill Aera================#
        F3 = Label(self.root, bd=10, relief=GROOVE,bg="gold",fg=fg_color)
        F3.place(x=910, y=190, width=325, height=380)
        # ===========
        bill_title = Label(F3, text="Bill List", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE, fg="gold",bg=bg_color)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Menu=============#
        F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=580, relwidth=1, height=150)

        # ===================
        cosm_lbl = Label(F4, font=("times new roman", 15, "bold"), fg="cyan", bg=bg_color, text="TOTAL-ICY:")
        cosm_lbl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_food)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # ===================
        gro_lbl = Label(F4, font=("times new roman", 15, "bold"), fg="#ff3300", bg=bg_color, text="TOTAL-SPICY:")
        gro_lbl.grid(row=1, column=0, padx=10, pady=20)
        gro_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_grocery)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

        # ================
        cosmt_lbl = Label(F4, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, text="Total :")
        cosmt_lbl.grid(row=0, column=2, padx=30, pady=0)
        cosmt_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_temp)
        cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # ===================
        total_btn = Button(F4, text="TOTAL", bg=bg_color, fg="gold", font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.total)
        total_btn.grid(row=1, column=3, ipadx=20, padx=20, pady=15)

        # ========================
        genbill_btn = Button(F4, text="GENERATE BILL", bg=bg_color, fg="gold", font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=15, padx=25)

        # ====================
        clear_btn = Button(F4, text="CLEAR", bg=bg_color, fg="gold", font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=15, padx=25)

        # ======================
        exit_btn = Button(F4, text="EXIT", bg=bg_color, fg="gold", font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=15, padx=25)

        # =======================
        next_btn = Button(F4, text="NEXT", bg=bg_color, fg="gold", font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.next)
        next_btn.grid(row=1, column=8, ipadx=15, padx=25)

    # Function to get total pfriess
    def total(self):
        # =================Total ICY PRODUCTS
        self.total_food_pfriess = (
                (self.choclate.get() * 30) +
                (self.strawberry.get() * 30) +
                (self.vanilla.get() * 30) +
                (self.cone.get() * 20) +
                (self.stick.get() * 15)
        )
        self.total_food.set(str(self.total_food_pfriess))
        self.tax_cos.set(str(round(self.total_food_pfriess * 0)))

        # ====================Total SPICY PRODUCTS
        self.total_grocery_pfriess = (
                (self.veg_roll.get() * 25) +
                (self.burger.get() * 25) +
                (self.noodles.get() * 30) +
                (self.fries.get() * 20) +
                (self.pani_puri.get() * 10)

        )
        self.total_grocery.set(str(self.total_grocery_pfriess))
        self.tax_groc.set(str(round(self.total_grocery_pfriess * 0)))

        self.total_temp_pfriess = (self.total_food_pfriess +
                           self.total_grocery_pfriess +
                           self.total_food_pfriess * 0 +
                           self.total_grocery_pfriess * 0
                           )
        self.total_temp.set(str(self.total_temp_pfriess) + " (Rs)")

    # Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "       Welcome To ICE - SPICE\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")

    # Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0', END)

    # Add Product name , qty and pfries to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.choclate.get() != 0:
            self.txt.insert(END, f"\nChoclate          {self.choclate.get()}           {self.choclate.get() * 30}")
        if self.strawberry.get() != 0:
            self.txt.insert(END, f"\nStrawberry        {self.strawberry.get()}           {self.strawberry.get() * 30}")
        if self.vanilla.get() != 0:
            self.txt.insert(END, f"\nVanilla           {self.vanilla.get()}           {self.vanilla.get() * 30}")
        if self.cone.get() != 0:
            self.txt.insert(END, f"\nCone              {self.cone.get()}           {self.cone.get() * 20}")
        if self.stick.get() != 0:
            self.txt.insert(END, f"\nStick             {self.stick.get()}           {self.stick.get() * 15}")
        if self.veg_roll.get() != 0:
            self.txt.insert(END, f"\nVeg-Roll          {self.veg_roll.get()}           {self.veg_roll.get() * 25}")
        if self.burger.get() != 0:
            self.txt.insert(END, f"\nBurger            {self.burger.get()}           {self.burger.get() * 25}")
        if self.noodles.get() != 0:
            self.txt.insert(END, f"\nNoodles           {self.noodles.get()}           {self.noodles.get() * 30}")
        if self.fries.get() != 0:
            self.txt.insert(END, f"\nFries             {self.fries.get()}           {self.fries.get() * 20}")
        if self.pani_puri.get() != 0:
            self.txt.insert(END, f"\nPani-Puri         {self.pani_puri.get()}           {self.pani_puri.get() * 10}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n\n                   Total(Rs):  {self.total_food_pfriess + self.total_grocery_pfriess + self.total_food_pfriess * 0 + self.total_grocery_pfriess * 0}")

    def exit(self):
        self.root.destroy()

    def next(self):
        self.txt.delete('1.0', END)



root = Tk()
object = Bill_App(root)
root.mainloop()
