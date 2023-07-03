from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter  as tk 

import grpc
import policestation_pb2 as pb
import policestation_pb2_grpc as pb_grpc
import registration_pb2 as pk
import registration_pb2_grpc as pk_grpc


root = Tk()
root.title("Vehicle Identification System")
root.configure(bg="black",highlightthickness=7,highlightcolor="PowderBlue")
screen_width =root.winfo_screenwidth()
scree_height= root.winfo_screenheight()



my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook,width=screen_width-30,height=scree_height-40,bg="black",highlightthickness=7,highlightcolor='blue')
my_frame2 = Frame(my_notebook,width=screen_width-30,height=scree_height-40,bg="black",highlightthickness=7,highlightcolor='blue')
my_frame3= Frame(my_notebook, width=screen_width-30,height=scree_height-40,bg="black",highlightthickness=7,highlightcolor='blue')
my_frame4= Frame(my_notebook, width=screen_width-30,height=scree_height-40,bg="blue")
my_frame1.pack(fill="both", expand=1)

my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)
my_frame4.pack(fill="both", expand=1)


my_notebook.add(my_frame1, text="Owner details")
my_notebook.add(my_frame2, text="Add charges")
my_notebook.add(my_frame3, text="Remove charges")
my_notebook.add(my_frame4, text="Remove charges")

#name of police station





global police_station_details
global code
with grpc.insecure_channel('localhost:50050') as channel:
    stub = pb_grpc.policestationServiceStub(channel)
    request = pb.PolicestationRequest()
    code = request.Police_station_code =474 

    response = stub.Police_station(request)
    
    # print(response)
    
    entries = response.station_entries
    for police_station_details in entries:
        # print(police_station_details.station_name, police_station_details.Police_station_code)
  
        policeStation_name = police_station_details.station_name.upper()
        # print(policeStation_name[0].upper())


    system_Name =Label(my_frame1,padx=0, bd= 20,width=58, relief=RIDGE, text= policeStation_name +" POLICE STATION SYSTEM", fg= "PowderBlue", bg="black", font=("times new roman",30))
    system_Name.place(x=1,y=1)




#tablet1  



tree = ttk.Treeview(my_frame1, column=("c1", "c2", "c3"), show='headings',height=5,selectmode='browse')
style =ttk.Style(my_frame1)
style.theme_use("clam")
style.configure("Treeview",background='black',foreground='PowderBlue',fieldbackground='black',font='bold')
style.configure('Treeview.Heading', background="PowderBlue")

tree.column("#1", width=160)
tree.heading("#1",text="Number Plate")
tree.column("#2", width=160)
tree.heading("#2",text="Phone Number")
tree.column("#3", width=160)
tree.heading("#3",text="Identification")
tree.place(x=4,y=250)
# tree.bind('<<TreeviewSelect>>', select_item)

#scroll in tree view
hs = ttk.Scrollbar(my_frame1,orient="vertical",command=tree.yview)
hs.place(x=290+100+100,y=250,height=100+20)

# hs.configure(command=tree.yview)
tree.configure(yscrollcommand=hs.set)
   


def NtSA_details(id):



    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pk_grpc.registrationServiceStub(channel)
        
        request = pk.FetchNTSARequest()  

        global m_number
        m_number =[] 
        if id =="":
            messagebox.showerror('Required Fields', 'Please Enter the number plate')
        
        
        x = request.Number_plate =id
        # print(x)
        response = stub.FetchNTSA(request)
        # print(response)   
        tree.delete(*tree.get_children())
        for row  in response.data_entries:

            tree.insert("",tk.END,value=(row.Number_plate, row.email, row.id))  
             
        
        
# def clear_plate():
#     Plate_entry.delete(0, END)
     
  

Plate = tk.Label(my_frame1,  text='Enter NUmber Plate: ',font=('bold', 14), pady=20,bg="black",fg="blue",bd=5)  
Plate.place(x=2, y=90)

numberplate1 = StringVar()
Plate_entry= Entry(my_frame1,bg='gray',textvariable=numberplate1, width=30) 
Plate_entry.place(x=200, y=117)

