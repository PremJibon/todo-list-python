import customtkinter as ctk

def add_to_list():
    todo  = entry.get()
    label = ctk.CTkLabel(scrollable_frame,text=todo)
    label.pack()
    entry.delete(0,ctk.END)

app = ctk.CTk()
app.geometry("750x420")
app.title("Todo List")

label = ctk.CTkLabel(app,text="Daily Task",font=ctk.CTkFont(size=30,weight="bold"))
label.pack(padx=10,pady=20)

scrollable_frame = ctk.CTkScrollableFrame(app,width=500,height=200)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame,placeholder_text="Add-Todo")
entry.pack(fill='x')

add_button = ctk.CTkButton(app,text='Add_to_list',width=300,command=add_to_list)
add_button.pack()

app.mainloop()