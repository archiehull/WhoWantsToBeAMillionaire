import tkinter as tk  #import as tk not from *, as tk is much easier and safer
# from tkinter import messagebox, Frame, ttk, Grid
# from tkinter.ttk import Button
from tkinter import Frame, messagebox, ttk, Grid
from tkinter.ttk import Button
import time
import random
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="applecrumble",#change password
  database = "examquestions"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE examquestions")
#mycursor.execute("SHOW DATABASES")

# drop the table - uncomment this and run the script to drop the table
#mycursor.execute("DROP TABLE questions")


#CREATETABLE - uncomment this section down to an including mydb.commit() to re-make the table - edits can be done or more questions added
# mycursor.execute("CREATE TABLE questions (id INT AUTO_INCREMENT PRIMARY KEY, question LONGTEXT, correct_ans VARCHAR(255), inc1 VARCHAR(255), inc2 VARCHAR(255), inc3 VARCHAR(255), inc4 VARCHAR(255), topic VARCHAR(255), subtopic VARCHAR(255), price VARCHAR(255), friend VARCHAR(255))")
# sql = "INSERT INTO questions (question, correct_ans, inc1, inc2, inc3, inc4, topic, subtopic, price, friend) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# val = [
# ("A BOY KICKS A FOOTBALL WITH A MASS OF 400 G. WHAT IS THE POTENTIAL ENERGY OF THE FOOTBALL WHEN IT IS 0.8 M ABOVE THE GROUND? GRAVITATIONAL FIELD STRENGTH (G) = 10 N/KG.", "3.2 J", "0.032 J", "320 J", "3200J", "32J", "forces", "forces in action", "100", "ENGINEER"),
# ("THE NATIONAL GRID TRANSFERS ENERGY EFFICIENTLY USING HIGH VOLTAGES. WHY ARE HIGH VOLTAGES MORE EFFICIENT?", "High voltages produce a low current which heats wires less", "High voltages produce a high current which heats wires less", "High voltages produce a low current which heats wires more", "High voltages produce a high current which heats wires more", "It saves money", "global challenges", "powering earth", "200", "ELECTRICIAN"),
# ("WHICH STATEMENT DESCRIBES NUCLEAR FUSION?", "Two hydrogen nuclei join to form a helium nucleus", "A helium nucleus joins with a hydrogen nucleus to form an alpha particle", "Two helium nuclei join to form a hydrogen nucleus", "The helium nucleus absorbing neutrons, making it unstable", "Uranium nuclei split and produce high energy neutrons causing a chainreaction", "radioactivity", "radioactive emissions", "300", "TEACHER"),
# ("WHAT IS A TYPICAL WEIGHT OF AN EMPTY SINGLE DECKER SCHOOL BUS?", "120 000 N", "1200 000 N", "12 000 N", "1 200N", "120N", "forces", "forces in action", "500", "ENGINEER"),
# ("HOW WAS THE SUN FORMED?", "From dust and gas pulled together by gravity leading to a fusion reaction", "From dust and gas pulled together by gravity leading to a fission reaction. ", "From dust and gas pushed together by gravity leading to a fission reaction ", "From dust and gas pushed together by gravity leading to a fusion reaction", "The great lord above", "radioactivity", "radioactive emissions", "1000", "TEACHER"),
# ("RADIUM-226 IS THE MOST ABUNDANT ISOTOPE OF RADIUM. ITS NUCLEAR MASS IS 226 AND ITS NUCLEUS CONTAINS 138 NEUTRONS. WHICH OF THE FOLLOWING IS ANOTHER ISOTOPE OF RADIUM?", "nuclear mass 227; 139 neutrons", "nuclear mass 227; 138 neutrons", "nuclear mass 226; 139 neutrons", "nuclear mass 225; 138 neutrons", "nuclear mass 226; 137 neutrons", "radioactivity", "radioactive emissions", "2000", "TEACHER"),
# ("A HOCKEY PLAYER USED PADS ON HER LEGS TO REDUCE INJURIES WHEN HIT BY THE BALL. HOW DO THE PADS AFFECT THE BALL?", "The acceleration and force of the ball is decreased", "The acceleration and force of the ball is increased", "The acceleration of the ball is decreased and the force is increased", "The acceleration of the ball is increased and the force is decreased", "No effect", "forces", "forces in action", "4000", "ENGINEER"),
# ("A RADIOACTIVE SOURCE HAS A HALF-LIFE OF 80 S. HOW LONG WILL IT TAKE FOR 7/8 OF THE SOURCE TO DECAY?", "240 s", "640 s", "70 s", "10 s", "160 s", "radioactivity", "radioactive emissions", "8000", "TEACHER"),
# ("WHICH OF THE FOLLOWING CORRECTLY DESCRIBES THE DOMESTIC ELECTRICITY SUPPLY IN THE UK?", "230V a.c. at 50Hz", "230V a.c. at 60Hz", "230V d.c. at 50Hz", "230V d.c. at 60Hz", "250V d.c. at 60Hz", "global challenges", "powering earth", "16000", "ELECTRICIAN"),
# ("BETA RADIATION IS USED TO CHECK THE THICKNESS OF THIN ALUMINIUM FOIL AT A FACTORY. WHY IS BETA RADIATION USED?", "Beta radiation will partially pass through aluminium foil", "All electromagnetic radiation is reflected by aluminium foil", "Beta radiation will not pass through aluminium foil", "Beta radiation is reflected by aluminium foil", "Beta radiation is absorbed by aluminium foil", "radioactivity", "uses and hazards", "32000", "TEACHER"),
# ("AN ALPHA PARTICLE COLLIDES WITH AN ATOM TO PRODUCE A POSITIVE ION. WHAT HAPPENS TO THE ATOM FOR IT TO BECOME A POSITIVE ION?", "It loses an electron from outside the nucleus", "It loses an electron from inside the nucleus", "It loses a neutron from inside the nucleus", "It loses a proton from outside the nucleus", "It gains a neutron form outside the nucleus", "radioactivity", "radioactive emissions", "64000", "TEACHER"),
# ("A CAR ACCELERATES FROM 0 TO 60MPH (MILES PER HOUR) IN ABOUT 9 SECONDS. USE THE RELATIONSHIP: 1M/S = 2.24MPH TO ESTIMATE THE ACCELERATION FOR THIS CAR IN M/S2.", "3m/s2", "1m/s2", "7m/s2", "15m/s2", "2.24m/s2", "forces", "motion", "125000", "ENGINEER"),
# ("A PLANET MOVES IN A CIRCULAR ORBIT AROUND ITS STAR. WHICH STATEMENT IS CORRECT?", "The planet travels at constant speed but changing velocity", "The planet travels at constant speed and velocity", "The planet travels at changing speed but constant velocity", "The planet travels at changing speed and changing velocity", "The planets speed and velocity doesn't change", "global challenges", "beyond earth", "250000", "ENGINEER"),
# ("A STUDENT MEASURES THE TIME IT TAKES FOR A BICYCLE TO STOP IN AN EMERGENCY. SHE REPEATS THE MEASUREMENT TO GET THREE RESULTS. THE AVERAGE TIME FOR HER RESULTS IS 2.72S. THE FIRST TWO RESULTS ARE 2.66S AND 2.60S. WHAT IS THE VALUE OF HER THIRD RESULT?", "2.90s", "2.72s", "2.66s", "2.63s", "2.60s", "global challenges", "physics on the move", "500000", "ENGINEER"),
# ("A GAS FIRE, USED TO HEAT A ROOM, HAS AN INPUT ENERGY TRANSFER OF 180000J PER MINUTE. THE FIRE HAS AN EFFICIENCY OF 0.8. USE THE EQUATION: EFFICIENCY = USEFUL OUTPUT ENERGY TRANSFER / INPUT ENERGY TRANSFER, CALCULATE THE USEFUL OUTPUT ENERGY TRANSFER PER MINUTE.", "144000J", "36000J", "2400J", "600J", "120000J", "energy", "power and efficiency", "1000000", "ENGINEER"),
#
#
# ]
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