Plate_entry = StringVar()
Details = tk.Button(my_frame1, text='Show Details', bg="black",fg="blue",command=lambda: NtSA_details (str(numberplate1.get().replace(' ', '').lower())),font='bold')
    # command=lambda: my_details(t1.get('1.0',END)))
Details.place(x=6, y=200)



def text_victim():
    l1 = tk.Label(my_frame1,  text='Enter Phone number: ',font=('bold', 14),bg="black",fg="blue",bd=5)  
    l1.place(x=4,y=450) 
    t1 = Entry(my_frame1,bg='gray',textvariable='k') 
    t1.place(x=200,y=460)
    l1 = tk.Label(my_frame1,  text='Text a message :',font=('bold', 14),bg="black",fg="blue",bd=5,padx=0)  
    l1.place(x=4,y=500)
    text_area = Entry(my_frame1,bg="gray",width=50)
    text_area.place(x=200,y=510)
l1 = tk.Button(my_frame1,  text='Text The Victim: ',command=text_victim, width=12, bg="black",fg="blue",bd=5,padx=10)  
l1.place(x=4,y=400) 
  
    
   
   
   
   
   
   

#Tablet2



def select_item(event):
    select_item.has_been_called= True
    try:
        global x_index
        index = charges_tree.selection()[0]
        x_index = charges_tree.item(index)['values']
        # selected_item = charges_tree.get(index)
        # print(index)
        # print(x_index)
        
        
        Number_plate_entry.delete(0, END)
        Number_plate_entry.insert(END, x_index[3])
        Charges_entry.delete(0, END)
        Charges_entry.insert(END, x_index[2])
        
        
        
        # remove_btn = Button(my_frame1, text='Remove Part', width=12, command=remove_item,bg="black",fg="blue")
        # remove_btn.place(x=400, y=300)
        
        # update_btn = Button(    my_frame1, text='Update Part', width=12, command=update_item,bg="black",fg="blue") 
        # update_btn.place(x=270, y=300)


    except IndexError:
        pass
    
    
select_item.has_been_called =False

 #charges_treeview
charges_tree = ttk.Treeview(my_frame2, column=("c1", "c2", "c3"), show='headings',height=10,selectmode='browse')
style =ttk.Style(my_frame2)
style.theme_use("clam")
style.configure("Treeview",background='black',foreground='PowderBlue',fieldbackground='black',font='bold')
style.configure('Treeview.Heading', background="PowderBlue")

charges_tree.column("#1", width=100)
charges_tree.heading("#1",text="Number plate")

charges_tree.column("#2", width=300)
charges_tree.heading("#2",text="Charges")

charges_tree.column("#3", width=300)
charges_tree.heading("#3",text="Date Reported")

# charges_tree.column("#4", width=200)
# charges_tree.heading("#1",text="Number")


charges_tree.grid(row=4,columnspan=4)
# charges_tree.place(x=2,y=340)
charges_tree.bind('<<TreeviewSelect>>', select_item)


#scroll in charges_tree view
hs = ttk.Scrollbar(my_frame2,orient="vertical",command=charges_tree.yview)
# hs.place(x=270+100+100+180,y=300,height=100+20)

# hs.configure(command=charges_tree.yview)
charges_tree.configure(yscrollcommand=hs.set)




def populate_list():
    
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = pb_grpc.policestationServiceStub(channel)
        request = pb.FetchchargesRequest()
        request.Police_station_code_id = police_station_details.Police_station_code
        # print(request)
        response = stub.FetchCharges(request)

        entries = response.Charges_entries
        
        
        global charges_id
        charges_tree.delete(*charges_tree.get_children())  
        for row  in response.Charges_entries:
            charges_tree.insert("",tk.END,value=(row.id,row.Number_plate, row.charges, row.charges))   
            


      

