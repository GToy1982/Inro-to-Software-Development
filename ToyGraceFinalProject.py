""" Program IDLE Shell 3.12
    Author Grace Toy

This program will prompt the user to answer two questions it will then use
the preset logic to suggest careers to the user
"""


import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class CallingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("What's My Calling")
        self.geometry("500x350")
        self.configure(bg="#333333")

        # Define the style variable at the class level
        self.style = ttk.Style(self)

        self.notebook = ttk.Notebook(self)
        self.page1 = ttk.Frame(self.notebook, style="TFrame")
        self.page2 = ttk.Frame(self.notebook, style="TFrame")

        self.create_styles()  # Create styles

        self.create_page1(self.page1)
        self.create_page2(self.page2)

        self.notebook.add(self.page1, text="Questions")
        self.notebook.add(self.page2, text="Results")

        self.notebook.pack(expand=True, fill="both")

        #Clear button
    def clear_answers(self):
        self.var_q1.set("")
        self.var_q2.set("")


    def create_styles(self):
        # Configure the style for the introduction label
        self.style.configure("IntroLabel", background="#333333", foreground="#FFFFFF", font=("Arial", 16, "bold"))

        # Frame Style
        self.style.configure("TFrame", background="#333333")

        # Label Style
        self.style.configure("TLabel", background="#333333", foreground="#FFFFFF", font=("Arial", 12))

        # Radiobutton Style
        self.style.configure("TRadiobutton", background="#333333", foreground="#FFFFFF", font=("Arial", 10))

        # Button Style
        self.style.configure("TButton", background="#4CAF50", foreground="#333333", font=("Arial", 12))

    def create_page1(self, parent):
        # Introduction
        intro_label = ttk.Label(parent, text="WONDERING WHAT TO DO AFTER HIGH SCHOOL?", style="TLabel")
        intro_label.pack(pady=10)

        # Page 1 - picture
        img1 = ImageTk.PhotoImage(Image.open("download.jpg"))
        label = ttk.Label(parent, image=img1)
        label.image = img1
        label.pack()

        # Page 1 - Questions
        label1 = ttk.Label(parent, text="What is your favorite school subject?", style="TLabel")
        label1.pack(pady=10)

        options1 = ["Math", "Science", "Art"]
        self.var_q1 = tk.StringVar()

        for option in options1:
            ttk.Radiobutton(parent, text=option, variable=self.var_q1, value=option, style="TRadiobutton").pack()

        label2 = ttk.Label(parent, text="What is your favorite hobby?", style="TLabel")
        label2.pack(pady=10)

        options2 = ["Playing video games", "Doing something creative", "Taking things apart, and putting them back together"]
        self.var_q2 = tk.StringVar()

        for option in options2:
            ttk.Radiobutton(parent, text=option, variable=self.var_q2, value=option, style="TRadiobutton").pack()

        submit_button = ttk.Button(parent, text="Submit", command=self.show_results, style="TButton")
        submit_button.pack(pady=10)

        clear_button = ttk.Button(parent, text="Clear", command=self.clear_answers, style="TButton")
        clear_button.pack(pady=10)



    def create_page2(self, parent):
        # Page 2 - Heading
        job_desc_label = ttk.Label(parent, text="CAREER IDEAS THAT YOU SHOULD CONSIDER", style="TLabel")
        job_desc_label.pack(pady=10)

        # page 2 - picture
        img1 = ImageTk.PhotoImage(Image.open("download2.jpg"))
        label = ttk.Label(parent, image=img1)
        label.image = img1
        label.pack()

        #Page 2 - Results
        self.results_label = tk.Listbox(parent, selectbackground="#4CAF50", selectforeground="#333333",
                                        font=("Arial", 14), bg="#333333", fg="#FFFFFF", selectmode=tk.SINGLE)
        self.results_label.pack(pady=10, padx=10, expand=True, fill=tk.BOTH, anchor="center")  # Set anchor to center

        save_button = ttk.Button(parent, text="Save Results", command=self.save_results, style="TButton")
        save_button.pack(side=tk.LEFT, padx=10)

        try_again_button = ttk.Button(parent, text="Try Again", command=self.reset_answers, style="TButton")
        try_again_button.pack(side=tk.LEFT, padx=10)

        exit_button = ttk.Button(parent, text="Exit", command=self.exit_application, style="TButton")
        exit_button.pack(side=tk.RIGHT, padx=10)

    def show_results(self):
        answer_q1 = self.var_q1.get()
        answer_q2 = self.var_q2.get()
        job_suggestions = self.determine_job_suggestions(answer_q1, answer_q2)

        # Clear previous suggestions
        self.results_label.delete(0, tk.END)

        # Calculate the number of lines to center the text
        num_lines = len(job_suggestions)
        start_line = max(0, (self.results_label.winfo_height() - num_lines) // 2)

        # Display new suggestions with a space between each result
        for suggestion in job_suggestions:
            self.results_label.insert(tk.END, suggestion)
            start_line += 1
            # Add an empty string for space without anchor and justify
            self.results_label.insert(tk.END, "")

        self.notebook.select(self.page2)

    def determine_job_suggestions(self, answer_q1, answer_q2):
        suggestions = {
            "Math+Playing video games": ["Game Programmer - The role of the game programmer is to develop the software to create video games."],
            "Math+Doing something creative": ["Programmer - A programmer is someone who writes/creates computer software or applications.", "Market Researcher - A Market Researcher pulls information from surveys, research reports, trend data, and business assessments.", "Astronomer - A scientist in the field of astronomy who focuses their studies on a specific question or field outside the scope of Earth."],
            "Math+Taking things apart, and putting them back together": ["Analyst - An individual who performs analysis of a topic.", "Actuary - A professional with advanced mathematical skills who deals with the measurement and management of risk and uncertainty.", "Mechanic - A skilled tradesperson who uses tools to build, maintain, or repair machinery, especially cars."],
            "Science+Playing video games": ["Researcher - An information professional who uses research methodologies to gather data, analyze that data and present their findings.", "Chemist - A chemist studies the composition, structure, properties, and behavior of matter."],
            "Science+Doing something creative": ["Biologist - a scientist who focuses on living organisms, including plants and animals.", "Clinical Technician - A laboratory worker who performs blood tests, urinalysis, and other tests on specimens."],
            "Science+Taking things apart, and putting them back together": ["Engineer - A person whose job is to design or build machines, engines or electrical equipment, or things such as roads, railways or bridges, using scientific principles", "Electronic Repair Technician - An electronics repair technician assists in the design, development, testing, repair, and maintenance of electronic and electrical equipment."],
            "Art+Playing video games": ["Illustrator - An artist who specializes in enhancing writing or elucidating concepts by providing a visual representation.", "Animator - An artist who creates multiple images, known as frames, which give an illusion of movement called animation when displayed in rapid sequence."],
            "Art+Doing something creative": ["Artist - A person engaged in an activity related to creating art, practicing the arts, or demonstrating an art.", "Interior Decorator - A professional skilled at beautifying a space using style, color, furniture, and accessories.", "Web Designer - A creative IT professional who designs the visual appearance, organizes the layout, and ensures the easy navigation of a website."],
            "Art+Taking things apart, and putting them back together": ["Art Conservator - An art conservator restores, repairs and preserves different works of fine art. They often specialize in a specific object or material.", "Robotics Engineer - A robotics engineer designs, builds and tests robots and robotic platforms."]
        }

        key = f"{answer_q1}+{answer_q2}"
        return suggestions.get(key, ["No suggestions available"])

    def save_results(self):
        filename = "job_suggestions.txt"
        with open(filename, "w") as file:
            suggestions = self.results_label.get(0, tk.END)
            file.write("\n".join(suggestions))

        messagebox.showinfo("Save Results", f"Results saved to {filename}")

    def reset_answers(self):
        self.var_q1.set("")
        self.var_q2.set("")
        self.notebook.select(self.page1)

    def exit_application(self):
        result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if result:
            print("Goodbye!")
            self.destroy()

if __name__ == "__main__":
    app = CallingApp()
    app.mainloop()