# mycursor.execute("SELECT question FROM questions WHERE id = '1'")
# myresult = mycursor.fetchone()
# print(myresult)
#
# y=1
# z=1
# w=1
# v=1

#mainwin
class main(tk.Tk):
    #*args & *kwargs are special keyword which allows function to take variable length argument
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.initializing_window()

    def initializing_window(self):
        #CONTAINER CREATION
        self.wm_title("WWBAM PHYSICS")
        self.minsize(1024,768)

        ####HEADER
        self.header=tk.Label(self, text="WHO WANTS TO BE A MILLIONAIRE?", font=("Verdana", 40), bg='#4F2B52', fg='#977C41')
        self.header.grid(row=0, column=0, rowspan=1, columnspan= 8, sticky="NSWE", padx=0, pady=0 )

        self.configure(bg='light blue')


        ##FOOTER
        self.footer=tk.Label(self, text="~archie hull", font=("Verdana", 12), bg='#4F2B52')
        self.footer.grid(row=8, column=0, rowspan=1, columnspan= 8, sticky="NSWE", padx=2, pady=2 )

        ## EXIT BUTTON ##
        def clicked(): #sets response when button clicked
            exit()

        btn = tk.Button(text="Exit", command=clicked,  fg='red') #builds button with attatched command
        btn.grid(row=0, column=7, sticky="NE")

        ###LHS BLOCK
        self.left=tk.Label(self, bg='#211C41')
        self.left.grid(row=1, column=0, rowspan=6, columnspan=1, sticky="NSWE")



        ###RHS BLOCK
        #15-£1,000,000\n14-£500,000\n13-£250,000\n12-£150,000\n11-£64,000\n10-£32,000\n9-£16,000\n8-£8,000\n7-£4,000\n6-£2,000\n5-£1,000\n4-£500\n3-£300\n2-£200\n1-£100
        self.right=tk.Label(self, bg='#211C41', fg='yellow', text='')
        self.right.grid(row=1, column=7, rowspan=3, columnspan=1, sticky="NSEW")
        self.filler= tk.Label(self.right, bg='#211C41', fg='yellow', text = '', pady = 20)
        self.filler.pack(fill=tk.BOTH, expand=False)
        self.fifteen = tk.Label(self.right, bg='#211C41', fg='yellow', text = '15 - £1,000,000', font=("Arial Black", 10))
        self.fifteen.pack(fill=tk.BOTH, expand=False)
        self.fourteen = tk.Label(self.right, bg='#211C41', fg='yellow', text = '14 - £500,000', font=("Arial Black", 10))
        self.fourteen.pack(fill=tk.BOTH, expand=False)
        self.thirteen = tk.Label(self.right, bg='#211C41', fg='yellow', text = '13 - £250,000', font=("Arial Black", 10))
        self.thirteen.pack(fill=tk.BOTH, expand=False)
        self.twelve = tk.Label(self.right, bg='#211C41', fg='yellow', text = '12 - £150,000', font=("Arial Black", 10))
        self.twelve.pack(fill=tk.BOTH, expand=False)
        self.eleven = tk.Label(self.right, bg='#211C41', fg='yellow', text = '11 - £64,000', font=("Arial Black", 10))
        self.eleven.pack(fill=tk.BOTH, expand=False)
        self.ten = tk.Label(self.right, bg='#211C41', fg='yellow', text = '10 - £32,000', font=("Arial Black", 10))
        self.ten.pack(fill=tk.BOTH, expand=False)
        self.nine = tk.Label(self.right, bg='#211C41', fg='yellow', text = '9 - £16,000', font=("Arial Black", 10))
        self.nine.pack(fill=tk.BOTH, expand=False)
        self.eight = tk.Label(self.right, bg='#211C41', fg='yellow', text = '8 - £8,000', font=("Arial Black", 10))
        self.eight.pack(fill=tk.BOTH, expand=False)
        self.seven = tk.Label(self.right, bg='#211C41', fg='yellow', text = '7 - £4,000', font=("Arial Black", 10))
        self.seven.pack(fill=tk.BOTH, expand=False)
        self.six = tk.Label(self.right, bg='#211C41', fg='yellow', text = '6 - £2,000', font=("Arial Black", 10))
        self.six.pack(fill=tk.BOTH, expand=False)
        self.five = tk.Label(self.right, bg='#211C41', fg='yellow', text = '5 - £1,000', font=("Arial Black", 10))
        self.five.pack(fill=tk.BOTH, expand=False)
        self.four = tk.Label(self.right, bg='#211C41', fg='yellow', text = '4 - £500', font=("Arial Black", 10))
        self.four.pack(fill=tk.BOTH, expand=False)
        self.three = tk.Label(self.right, bg='#211C41', fg='yellow', text = '3 - £300', font=("Arial Black", 10))
        self.three.pack(fill=tk.BOTH, expand=False)
        self.two = tk.Label(self.right, bg='#211C41', fg='yellow', text = '2  -£200', font=("Arial Black", 10))
        self.two.pack(fill=tk.BOTH, expand=False)
        self.one = tk.Label(self.right, bg='#211C41', fg='yellow', text = '1 - £100', font=("Arial Black", 10))
        self.one.pack(fill=tk.BOTH, expand=False)



        ###RBHS1 BLOCK
        self.RB=tk.Label(self, bg='#211C41')
        self.RB.grid(row=4, column=7, rowspan=3, columnspan=1, sticky="NSWE")

        ###RBHS2 BLOCK
        self.RB2=tk.Label(self, bg='black')
        self.RB2.grid(row=3, column=7, sticky="S")

        ##PRICE
        #self.pr_text1="CURRENT PRICE : £", self.cur_pr()

        #self.pr = tk.Label(self.RB2, text="", fg='white', bg='grey')
        #self.pr.pack(fill=tk.BOTH, expand=True)




        ### QUESITON AND ANSWER FRAME ###

        self.mid=tk.Frame(self, bg='red')
        self.mid.grid(row=1, column=1, rowspan=6, columnspan=6,  sticky="NSWE")

        ### QUESTION FRAME
        self.question=tk.Label(self, bg='#FFE396', fg="black", text="", wraplength = 400, justify = "center", font = ("Arial", 10))
        self.question.grid(row=1, column=1, rowspan=2, columnspan=6,  sticky="NSWE", padx=5, pady=5)
        mycursor.execute("SELECT question, correct_ans, inc1, inc2, inc3, inc4 FROM questions WHERE id = 1")
        myresultF = mycursor.fetchall()
        for row in myresultF:
            #array index number identifies date in the myresult tuple - which corresponds to the order in which they are selected in the mysql query
            qstr = row[0]
            ans_str = row[1]
            inc1_str = row[2]
            inc2_str = row[3]
            inc3_str = row[4]
            inc4_str = row[5]
            self.question["text"] = qstr



        ####### BTN CONTAINER ########

        def checkansTL():
            #look for the answer in the database
            #print (self.TL["text"])
            sql = "SELECT id FROM questions WHERE correct_ans = %s"
            TL_ans = (self.TL["text"],)
            mycursor.execute(sql, TL_ans)
            myresultTL = mycursor.fetchone()
            #print(myresultTL)
            # myresultTL = int(myresultTL)
            if myresultTL is not None :
                self.TL["text"] = "CORRECT"
            else:
                self.TL["text"] = "WRONG"
            #inactive the buttons to prevent multiple guesses
            self.TL["command"] = ''
            self.TR["command"] = ''
            self.BL["command"] = ''
            self.BR["command"] = ''



        def checkansTR():
            #look for the answer in the database
            #print (self.TR["text"])
            sql = "SELECT id FROM questions WHERE correct_ans = %s"
            TR_ans = (self.TR["text"],)
            mycursor.execute(sql, TR_ans)
            myresultTR = mycursor.fetchone()
            if myresultTR is not None :
                self.TR["text"] = "CORRECT"
            else:
                self.TR["text"] = "WRONG"
            #inactive the buttons to prevent multiple guesses
            self.TL["command"] = ''
            self.TR["command"] = ''
            self.BL["command"] = ''
            self.BR["command"] = ''

        def checkansBL():
            #look for the answer in the database
            #print (self.BL["text"])
            sql = "SELECT id FROM questions WHERE correct_ans = %s"
            BL_ans = (self.BL["text"],)
            mycursor.execute(sql, BL_ans)
            myresultBL = mycursor.fetchone()
            if myresultBL is not None :
                self.BL["text"] = "CORRECT"
            else:
                self.BL["text"] = "WRONG"
            #inactive the buttons to prevent multiple guesses
            self.TL["command"] = ''
            self.TR["command"] = ''
            self.BL["command"] = ''
            self.BR["command"] = ''

        def checkansBR():
            #look for the answer in the database
            #print (self.BR["text"])
            sql = "SELECT id FROM questions WHERE correct_ans = %s"
            BR_ans = (self.BR["text"],)
            mycursor.execute(sql, BR_ans)
            myresultBR = mycursor.fetchone()
            if myresultBR is not None :
                self.BR["text"] = "CORRECT"
            else:
                self.BR["text"] = "WRONG"
            #inactive the buttons to prevent multiple guesses
            self.TL["command"] = ''
            self.TR["command"] = ''
            self.BL["command"] = ''
            self.BR["command"] = ''

        ### ANSWER BUTTONS ###


        ###TOP ROW####

        self.button_container = tk.Frame(self)
        self.button_container.grid(row=3, column=1, columnspan=6, rowspan=1,   sticky="NSWE")
        ##TOP LEFT
        #ttk.button does not allow wraplength
        self.TL= tk.Button(self.button_container, text="", command=checkansTL, justify="center", wraplength = 100, font = ("Arial", 10), bg="white", fg="black", borderwidth="3", relief = "raised")
        self.TL.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=2, pady=2)
        ##TOP RIGHT
        self.TR = tk.Button(self.button_container,text="", command=checkansTR, justify="center", wraplength = 100, font = ("Arial", 10), bg="white", fg="black", borderwidth="3", relief = "raised")
        self.TR.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=2, pady=2)

        ###BOTTOM ROW####

        self.button_container = tk.Frame(self, height=5, width=5)
        self.button_container.grid( row=4, column=1, columnspan=6, rowspan=1,  sticky="NSWE")
        ##BOTTOM LEFT
        self.BL= tk.Button(self.button_container,text="", command=checkansBL, justify="center", wraplength = 100, font = ("Arial", 10), bg="white", fg="black", borderwidth="3", relief = "raised")
        self.BL.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=2, pady=2)
        ##BOTTOM RIGHT
        self.BR = tk.Button(self.button_container,text="", command=checkansBR, justify="center", wraplength = 100, font = ("Arial", 10), bg="white", fg="black", borderwidth="3", relief = "raised")
        self.BR.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=2, pady=2)

        #work out answers for question 1
        #assign buttons to varibles.
        var_buttonA = self.TL
        var_buttonB = self.TR
        var_buttonC = self.BL
        var_buttonD = self.BR
        #make a button list and randomly select one
        button_list = [var_buttonA, var_buttonB, var_buttonC, var_buttonD]
        correct_button = random.choice(button_list)
        #print(correct_button)
        #assign corret answer to the selected button
        correct_button["text"] = ans_str
        #remove selected button from button_list
        button_list.remove(correct_button)
        #print(button_list)
        # the list automatically re-sizes
        #make list of incorrect answers
        ans_list = [inc1_str, inc2_str, inc3_str, inc4_str]
        #print(ans_list)
        #randomly select 3 of these incorrect answers
        inc_ans_sel1 = random.choice(ans_list)
        #remove this from the ans_list
        ans_list.remove(inc_ans_sel1)
        #repeat for the next 2 incorrect answers
        inc_ans_sel2 = random.choice(ans_list)
        ans_list.remove(inc_ans_sel2)
        inc_ans_sel3 = random.choice(ans_list)
        #now assign these to the remaining 3 buttons
        button_list[0]["text"] = inc_ans_sel1
        button_list[1]["text"] = inc_ans_sel2
        button_list[2]["text"] = inc_ans_sel3

        #question counter
        self.qno = tk.Label(self.RB2, text="1", fg='white', bg='grey')
        self.qno.pack(fill=tk.BOTH, expand=True)
        #qvalue = int(self.qno["text"])

        self.correct = tk.Label(self.RB2, text="0", fg='white', bg='grey')
        self.correct.pack(fill=tk.BOTH, expand=True)


        def increase():
            #only advance if the user has selected an answer. Can check this because the answer text will have changed to WRONG or CORRECT
            qvalue = int(self.qno["text"])
            if qvalue > 14:
                self.fifteen["fg"] = "red"
                self.question["text"] = "CONGRATULATIONS!"
                self.question["bg"] = "green"
                self.question["fg"] = "red"
                self.question["font"] = ("Arial Black", 25)
                messagebox.showinfo("Finished", "You have attempted all the questions")
            if self.TL["text"] == "WRONG" or self.TL["text"] == "CORRECT" or self.TR["text"] == "WRONG" or self.TR["text"] == "CORRECT" or self.BR["text"] == "WRONG" or self.BR["text"] == "CORRECT" or self.BL["text"] == "WRONG" or self.BL["text"] == "CORRECT":
                # increase the number of correct answers if answer is correct
                if self.TL["text"] == "CORRECT" or  self.TR["text"] == "CORRECT" or self.BR["text"] == "CORRECT" or  self.BL["text"] == "CORRECT":
                    number_correct = int(self.correct["text"]) + 1
                    self.correct["text"] = number_correct
                number_correct = int(self.correct["text"])
                if number_correct == 1:
                    self.one["fg"] = "red"
                if number_correct == 2:
                    self.two["fg"] = "red"
                if number_correct == 3:
                    self.three["fg"] = "red"
                if number_correct == 4:
                    self.four["fg"] = "red"
                if number_correct == 5:
                    self.five["fg"] = "red"
                if number_correct == 6:
                    self.six["fg"] = "red"
                if number_correct == 7:
                    self.seven["fg"] = "red"
                if number_correct == 8:
                    self.eight["fg"] = "red"
                if number_correct == 9:
                    self.nine["fg"] = "red"
                if number_correct == 10:
                    self.ten["fg"] = "red"
                if number_correct == 11:
                    self.eleven["fg"] = "red"
                if number_correct == 12:
                    self.twelve["fg"] = "red"
                if number_correct == 13:
                    self.thirteen["fg"] = "red"
                if number_correct == 14:
                    self.fourteen["fg"] = "red"
                # if number_correct == 15:
                #     self.fifeen["fg"] = "red"
                #     self.question["text"] = "CONGRATULATIONS!"
                #     self.question["bg"] = "green"
                #     self.question["fg"] = "red"

                #increase the total number of questions attempted
                qvalue = int(self.qno["text"])
                self.qno["text"] = f"{qvalue + 1}"
                qvalue = f"{qvalue + 1}"
                mycursor.execute("SELECT question, correct_ans, inc1, inc2, inc3, inc4 FROM questions WHERE id = %s",[qvalue])
                myresultI = mycursor.fetchall()
                for row in myresultI:
                #qstr = str(row[0])
                    qstr = row[0]
                    ans_str = row[1]
                    inc1_str = row[2]
                    inc2_str = row[3]
                    inc3_str = row[4]
                    inc4_str = row[5]
                self.question["text"] = qstr
                button_list = [var_buttonA, var_buttonB, var_buttonC, var_buttonD]
                correct_button = random.choice(button_list)
                #print(correct_button)
                #assign corret answer to the selected button
                correct_button["text"] = ans_str
                #remove selected button from button_list
                button_list.remove(correct_button)
                #print(button_list)
                # the list automatically re-sizes
                #make list of incorrect answers
                ans_list = [inc1_str, inc2_str, inc3_str, inc4_str]
                #print(ans_list)
                #randomly select 3 of these incorrect answers
                inc_ans_sel1 = random.choice(ans_list)
                #remove this from the ans_list
                ans_list.remove(inc_ans_sel1)
                #repeat for the next 2 incorrect answers
                inc_ans_sel2 = random.choice(ans_list)
                ans_list.remove(inc_ans_sel2)
                inc_ans_sel3 = random.choice(ans_list)
                #now assign these to the remaining 3 buttons
                button_list[0]["text"] = inc_ans_sel1
                button_list[1]["text"] = inc_ans_sel2
                button_list[2]["text"] = inc_ans_sel3
                #reset colours on the answer buttons if changed by the 50-50 buttons
                self.TL["fg"] = "black"
                self.TL["bg"] = "white"
                self.TR["fg"] = "black"
                self.TR["bg"] = "white"
                self.BL["fg"] = "black"
                self.BL["bg"] = "white"
                self.BR["fg"] = "black"
                self.BR["bg"] = "white"
                #reset the button commands
                self.TL["command"] = checkansTL
                self.TR["command"] = checkansTR
                self.BL["command"] = checkansBL
                self.BR["command"] = checkansBR
            else:
                messagebox.showinfo("Next Question", "You must answer this question first!")


    #mycursor.execute("SELECT question FROM questions WHERE id = %s",[qvalue])
    #myresultI = mycursor.fetchone()
    #x = ''.join(myresultI)
    #x = x.upper()
    #self.question["text"] = x


        def decrease():
            qvalue = int(self.qno["text"])
            self.qno["text"] = f"{qvalue - 1}"
            qvalue = f"{qvalue - 1}"
            mycursor.execute("SELECT question, correct_ans, inc1, inc2, inc3, inc4 FROM questions WHERE id = %s",[qvalue])
            myresultD = mycursor.fetchall()
            for row in myresultD:
                #qstr = str(row[0])
                qstr = row[0]
                ans_str = row[1]
                inc1_str = row[2]
                inc2_str = row[3]
                inc3_str = row[4]
                inc4_str = row[5]
            self.question["text"] = qstr
            button_list = [var_buttonA, var_buttonB, var_buttonC, var_buttonD]
            correct_button = random.choice(button_list)
            #print(correct_button)
            #assign corret answer to the selected button
            correct_button["text"] = ans_str
            #remove selected button from button_list
            button_list.remove(correct_button)
            #print(button_list)
            # the list automatically re-sizes
            #make list of incorrect answers
            ans_list = [inc1_str, inc2_str, inc3_str, inc4_str]
            #print(ans_list)
            #randomly select 3 of these incorrect answers
            inc_ans_sel1 = random.choice(ans_list)
            #remove this from the ans_list
            ans_list.remove(inc_ans_sel1)
            #repeat for the next 2 incorrect answers
            inc_ans_sel2 = random.choice(ans_list)
            ans_list.remove(inc_ans_sel2)
            inc_ans_sel3 = random.choice(ans_list)
            #now assign these to the remaining 3 buttons
            button_list[0]["text"] = inc_ans_sel1
            button_list[1]["text"] = inc_ans_sel2
            button_list[2]["text"] = inc_ans_sel3
            #reset colours on the answer buttons if changed by the 50-50 buttons
            self.TL["fg"] = "black"
            self.TL["bg"] = "white"
            self.TR["fg"] = "black"
            self.TR["bg"] = "white"
            self.BL["fg"] = "black"
            self.BL["bg"] = "white"
            self.BR["fg"] = "black"
            self.BR["bg"] = "white"

        ##NEXT QUESTION
        self.NQ = tk.Button(self.RB, text="NEXT QUESTION", command=increase, fg='white', bg='#8CA2C4', highlightbackground='red')
        self.NQ.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.PQ = tk.Button(self.RB, text="PREVIOUS QUESTION", command=decrease, fg='white', bg='#8CA2C4', highlightbackground='red')
        self.PQ.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        def fif_fif():
            #first find the correct button using a loop through each button
            button_list = [var_buttonA, var_buttonB, var_buttonC, var_buttonD]
            for t in button_list:
                #check to see if this has the correct answer
                sql = "SELECT id FROM questions WHERE correct_ans = %s"
                ans = (t["text"],)
                mycursor.execute(sql, ans)
                myresultFF = mycursor.fetchone()
                # if the result is none, that means the ans is not found and so is incorrect
                if myresultFF is not None :
                    corr_button = t
                    break
            #print(corr_button)
            #remove correct button from button_list
            button_list.remove(corr_button)
            #now grey out 2 of these buttons by random choice
            grey_button1 = random.choice(button_list)
            #remove selected button from button_list
            grey_button1["fg"] = "#b3b3cc"
            grey_button1["bg"] = "#b3b3cc"
            button_list.remove(grey_button1)
            grey_button2 = random.choice(button_list)
            #remove selected button from button_list
            grey_button2["fg"] = "#b3b3cc"
            grey_button2["bg"] = "#b3b3cc"
            #inactive button so it can only be used once
            self.fif["command"] = ''
            self.fif["fg"] = 'black'
            self.fif["bg"] = '#dde4ee'
            self.fif["text"] = "50-50 used!"

        ##5050
        self.fif = tk.Button(self.left, text="50-50", font=("Verdana", 12), command=fif_fif, fg='white', bg='#8CA2C4', highlightbackground='red')
        self.fif.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        def phone():
            #make friend list
            friends = ["PLUMMER", "ELECTRICIAN", "DOCTOR", "TEACHER", "ENGINEER", "SCHOOL FRIEND"]
            #pick a random friend
            var_friend = random.choice(friends)
            # sort out the grammer - a or an
            if var_friend == "ELECTRICIAN" or var_friend == "ENGINEER":
                var_a = "an "
            else:
                var_a = "a "

            #check the database to see of this friend is an expert for this question
            sql = "SELECT friend, correct_ans FROM questions WHERE question = %s"
            question = (self.question["text"],)
            mycursor.execute(sql, question)
            myresultPF = mycursor.fetchall()
            for row in myresultPF:
                expert = row[0]
                correct_answer = row[1]
            #if the var_friend is the same as the expert, then the there is an 80% chance of the friend being correct.  Otherwise there is a 25% chance
            #get the possible answers from those that are displayed
            ans_one = self.TL["text"]
            ans_two = self.TR["text"]
            ans_three = self.BL["text"]
            ans_four = self.BR["text"]
            #make a list of the answers
            answers = [ans_one, ans_two, ans_three, ans_four]
            #pick one at random
            twentyfive_percent = random.choice(answers)
            #remove the correct answer
            answers.remove(correct_answer)
            #select random incorrect answer
            random_inc = random.choice(answers)
            eighty_percent = [correct_answer, correct_answer, correct_answer, correct_answer, correct_answer, correct_answer, correct_answer, correct_answer, random_inc, random_inc]
            if var_friend == expert:
                var_answer = random.choice(eighty_percent)
            else:
                var_answer = twentyfive_percent
            var_answer = var_answer.upper()
            var_message = "You phoned " + var_a + var_friend + ". Do you trust their judgement?" " Their best guess is " + var_answer +". Good luck!"
            messagebox.showinfo("Phone A Friend", var_message)

            #inactive button so it can only be used once
            self.phon["command"] = ''
            self.phon["fg"] = 'black'
            self.phon["bg"] = '#dde4ee'
            self.phon["text"] = "PHONE A FRIEND used!"





        ##PHONE FRIEND
        self.phon = tk.Button(self.left, text="PHONE A FRIEND", font=("Verdana", 12), command=phone, fg='white', bg='#8CA2C4', highlightbackground='red')
        self.phon.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)


        # give a weight to the grid elements, allowing resizing
        for row, weight in zip(range(5), [1, 1, 1, 1, 1, 1, 1, 1]):
            Grid.rowconfigure(self, row, weight=weight)
        for y in range(self.grid_size()[0]):
            Grid.columnconfigure(self, y, weight=1)




        #ITERATIVE LABEL CREATION IDEA
        # self.collumns=[]
        # self.col=['red', 'green', 'white']
        # for i,color in enumerate(self.col):
        #   self.collumns.append(tk.Label(self.content, bg=color))


if __name__ == '__main__':
    app = main()

    app.mainloop()
