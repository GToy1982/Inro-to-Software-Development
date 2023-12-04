import tkinter as tk
from tkinter import ttk, messagebox

class CallingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("What's My Calling")
        self.geometry("400x300")

        self.notebook = ttk.Notebook(self)
        self.page1 = ttk.Frame(self.notebook)
        self.page2 = ttk.Frame(self.notebook)

        self.create_page1(self.page1)
        self.create_page2(self.page2)

        self.notebook.add(self.page1, text="Questions")
        self.notebook.add(self.page2, text="Results")

        self.notebook.pack(expand=True, fill="both")

    def create_page1(self, parent):
        # Page 1 - Questions
        label1 = ttk.Label(parent, text="What is your favorite school subject?")
        label1.grid(row=0, column=0, columnspan=3, pady=10)

        # Question 1 options
        options1 = ["Math", "Science", "Art"]
        self.var_q1 = tk.StringVar()
        for i, option in enumerate(options1):
            ttk.Radiobutton(parent, text=option, variable=self.var_q1, value=option).grid(row=1, column=i, pady=5)

        label2 = ttk.Label(parent, text="What is your favorite hobby?")
        label2.grid(row=2, column=0, columnspan=3, pady=10)

        # Question 2 options
        options2 = ["Playing video games", "Doing something creative", "Taking things apart, and putting them back together"]
        self.var_q2 = tk.StringVar()
        for i, option in enumerate(options2):
            ttk.Radiobutton(parent, text=option, variable=self.var_q2, value=option).grid(row=3, column=i, pady=5)

        submit_button = ttk.Button(parent, text="Submit", command=self.show_results)
        submit_button.grid(row=4, column=0, columnspan=3, pady=10)

    def create_page2(self, parent):
        # Page 2 - Results
        self.results_label = ttk.Label(parent, text="Your Results\n'Job Suggestions'")
        self.results_label.pack(pady=10)

        save_button = ttk.Button(parent, text="Save Results", command=self.save_results)
        save_button.pack(side=tk.LEFT, padx=10)

        try_again_button = ttk.Button(parent, text="Try Again", command=self.reset_answers)
        try_again_button.pack(side=tk.LEFT, padx=10)

        exit_button = ttk.Button(parent, text="Exit", command=self.exit_application)
        exit_button.pack(side=tk.RIGHT, padx=10)

    def show_results(self):
        # Logic to determine job suggestions based on user answers
        answer_q1 = self.var_q1.get()
        answer_q2 = self.var_q2.get()

        job_suggestions = self.determine_job_suggestions(answer_q1, answer_q2)

        # Display results on Page 2
        self.results_label.config(text=f"Your Results\nJob Suggestions:\n{job_suggestions}")
        self.notebook.select(self.page2)

    def determine_job_suggestions(self, answer_q1, answer_q2):
        # Define logic to determine job suggestions based on answers
        suggestions = {
            "Math+Playing video games": "Game Programmer",
            "Math+Doing something creative": "Programmer, Market Researcher, Astronomer",
            "Math+Taking things apart, and putting them back together": "Analyst, Actuary, Mechanic",
            "Science+Playing video games": "Researcher, Chemist",
            "Science+Doing something creative": "Biologist, Clinical Technician",
            "Science+Taking things apart, and putting them back together": "Engineer, Electronic Repair",
            "Art+Playing video games": "Illustrator, Animator",
            "Art+Doing something creative": "Artist, Interior Decorator, Tattoo Artist, Web Designer",
            "Art+Taking things apart, and putting them back together": "Art Preserver, Robotics"
        }

        key = f"{answer_q1}+{answer_q2}"
        return suggestions.get(key, "No suggestions available")

    def save_results(self):
        # Save results to a text file
        filename = "job_suggestions.txt"
        with open(filename, "w") as file:
            file.write(self.results_label.cget("text"))

        messagebox.showinfo("Save Results", f"Results saved to {filename}")

    def reset_answers(self):
        # Reset answers and go back to the Questions page
        self.var_q1.set("")
        self.var_q2.set("")
        self.notebook.select(self.page1)

    def exit_application(self):
        # Display a confirmation dialog before exiting
        result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if result:
            print("Goodbye!")
            self.destroy()


if __name__ == "__main__":
    app = CallingApp()
    app.mainloop()
