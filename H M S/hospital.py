from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FutherInformation = StringVar()
        self.storageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Dataframe
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # Buttons
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # Details
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # Dataframe Left
        lblNameTablet = Label(DataframeLeft, text="Name Of Tablets", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"] = ("nice", "corona vaccine", "acetaminophen", "adderall", "amlodipine", "ativan")
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.NumberofTablets, width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.sideEfect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2, pady=6)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.FutherInformation, width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblDrivingMachine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblDrivingMachine.grid(row=1, column=2, sticky=W)
        txtDrivingMachine = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtDrivingMachine.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage:", padx=2)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.storageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DateofBirth, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        # Dataframe Right
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Buttons
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.iPrescription)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.idelete)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.clear)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.iExit)
        btnExit.grid(row=0, column=5)

        # Details Frame
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"))
        self.hospital_table.heading("nameoftablets", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")
        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "No of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effects:\t\t\t" + self.sideEfect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FutherInformation.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.storageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Driving Using Machine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END, "Patient Id:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DateofBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")

    def iPrescriptionData(self):
        if self.ref.get() == "" or self.Dose.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="vaigainathan614", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO hospital (Nameoftablets, ref, Dose, NumberofTablets, Lot, Issuedate, ExpDate, DailyDose, Storage, NHSNumber, PatientName, DateofBirth, PatientAddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.storageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateofBirth.get(),
                self.PatientAddress.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="vaigainathan614", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE hospital SET Nameoftablets=%s, Dose=%s, NumberofTablets=%s, Lot=%s, Issuedate=%s, ExpDate=%s, DailyDose=%s, Storage=%s, NHSNumber=%s, PatientName=%s, DateofBirth=%s, PatientAddress=%s WHERE ref=%s", (
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.storageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateofBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="vaigainathan614", database="mydata")
        my_cursor = conn.cursor()
        query = "DELETE FROM hospital WHERE ref=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Record has been deleted")
        self.clear()

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FutherInformation.set("")
        self.storageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iExit > 0:
            self.root.destroy()
            return


if __name__ == "__main__":
    root = Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
