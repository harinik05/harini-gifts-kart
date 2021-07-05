import smtplib
from tkinter import *
from fpdf import FPDF
# Do pip install wheel before
from pdf_mail import sendpdf 

class emailReports(Tk):
    def __init__(self):
        super().__init__()
        def layout():
            self.geometry("800x600")

            self.title("send your reports to the inbox")


            self.heading = Label(self,text="Send your email",bg="pink",fg="black",font="10",width="500",height="3")

            self.heading.pack()

            self.address_field = Label(self,text="Recipient Address :")
            self.email_body_field = Label(self,text="Message :")

            self.address_field.place(x=15,y=70)
            self.email_body_field.place(x=15,y=140)

            self.address = StringVar()
            self.email_body = StringVar()


            self.address_entry = Entry(self,textvariable=self.address,width="30")
            self.email_body_entry = Entry(self,textvariable=self.email_body,width="30")

            self.address_entry.place(x=15,y=100)
            self.email_body_entry.place(x=15,y=180)

            self.upload = Button(self, text= "Generate Pdf", command = generate_pdf, width = "30", height = "2", bg = "pink")
            self.upload.place (x=15, y = 220)

            self.button = Button(self,text="Send Message",command=send_message,width="30",height="2",bg="grey")

            self.button.place(x=15,y=300)
        def generate_pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="This is my pdf", ln=1, align="C")
            #self.imagePath = 'C:\\GitHub\\HaltonSchool\\final-project-awesomebunny155\\test.pdf'
            self.pathPdfNo = 'C:/GitHub/HaltonSchool/final-project-awesomebunny155'
            self.pathPdf = 'C:/GitHub/HaltonSchool/final-project-awesomebunny155/idiot.pdf'
            pdf.output(self.pathPdf)

        def send_message():
            
            address_info = self.address.get()
            
            email_body_info = self.email_body.get()
            #path_pdf_info = self.pathPdf.get()
            #imagePath_info = self.outputPDF.get()
            
            print(address_info,email_body_info)
            # DONT PUSH PERSONAL EMAIL
            
            sender_email = "email" # Need to make a company email wherin everything gets sent to and from 
            
            sender_password ="pass"
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            
            server.starttls()
            
            server.login(sender_email,sender_password)
            
            print("Login successful")
            
            emailInformation = sendpdf(sender_email, address_info, sender_password, "Hello World: This is test", email_body_info, 'idiot', self.pathPdfNo)
            emailInformation.email_send()
            #server.sendmail(sender_email,address_info,email_body_info,imagePath_info)
            
            print("Message sent")
            
            self.address_entry.delete(0,END)
            self.email_body_entry.delete(0,END)
        layout()
emailReports().mainloop()