from tkinter import *

class User:
    def __init__(self, Age, SEX, Weight, Goal):
        self.age = Age
        self.sex = SEX
        self.weight = Weight
        self.goal = Goal

    def TrueWeight(self, weightOPT):
        self.WOPT = weightOPT

        weightKG = self.WOPT / 2.2046
        self.TWOPT = weightKG
        return weightKG

    def TDEE(self, job, excersise):
        self.JOB = job
        self.exre = excersise

        def ActivityLVL(ACTIV):
            LVL = ord(ACTIV)

            if LVL == ord('L'):
                ELVL = 250
            elif LVL == ord('M'):
                ELVL = 325
            elif LVL == ord('V'):
                ELVL = 425
            else:
                ELVL = 500
            return ELVL

        def NEAT(difficulty):
            if difficulty == 1:
                NEAT = 250
            elif difficulty == 2:
                NEAT = 325
            elif difficulty == 3:
                NEAT = 425
            else:
                NEAT = 500
            return NEAT

        BMR = self.TWOPT * 20
        TEF = BMR * 0.1
        EEEt = ActivityLVL(self.exre)
        NEATt = NEAT(self.JOB)
        totalCalC = BMR + TEF + EEEt + NEATt
        return totalCalC

def main():
    #create account
    #input personal information: Fname, Lname, Age, SEX, Goal
    def showinfo():
        infowindow = Toplevel(master=root)
        infowindow.title("account info")
        infowindow.geometry("600x800+300+300")


    root = Tk()
    Var1 = StringVar()
    Var2 = StringVar()
    root.title('Account')
    root.geometry("400x250+350+350")
    label = Label(root, text="Account Information", bg="gray75")
    weight = Label(root, text="weight").place(x = 30 ,y =50)
    Age = Label(root, text="Age").place(x = 30 ,y =90)
    Sex = Label(root, text="Sex").place(x=30, y=130)
    Sexbttns = Radiobutton(root, text="Male", variable=Var1, value=1)
    Sexbttns2 = Radiobutton(root, text="Female", variable=Var1, value=2) 
    Sexbttns.place(x=65, y=130)
    Sexbttns2.place(x=130, y=130)
    Goal = Label(root, text="Goal").place(x = 30 ,y =170)
    Gbttns = Radiobutton(root, text="lose", variable=Var2, value=1)
    Gbttns2 = Radiobutton(root, text="Gain", variable=Var2, value=2)
    Gbttns.place(x=65, y=170)
    Gbttns2.place(x=130, y=170)
    e1 = Entry(root).place(x =75, y =50)
    e2 = Entry(root).place(x =65, y =90)



    calc = Button(root, text="Calculate", command=showinfo)
    label.pack(side=TOP, padx=50, pady=10)
    calc.pack(side=BOTTOM, padx=30, pady=10)

    root.mainloop()
    # input physical information
    #out put information organised


if __name__ == '__main__':
    main()
