from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")              
        self.root.title("face Recognition System")

        # ------------  variable----------------------
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # first images
        img1 = Image.open(r"D:\face2\images\22.jpg")
        img1 = img1.resize((700,200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=700, height=200)

        # Second Images
        img2 = Image.open(r"D:\face2\images\18.jpg")
        img2 = img2.resize((700,200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=700, y=0, width=700, height=200)

        # BackGround Images
        img4 = Image.open(r"D:\face2\images\4.jpg")
        img4 = img4.resize((1400,700), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1400, height=700)

        title_lb1 = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM ", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lb1.place(x=0, y=0, width=1400, height=45)

        # making a frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=50, width=1330, height=510)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Detail", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=2, width=650, height=500)

        img_left = Image.open(r"D:\face2\images\22.jpg")
        img_left = img_left.resize((635, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb1 = Label(Left_frame, image=self.photoimg_left)
        f_lb1.place(x=5, y=0, width=635, height=70) 

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=75, width=640, height=340)

        # label and entry
        # attendance Id
        attendanceId_label = Label(left_inside_frame, text="AttendanceId", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # Roll
        rollLabel = Label(left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold"))
        atten_roll.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        nameLabel = Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        atten_name = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=637, height=35)

        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=2, width=640, height=500)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=620, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendaceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Attendance ID")
        self.AttendaceReportTable.heading("roll", text="Roll")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("attendance", text="Attendance")

        self.AttendaceReportTable["show"] = "headings"

        self.AttendaceReportTable.column("id", width=100)
        self.AttendaceReportTable.column("roll", width=100)
        self.AttendaceReportTable.column("name", width=100)
        self.AttendaceReportTable.column("department", width=100)
        self.AttendaceReportTable.column("time", width=100)
        self.AttendaceReportTable.column("date", width=100)
        self.AttendaceReportTable.column("attendance", width=100)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # Function to fetch data from the CSV file
    def fetchData(self, rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("", END, values=i)

    # Function to import CSV data
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Function to export updated data to CSV
    def exportCsv(self):
        try:
            # Gather the current data from the Treeview to ensure it's up-to-date
            updated_data = []
            for row_id in self.AttendaceReportTable.get_children():
                row = self.AttendaceReportTable.item(row_id)['values']
                updated_data.append(row)

            if len(updated_data) < 1:
                messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
                return False
            
            # Prompt for file save location
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            
            # Write the updated data to the CSV file
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for row in updated_data:
                    exp_write.writerow(row)
                messagebox.showinfo("Data Export", "Your Data Exported to " + os.path.basename(fln) + " Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Function to get cursor position and update fields
    def get_cursor(self, event=""):
        cursor_row = self.AttendaceReportTable.focus()
        content = self.AttendaceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    # Function to update the data in the CSV
    def update_data(self):
        selected_row = self.AttendaceReportTable.selection()
        if not selected_row:
            messagebox.showerror("Error", "No row selected", parent=self.root)
            return

        # Get the current selected row values
        current_values = self.AttendaceReportTable.item(selected_row, "values")

        # Update the values in the Treeview
        self.AttendaceReportTable.item(selected_row, values=(
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        ))

        # Update the global mydata list
        for i, row in enumerate(mydata):
            if row[0] == current_values[0]:  # Assuming the first column is the unique identifier
                mydata[i] = (
                    self.var_atten_id.get(),
                    self.var_atten_roll.get(),
                    self.var_atten_name.get(),
                    self.var_atten_dep.get(),
                    self.var_atten_time.get(),
                    self.var_atten_date.get(),
                    self.var_atten_attendance.get()
                )
                break

        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

    # Function to reset data fields
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
