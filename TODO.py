import tkinter as tk 

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window appearance
        self.config(bg="#524948")
        self.title("To Do List")
        self.geometry("400x700")

        #calls the method that creates the ui/ux
        self.build_app()

        #method that build the ui/ux
    def build_app(self):
        #Label sa taas
        tk.Label(self,
                 text="TODO LIST",
                 font=("Arial", 20, "bold")
                 ).pack(pady=10)
        
        #stores the tasks
        self.tasks = []
        self.filename = "task.txt"


        #stores the user input for later use
        self.entry_task = tk.Entry(self,
                                   width=20,
                                   font=("Arial", 15, "bold"),
                                   highlightthickness=10,
                                   highlightcolor="#57467B",
                                   justify="center"
                                   )
        self.entry_task.bind("<Return>", self.add_task)
        self.entry_task.pack(ipady=10)

        self.add_button  = tk.Button(self,
                                 text="Add task",
                                 font=("Arial", 13),
                                 width=15,
                                 relief="raised",
                                 bd=5,
                                 command=self.add_task
                                 )
        self.add_button.pack(pady=15)

        self.delete_button  = tk.Button(self,
                                 text="delete task",
                                 font=("Arial", 13),
                                 width=15,
                                 relief="raised",
                                 bd=5,
                                 command=self.delete_task
                                 )
        self.delete_button.pack(pady=15)

        self.clear_all_button  = tk.Button(self,
                                 text="CLEAR ALL TASKS",
                                 font=("Arial", 11),
                                 width=15,
                                 relief="raised",
                                 bd=5,
                                 command=self.clear_all_task
                                 )
        self.clear_all_button.pack(pady=15)

        #displays the tasks
        self.task_lists = tk.Listbox(self,
                                    width=20,
                                    font=("Arial", 15, "bold"),
                                    height=8
                                     )
        self.task_lists.pack(pady=10)

        self.label = tk.Label(self,
                              text="ENTER YOUR TASK",
                              font=("Arial", 15)
                              )
        self.label.pack(pady=10)

        self.load_task()
    
    def add_task(self, event=None):
        task = self.entry_task.get().strip().upper()
        
        if task == "":
            self.label.config(text="PLEASE INPUT A TASK")
            return

        self.tasks.append(task)
        self.task_lists.insert(tk.END, task)
        self.entry_task.delete(0, tk.END)
        self.label.config(text=f"{task} ADDED")
        self.save_task()

    def delete_task(self):
        selected = self.task_lists.curselection()

        if not selected:
            self.label.config(text="PLEASE SELECT A TASK")
            return
        
        index = selected[0]

        self.task_lists.delete(index)
        deleted_task = self.tasks.pop(index)

        self.label.config(text=f"{deleted_task} deleted")
        
        self.save_task()


    def clear_all_task(self):
        self.task_lists.delete(0, tk.END)
        self.tasks.clear()
        self.save_task()
        self.label.config(text="ALL TASKS CLEARED")

    def save_task(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task+"\n")

    def load_task(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    task = line.strip()

                    if task != "":
                        self.tasks.append(task)
                        self.task_lists.insert(tk.END, task)

        except FileNotFoundError:
            pass

Window().mainloop()