def add_item():

    
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = pb_grpc.policestationServiceStub(channel)
        request = pb.InsertChargesRequest()
        
        if Number_plate.get() == '' or Charges.get() == '' :
            messagebox.showerror('Required Fields', 'Please include all fields')
            return
        try:
       
            request.Number_plate = Number_plate.get().replace(' ', '').lower()
            request.charges = Charges.get()
            request.Police_station_code_id =police_station_details.Police_station_code 
            # print(police_station_details.Police_station_code ,m,Charges.get())
            response = stub.InsertCharges(request)
            if response.success:
                    populate_list()
                    print("Insertion successful!")
            else:
                    print("Insertion failed. Error:", response.error)
                    messagebox.showerror('Not Registered', 'The number plate you entered is not registered')
 
        except:
            messagebox.showerror('Not Registered', 'The server is not responding')
            
    
        charges_tree.insert("",tk.END,(Number_plate.get(), Charges.get()))
        clear_text()
        populate_list()
       
     

def clear_text():
    Number_plate_entry.delete(0, END)
    Charges_entry.delete(0, END)

# Number_Plate
Number_plate = StringVar()
part_label = Label(my_frame2, text='Number Plate', font=('bold', 14),pady=20,bg="black",fg="blue")
part_label.grid(row=0, column=0, sticky=W)
Number_plate_entry = Entry(my_frame2, textvariable=Number_plate,bg="gray")
Number_plate_entry.grid(row=0, column=1)
# Charges
Charges = StringVar()
customer_label = Label(my_frame2, text='Charges', font=('bold', 14),pady=20,bg="black",fg="blue")
customer_label.grid(row=0, column=2, sticky=W)
Charges_entry = Entry(my_frame2, textvariable=Charges,bg='gray')
Charges_entry.grid(row=0, column=3)




   
def remove_item():
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = pb_grpc.policestationServiceStub(channel)
        request = pb.DeleteChargesRequest()
        
        if select_item.has_been_called:
            # try:   
                request.ID = x_index[0]
                request.police_code = code
                response = stub.DeleteCharges(request)
                
                if response.success:
                    print("deletion successful!")
                else:
                    print("deletion failed. Error:", response.error)

                clear_text()
                populate_list()
        #     except:
        #         messagebox.showerror('Has charges', 'The number plate has committed crimes')
        # else:
        #     messagebox.showerror('Select item', 'select the numberplate to remove')
                         

# # Buttons
add_btn = Button(my_frame2, text='Add Charges', width=12, command=add_item,bg="black",fg="blue")
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(my_frame2, text='Remove Charges', width=12, command=remove_item,bg="black",fg="blue")
remove_btn.grid(row=3, column=1)

clear_btn = Button(my_frame2, text='Clear Input', width=12, command=clear_text,bg="black",fg="blue")
clear_btn.grid(row=3, column=2)
# # Populate data
populate_list()





# #tablet 3
# def remove(id):
#     if id =="":
#         messagebox.showerror('Required Fields', 'Please Enter the number plate')
#     remove_list.delete(0, END)
#     for row in db.Remove(id):
#         remove_list.insert(END, row)

# l1 = tk.Label(my_frame3,  text='NUmber Plate: ',font=('bold', 14), pady=20,bg="black",fg="blue",bd=5)  
# l1.grid(row=1,column=0) 
# numberplate3 = StringVar()
# t1 = Entry(my_frame3,bg='gray',textvariable=numberplate3) 
# t1.grid(row=1,column=1) 
# t1 = StringVar()
# b1 = tk.Button(my_frame3, text='Show Details', bg="black",fg="blue",command=lambda: remove(numberplate3.get()))
#     # command=lambda: my_details(t1.get('1.0',END)))
# b1.grid(row=1,column=4) 
# remove_list = Listbox(my_frame3, height=8, width=70,border=7,bg="gray",background='blue')
# remove_list.grid(row=3, column=0, rowspan=6,columnspan=3, pady=20,)
# # Create scrollbar
# scrollbar = Scrollbar(my_frame3)
# scrollbar.grid(row=3, column=3)
# # Set scroll to listbox
# remove_list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=remove_list.yview)


# Start program
root.mainloop()

