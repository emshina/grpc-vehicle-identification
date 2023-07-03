from tkinter import *
from tkinter import ttk
import tkinter as tk
import grpc

from tkinter import messagebox


import registration_pb2 as pb
import registration_pb2_grpc as pb_grpc


app = Tk()
app.configure(bg="black",highlightthickness=7,highlightcolor="PowderBlue")
screen_width = app.winfo_screenwidth()
scree_height= app .winfo_screenheight()

frame =Frame(app,width=screen_width-30,height=scree_height-40,bg="black")

frame.grid(row=1,column=0)

system_Name =Label(frame,padx=0, bd= 20,width=59, relief=RIDGE, text="KENYA VEHICLE REGISTRATION SYSTEM", fg= "PowderBlue", bg="black", font=("times new roman",30))
system_Name.place(x=1,y=1)

def select_item(event):
    select_item.has_been_called= True
    try:
        global x
        index = tree.selection()[0]
        x = tree.item(index)['values']
        number_plate_entry.delete(0, END)
        number_plate_entry.insert(END, x[1])
        email_entry.delete(0, END)
        email_entry.insert(END, x[3])
        id_entry.delete(0, END)
        id_entry.insert(END, x[5])
        print(x[1])
        
        remove_btn = Button(frame, text='Remove Part', width=12, command=remove_item,bg="black",fg="blue")
        remove_btn.place(x=400, y=300)
        
        update_btn = Button(frame, text='Update Part', width=12, command=update_item,bg="black",fg="blue") 
        update_btn.place(x=270, y=300)


    except IndexError:
        pass
    
    
select_item.has_been_called =False

def populate_list():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb_grpc.registrationServiceStub(channel)
        request = pb.FetchRequest()

        response = stub.Fetch(request)

    
    
        tree.delete(*tree.get_children())
        
        for row  in response.data_entries:
                 
                tree.insert("",tk.END,value=row)   



def add_item():

    
    with grpc.insecure_channel('localhost:50051') as channel:
        if number_plate.get() == '' or email.get() == '' or id.get() == '':
           messagebox.showerror('Required Fields', 'Please include all fields')
           return
        stub = pb_grpc.registrationServiceStub(channel)
        request = pb.InsertRequest()
        # Set request fields accordingly
        # try:
        request.Number_plate = number_plate.get().replace(' ', '').lower()
        request.email = email.get()
        request.id =int(id.get()) 
        response = stub.Insert(request)
        if response.success:
                print("Insertion successful!")
        else:
                print("Insertion failed. Error:", response.error)
            
        # except:
        #    messagebox.showerror('Already exist', 'The number plate already exist')
        #    parts_list.delete(0, END)
        
        tree.delete(*tree.get_children())
        tree.insert("",tk.END,(number_plate.get(), email.get(),id.get()))
        clear_text()
        populate_list()
    
    
    
def remove_item():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb_grpc.registrationServiceStub(channel)
        request = pb.DeleteRequest()  
        
        if select_item.has_been_called:
            try:   
                request.Number_plate = x[1]
                response = stub.Delete(request)
        
                if response.success:
                    print("deletion successful!")
                else:
                    print("deletion failed. Error:", response.error)

                clear_text()
                populate_list()
            except:
                messagebox.showerror('Has charges', 'The number plate has committed crimes')
        else:
            messagebox.showerror('Select item', 'select the numberplate to remove')
        
def update_item():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb_grpc.registrationServiceStub(channel)
        request = pb.UpdateRequest()


        print('pk')
        # try:   
        m=request.Number_plate = number_plate.get().replace(' ', '').lower()
        request.email = email.get()
        request.id = int(id.get()) 
        request.condition = x[1]
        print(m)
        
        response = stub.Update(request)
        # populate_list()

        # if response.success:
        #     print("Updating successful!")
        # else:
        #     print("updating failed. Error:", response.error)

        # except:
        #         messagebox.showerror('Has charges', 'The number plate has committed crimes')
    
   
  
    

  

  
        

def clear_text():
    number_plate_entry.delete(0, END)
    email_entry.delete(0, END)
    id_entry.delete(0, END) 
    
    
tree = ttk.Treeview(frame, column=("c1", "c2", "c3","c4"), show='headings',height=10,selectmode='browse')
style =ttk.Style(frame)
style.theme_use("clam")
style.configure("Treeview",background='black',foreground='PowderBlue',fieldbackground='black',font='bold')
style.configure('Treeview.Heading', background="PowderBlue")

tree.column("#1", width=300)
tree.heading("#1",text="Number Plate")
tree.column("#2", width=300)
tree.heading("#2",text="email")
tree.column("#3", width=200)
tree.heading("#3",text="Date of registration")
tree.column("#4", width=200)
tree.heading("#4",text="Identification")
tree.place(x=2,y=340)   
tree.bind('<<TreeviewSelect>>', select_item)



# def run():
#     with grpc.insecure_channel('localhost:50051') as channel:
#         stub = pb_grpc.registrationServiceStub(channel)
#         request = pb.InsertRequest()
#         # Set request fields accordingly
#         request.Number_plate = input('enter Number_plate')
#         request.email = input("enter email")
#         request.id = int(input("enter id"))
#         response = stub.Insert(request)
        
#         if response.success:
#             print("Insertion successful!")
#         else:
#             print("Insertion failed. Error:", response.error)
            
# def pk():
#     with grpc.insecure_channel('localhost:50051') as channel:
#         stub = pb_grpc.registrationServiceStub(channel)
#         request = pb.FetchRequest()

#         response = stub.Fetch(request)
#         # print(response)

#         for data_entry in response.data_entries:
#             print(f"Number_palte: {data_entry.Number_plate}")
#             print(f"email: {data_entry.email}")
#             print(f"id: {data_entry.id}")
            



# Numberplate
number_plate = StringVar()
part_label = Label(frame, text='NumberPlate', font=('bold', 14), pady=20,bg="black",fg="blue",)

part_label.place(x=2, y=90)
number_plate_entry = Entry(frame, textvariable=number_plate,bg="gray",width=30,foreground='brown',font='bold')

number_plate_entry.place(x=130, y=115)

# email
email = StringVar()
customer_label = Label(frame, text='Email', font=('bold', 14),bg="black",fg="blue")

customer_label.place(x=2, y=165)
email_entry = Entry(frame, textvariable=email,bg="gray",width=30,foreground='white',font='bold')
# email_entry.grid(row=1, column=3)
email_entry .place(x=130, y=170)

# Identification
id = StringVar()
retailer_label = Label(frame, text='Identification', font=('bold', 14),bg="black",fg="blue")
# retailer_label.grid(row=2, column=0, sticky=W)
retailer_label.place(x=2, y=225)

id_entry = Entry(frame, textvariable=id,bg="gray",width=30,foreground='white',font='bold')
# id_entry.grid(row=2, column=1)
id_entry.place(x=130, y=232)


# Buttons
add_btn = Button(frame, text='Register', width=12, command=add_item,bg="black",fg="blue")
# add_btn.grid(row=3, column=0, pady=20)
add_btn.place(x=2, y=300)



clear_btn = Button(frame, text='Clear Input', width=12, command=clear_text,bg="black",fg="blue")
# clear_btn.grid(row=3, column=3)
clear_btn.place(x=140, y=300)

app.title('Car registration system')
# app.attributes('-fullscreen', True)

# app.geometry('865x600')

# Populate data
populate_list()

# Start program
app.mainloop()


# if __name__ == '__main__':
    # run()
    # pk()