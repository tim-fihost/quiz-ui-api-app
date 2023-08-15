from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterfacec:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score = Label(text="Score: 0",height=5,width=10,bg=THEME_COLOR,fg="white",font=("Arial",15,"bold"))
        self.score.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.text_screen = self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text="Have a nice day!",
                                                   fill=THEME_COLOR,
                                                   font=("Arial",15,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        #True Button
        true_image = PhotoImage(file="day-34\\quizzler-app-start\\images\\true.png")
        self.true_button = Button(image=true_image,highlightthickness=0,command=self.true_case)
        self.true_button.grid(row=2,column=0,pady=20)
        #False Button
        false_image = PhotoImage(file="day-34\\quizzler-app-start\\images\\false.png")
        self.false_button = Button(image=false_image,highlightthickness=0,command=self.false_case)
        self.false_button.grid(row=2,column=1,pady=20)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_screen,text=q_text)
        else:
            self.canvas.itemconfig(self.text_screen,text="You have reached end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        
    def true_case(self):
        self.give_feedback(self.quiz.check_answer("true"))
    def false_case(self):
        self.give_feedback(self.quiz.check_answer("false"))
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_question)