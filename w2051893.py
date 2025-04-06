
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:W2051893
# Date:14/12/2023

#part 1
#importing graphics
from graphics import *

#A
progress,exclude,module_trailer,module_retriever = 0,0,0,0
list_1 = []
list_2 = []

def taking_inputs():
    global pass_mark,defer_mark,fail_mark
    pass_mark = int(input('Please enter your credits at pass: '))
    defer_mark = int(input('Please enter your credit at defer: '))
    fail_mark = int(input('Please enter your credit at fail: '))

#b
def prediction(passing_grade,failing_grade):
    global progress,module_trailer,exclude,module_retriever,string_hold
    if passing_grade == 120:
        print('Progress')
        progress += 1
        string_hold = 'Progress - '
    elif passing_grade == 100:
        print('Progress (module trailer)')
        module_trailer += 1
        string_hold = 'Progress (module trailer) - '
    elif (passing_grade == 40 or passing_grade == 20 or passing_grade == 0) and (failing_grade == 120 or failing_grade == 100 or failing_grade == 80):
        print('Exclude')
        exclude += 1
        string_hold = 'Exclude - '
    else:
        print('Do not progress - module retriever')
        module_retriever += 1
        string_hold = 'Do not progress - module retriever - '


def validation_range(temporary_1,temporary_2,temporary_3):
    if temporary_1 not in [0,20,40,60,80,100,120] or temporary_2 not in [0,20,40,60,80,100,120] or temporary_3 not in [0,20,40,60,80,100,120]:
        print('Out of range')

def validation_total(a,b,c):
    if a + b + c != 120:
        print('Total incorrect')

#histogram
def histogram():
    global outcomes
    outcomes = progress + module_retriever + module_trailer + exclude
    window = GraphWin('Histogram',1000,700)
    rect1 = Rectangle(Point(40,600 - progress*5),Point(240,600))
    rect2 = Rectangle(Point(280,600 - module_trailer*5),Point(480,600))
    rect3 = Rectangle(Point(520,600 - module_retriever*5),Point(720,600))
    rect4 = Rectangle(Point(760,600 - exclude*5),Point(960,600))
    text1 = Text(Point(140,640),'Progress')
    text2 = Text(Point(380,640),'Trailer')
    text3 = Text(Point(620,640),'Retrieve')
    text4 = Text(Point(860,640),'Exclude')
    text5 = Text(Point(75,50),"Histogram Results")
    text6 = Text(Point(50,680),outcomes)
    text7 = Text(Point(125,680),'outcomes in  total')
    rect1.setFill(color_rgb (60, 179, 113))
    rect2.setFill(color_rgb(0,0,255))
    rect3.setFill(color_rgb(255,0,0))
    window.setBackground('white')
    rect4.setFill(color_rgb(170,0,255))
    text8 = Text(Point(140,580-progress*5),progress)
    text9 = Text(Point(380,580-module_trailer*5),module_trailer)
    text10 = Text(Point(620,580-module_retriever*5),module_retriever)
    text11 = Text(Point(860,580-exclude*5),exclude)
    line = Line(Point(0,600),Point(1000,600))
    [test.draw(window) for test in [rect1,rect2,rect3,rect4,text1,text2,text3,text4,text5,text6,text7,line,text8,text9,text10,text11]]
    window.getMouse()
    window.close()

#C
loop_or_quit = 'y'

while True:
    who_is_using = input('Are you a student or a staff member: ')
    who_is_using = who_is_using.lower()
    if who_is_using == 'student':
        try:
            taking_inputs()
            validation_range(pass_mark,defer_mark,fail_mark)
            validation_total(pass_mark,defer_mark,fail_mark)
            prediction(pass_mark,fail_mark)
            progress,exclude,module_retriever,module_trailer = 0,0,0,0
        except ValueError:
            print('Integer required!')
    elif who_is_using == 'staff': 
        while loop_or_quit == 'y':
            try:
                taking_inputs()
                validation_range(pass_mark,defer_mark,fail_mark)
                validation_total(pass_mark,defer_mark,fail_mark)
                prediction(pass_mark,fail_mark)
                loop_or_quit = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
                loop_or_quit = loop_or_quit.lower()
                list_1.append(string_hold)
                list_1.append(pass_mark)
                list_1.append(defer_mark)
                list_1.append(fail_mark)
                list_2.append(list_1)
                list_1 = []
            except ValueError:
                print('Integer required')
        else:
            if loop_or_quit == 'q':
                histogram()
                for i in range(len(list_2)):
                        print(str(list_2[i][0]) + str(list_2[i][1]) + ' , ' + str(list_2[i][2]) + ' , ' + str(list_2[i][3]) + '\n')

                write_in_file = open('Text.txt','a+')
                for k in range (len(list_2)):
                    write_in_file.write(str(list_2[k][0]) + str(list_2[k][1]) + ' , ' + str(list_2[k][2]) + ' , ' + str(list_2[k][3]) + '\n')
                write_in_file.close()

                read_file = open('Text.txt','r')
                read = read_file.read()
                print(read)
                read_file.close()
                
            else:
                print('Wrong input entered!')
    else:
        print('Wrong input entered!')
