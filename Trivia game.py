import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import winsound
import webbrowser
from tkinter import *
import webbrowser



#show true false frame
def showTF1():
    TFframe1.place_forget
    registrationFrame.place_forget()
    TFframe1.place(x = 0, y = 0)
    

    
    
    setupTF1()    
#add widgets to registration frame
def setupRegistrationFrame():
    logo = tk.PhotoImage(file="Registration Background.png")
    
    # Create labels for the frame
    appLabel1 = ttk.Label(registrationFrame, image = logo, anchor = 'center')
    appLabel1.place(x=0, y=0, width = 1000, height = 600)
    appLabel1.logo = logo

    titleLabel = ttk.Label(registrationFrame, text = 'NFL trivia game',background="blue",font=("Courier", 30), anchor = 'center')
    titleLabel.place(x=300, y=30, width = 500, height = 60)

    usernameLabel = ttk.Label(registrationFrame, text = 'Username',anchor = 'w')
    usernameLabel.place(x=280, y=190, width = 100, height = 25)
   

    usernameEntry = ttk.Entry(registrationFrame, textvariable = username, justify = 'left')
    usernameEntry.place(x = 400, y = 190, width = 200, height = 25)

    easyRadiobutton = ttk.Radiobutton(registrationFrame, text = 'Easy', variable = difficulty, value = 1)
    easyRadiobutton.place(x = 250, y = 250, width = 150, height = 25)

    mediumRadiobutton = ttk.Radiobutton(registrationFrame, text = 'Medium', variable = difficulty, value = 2)
    mediumRadiobutton.place(x = 400, y = 250, width = 150, height = 25)

    hardRadiobutton = ttk.Radiobutton(registrationFrame, text = 'Hard', variable = difficulty, value = 3)
    hardRadiobutton.place(x = 550, y = 250, width = 150, height = 25)

    
    x = '''Would you like to test your knowledge of the NFL?
If the answer to that question is yes then this is the quiz for you.
This quiz will have 5 true false questions and 5 multiple choice questions.
If you choose easy you will have 0 challenge questions.
If you chose medium you will have 1 challenge question,
If you chose hard you will have 3 challenge questions.
Your score will be shown in the end.Good luck!

Rules
1.After you chose the answer you think is correct, click next
2.Each normal question answered correctly will give you 100 points
3.For each normal question you got wrong you will lose 100 point
4.Each challenge question answered correctly will give you 300 points
5.For each challenge question you got wrong you will lose 300 point
'''
    usernameLabel = ttk.Label(registrationFrame, text = x,background = 'sky blue',anchor = 'w')
    usernameLabel.place(x=220, y=280, width = 400, height = 250)        

    nextButton = ttk.Button(registrationFrame, text = "Next", command = showTF1)
    nextButton.place(x = 740, y = 480, width = 100, height = 50)


         

#set up true false frame    
def setupTF1():
    #all the variables I will need
    global scores
    global TFscore
    global correctAnswers
    global x
    global TFquestionsAvailable
    global picList

    #users currest aswer
    ans = int(TF1ans.get())

    #Backhround igame
    logo = tk.PhotoImage(file="TF1.gif")
    appLabel1 = ttk.Label(TFframe1, image = logo, anchor = 'center')
    appLabel1.place(x=0, y=0, width = 1000, height = 600)
    appLabel1.logo = logo

    #cycle through images
    chosenpic = random.choice(picList)
    pic = tk.PhotoImage(file=chosenpic)
    picLabel = ttk.Label(TFframe1, image = pic, anchor = 'center')
    picLabel.place(x=400, y=100, width = 250, height = 250)
    picLabel.logo = pic

    #Mark questions and assign score
    if ans == 1 or ans == 2:
        if ans == correctAnswers[x]:
            TFscore += 100

        else:
            TFscore -= 100
        
    #make sure questions are not repeated
    x = random.choice(TFquestionsAvailable)
    TFquestionsAvailable.remove(x)
    


        

    
    #labels, butons and radio buttons
    questionLabel = ttk.Label(TFframe1,font=("Courier", 14), text = TFQuestions[x],background = 'purple',anchor = 'w')
    questionLabel.place(x=180, y=400, width = 650, height = 50)

    trueRadiobutton = ttk.Radiobutton(TFframe1, text = 'True', variable = TF1ans, value = 1)
    trueRadiobutton.place(x = 190, y = 545, width = 150, height = 25)

    falseRadiobutton = ttk.Radiobutton(TFframe1, text = 'False', variable = TF1ans, value = 2)
    falseRadiobutton.place(x = 575, y = 545, width = 150, height = 25)

    nextButton = ttk.Button(TFframe1, text = "Next", command = setupTF1)
    nextButton.place(x = 850, y = 480, width = 100, height = 50)

    #if on 5th tf 5 question change command of button
    if len(TFquestionsAvailable) == 5:
        
        nextButton.place_forget()
        
        McButton = ttk.Button(TFframe1, text = "Next", command = showMcFrame)
        McButton.place(x = 850, y = 480, width = 100, height = 50)
        
        


    
#Create widgets I need for multiple choice frame
#MC stands for Multiple choice
def setUpMCFrame():
    #variables I will need
    global MCQuestions
    global userInputMC
    global answersMC
    global scores
    global MCscore
    global xNum
    global picList



    userInputMC = []
    
    MCQuestionsused = []
    
    
    userInputMC.append(McAns.get())
        
    
    #reference of list of questions used to find index
    reference = ['Who is the passing touchdown career leader?',
              'The weight of a football is approximately (answer) pounds?',
              'What is the length of an nfl football field in yards ?',
              'Who is the QB with most superbowl wins ?',
              'Who is the nfl career receiving yards leader ?',
              'The most touchdowns in a season by a QB is?',
              'The team with best win percentage over the last 20 years is?',
              'Who is the oldest person to win an MVP?',
              'How many WR have won MVP?',' Who is the player that won the most MVPs?',]



    #this part choses random question
    x = random.choice(MCQuestions)


    
   

    
    
    
    #Check if user got answer right or wrong and update score
    if McAns.get()>0:
        if McAns.get() == answersMC[xNum]:
            
            MCscore += 100
        else:
            
            MCscore -=100
    #this part finds index of the question
    xNum = reference.index(x)
    MCQuestions.remove(x)
    
    #Labels, buttons , and radiobuttons for the frame
    logo = tk.PhotoImage(file="MC.gif")
    MCFrameBackgroundLabel1 = ttk.Label(McFrame, image = logo, anchor = 'center')
    MCFrameBackgroundLabel1.place(x=0, y=0, width = 1000, height = 600)
    MCFrameBackgroundLabel1.logo = logo

    #cycle through pictures
    chosenpic = random.choice(picList)
    pic = tk.PhotoImage(file=chosenpic)
    picLabel = ttk.Label(McFrame, image = pic, anchor = 'center')
    picLabel.place(x=400, y=70, width = 250, height = 250)
    picLabel.logo = pic


    questionLabel = ttk.Label(McFrame,font=("Courier", 14), text = x,background = 'purple',anchor = 'w')
    questionLabel.place(x=180, y=340, width = 650, height = 40)

    optionARadiobutton = ttk.Radiobutton(McFrame, text = OptionA[xNum], variable = McAns, value = 1)
    optionARadiobutton.place(x = 230, y = 450, width = 150, height = 25)

    optionBRadiobutton = ttk.Radiobutton(McFrame, text = OptionB[xNum], variable = McAns, value = 2)
    optionBRadiobutton.place(x = 600, y = 450, width = 150, height = 25)

    optionCRadiobutton = ttk.Radiobutton(McFrame, text = OptionC[xNum], variable = McAns, value = 3)
    optionCRadiobutton.place(x = 230, y = 530, width = 150, height = 25)

    optionDRadiobutton = ttk.Radiobutton(McFrame, text = OptionD[xNum], variable = McAns, value = 4)
    optionDRadiobutton.place(x = 600, y = 530, width = 150, height = 25)
    
    nextButton = ttk.Button(McFrame, text = "Next", command = setUpMCFrame)
    nextButton.place(x = 850, y = 480, width = 100, height = 50)

    MCQuestionsused.append(xNum)

    



    
    # if on 5th question change command of button
    if len(MCQuestions)==5:
        nextButton.place_forget()

        
        challengeButton = ttk.Button(McFrame, text = "Next", command = showchallengeFrame)
        challengeButton.place(x = 850, y = 480, width = 100, height = 50)
        

#shows Multiple choice frame        
def showMcFrame():
    #place multiple choice frame
    McFrame.place(x = 0, y = 0)
    TFframe1.place_forget()
    global answers
    global correctAnswers
    global TFscore
    global scores

    #mark last true false question
    if TF1ans.get() == 1 or TF1ans.get() == 2:
        if TF1ans.get() == correctAnswers[x]:
            TFscore += 100

        else:
            TFscore -= 100
    answers.append(TF1ans.get())

    #update score
    scores = TFscore + scores
        

    setUpMCFrame()
#show challenge frame
def showchallengeFrame():
    global scores
    global MCscore
    global xNum
    #place challenge frame
    McFrame.place_forget()        
    challengeFrame.place(x = 0, y = 0)
    #mark last multiple choice question
    if McAns.get() == answersMC[xNum]:       
        
        MCscore += 100
    else:
        
        MCscore -=100
    print(MCscore)

    #update score
    scores += MCscore
    
    setupChallengeFrame()

def setupChallengeFrame():

    global challengQuestions
    global challengeOptionA
    global challengeOptionB
    global challengeOptionC
    global challengeOptionD
    global challengeAnswers
    global questionsAvailable
    global cscore
    global r
    global count
    global scores

    #mark users answer
    if challengeAns.get() >0:
        
        if challengeAns.get() == challengeAnswers[r]:
            cscore += 300
        else:
            cscore -=300
        
    #chose random number from 0-9, then remove that number from list
    #this is to make sure questions are not repeated
    r = random.choice(questionsAvailable)
    questionsAvailable.remove(r)

    #labels,buttons, and radio buttons for frame
    logo = tk.PhotoImage(file="challengeRound.png")
    challenegeFrameBackgroundLabel1 = ttk.Label(challengeFrame, image = logo, anchor = 'center')
    challenegeFrameBackgroundLabel1.place(x=0, y=0, width = 1000, height = 600)
    challenegeFrameBackgroundLabel1.logo = logo

    titleLabel = ttk.Label(challengeFrame,font=("Courier", 16), text = 'Challenge round!',background = 'white',anchor = 'w')
    titleLabel.place(x=260, y=50, width = 550, height = 40)

    questionLabel = ttk.Label(challengeFrame,font=("Courier", 13), text = challengQuestions[r],background = 'purple',anchor = 'w')
    questionLabel.place(x=260, y=130, width = 550, height = 40)

    optionARadiobutton = ttk.Radiobutton(challengeFrame, text = challengeOptionA[r], variable = challengeAns, value = 1)
    optionARadiobutton.place(x = 110, y = 335, width = 150, height = 25)

    optionBRadiobutton = ttk.Radiobutton(challengeFrame, text = challengeOptionB[r], variable = challengeAns, value = 2)
    optionBRadiobutton.place(x = 540, y = 335, width = 150, height = 25)

    optionCRadiobutton = ttk.Radiobutton(challengeFrame, text = challengeOptionC[r], variable = challengeAns, value = 3)
    optionCRadiobutton.place(x = 110, y = 450, width = 150, height = 25)

    optionDRadiobutton = ttk.Radiobutton(challengeFrame, text = challengeOptionD[r], variable = challengeAns, value = 4)
    optionDRadiobutton.place(x = 540, y = 450, width = 150, height = 25)
    
    nextButton = ttk.Button(challengeFrame, text = "Next", command = setupChallengeFrame)
    nextButton.place(x = 780, y = 520, width = 100, height = 50)

    
    #change amount of questions based around difficulty
    if count == 2:
        nextButton.place_forget()
        resultsButton = ttk.Button(challengeFrame, text = "results", command = showresultsFrame)
        resultsButton.place(x = 780, y = 520, width = 100, height = 50)
        
    
    count +=1

    if difficulty.get() == 1:
        challengeFrame.place_forget()
        setupresultsFrame()
        resultsFrame.place(x = 0, y = 0)


            
    elif difficulty.get() == 2:
        nextButton.place_forget()
        
        resultsButton = ttk.Button(challengeFrame, text = "Results", command = showresultsFrame)
        resultsButton.place(x = 780, y = 520, width = 100, height = 50)



def showresultsFrame():
    global r
    global cscore
    global scores
    #place results frame
    resultsFrame.place(x = 0, y = 0)
    challengeFrame.place_forget()
    ##mark last challenge question
    if challengeAns.get() >0:
        
        if challengeAns.get() == challengeAnswers[r]:
            cscore += 300
        else:
            cscore -=300

        
        scores = scores + cscore
        setupresultsFrame()
        
def setupresultsFrame():

    global scores
    global TFscore
    global MCscore
    global cscore

    #labels buttons and radio buttons for results frame

    logo = tk.PhotoImage(file="resultsBackground.png")
    challenegeFrameBackgroundLabel1 = ttk.Label(resultsFrame, image = logo, anchor = 'center')
    challenegeFrameBackgroundLabel1.place(x=0, y=0, width = 1000, height = 600)
    challenegeFrameBackgroundLabel1.logo = logo
    
    titleLabel = ttk.Label(resultsFrame,font=("Courier", 20), text = 'results',background = 'white',anchor = 'w')
    titleLabel.place(x=260, y=10, width = 200, height = 70)

    name = str(username.get())

    #scoring breakdown
    yourScore = ''+name+'s total score is '+str(scores)
    yourTFscore = 'True false: '+str(TFscore)
    yourMCscore = 'Multiple Choice: '+str(MCscore)
    yourcscore = 'Challenge Round: '+str(cscore)
    
    scoreLabel = ttk.Label(resultsFrame,font=("Courier", 14), text = yourScore,background = 'white',anchor = 'w')
    scoreLabel.place(x=260, y=150, width = 550, height = 40)

   

    scoreBreakdownLabel = ttk.Label(resultsFrame,font=("Courier", 14), text = 'Scoring breakdown',background = 'white',anchor = 'w')
    scoreBreakdownLabel.place(x=50, y=200, width = 300, height = 40)

    yourTFscoreLabel = ttk.Label(resultsFrame,font=("Courier", 14), text = yourTFscore,background = 'white',anchor = 'w')
    yourTFscoreLabel.place(x=50, y=250, width = 300, height = 40)

    yourMCscoreLabel  = ttk.Label(resultsFrame,font=("Courier", 14), text = yourMCscore,background = 'white',anchor = 'w')
    yourMCscoreLabel.place(x=50, y=300, width = 300, height = 40)

    yourcscoreLabel  = ttk.Label(resultsFrame,font=("Courier", 14), text = yourcscore,background = 'white',anchor = 'w')
    yourcscoreLabel.place(x=50, y=350, width = 300, height = 40)

    rankingTitleLabel  = ttk.Label(resultsFrame,font=("Courier", 14), text = 'Rankings',background = 'white',anchor = 'w')
    rankingTitleLabel.place(x=750, y=180, width = 300, height = 40)


    #Output user rankings

    rank = ''
    George = 'George'
    Bobby = 'Bobby'
    Jeff = 'Jeff'
    Jeb = 'Jeb'
    Holly = 'Holly'
    Mitch = 'Mitch'
    Tom = 'Tom'
    Bill = 'Bill'
    Joe = 'Joe'
    Bob = 'Bob'



    #find users rank
    if scores >= 1000:
        rank = '1st'
        George = str(username.get()) +': '+ str (scores)+ '             '
    elif scores >= 900:
        rank = '2nd'
        Bobby = str(username.get()) +': '+ str (scores)+ '             '
    elif scores >= 800:
        rank = '3rd'
        Jeff = str(username.get()) +': '+ str (scores)+ '             '
    elif scores >= 700:
        rank = '4th'
        Jeb = str(username.get()) +': '+ str (scores)+ '            '
    elif scores >= 600:
        rank = '5th'
        Holly = str(username.get()) +': '+ str (scores)+ '             '
    elif scores >= 500:
        rank = '6th'
        Mitch = str(username.get()) +': '+ str (scores)+ '            '
    elif scores >= 400:
        rank = '7th'
        Tom = str(username.get()) +': '+ str (scores)+ '             '
    elif scores >= 300:
        rank = '8th'
        Bill = str(username.get()) +': '+ str (scores)+ '             '
    elif scores >= -200:
        rank = '9th'
        Joe = str(username.get()) +': '+ str (scores)+ '              '
    elif scores >= -300:
        rank = '10th'
        Bob = str(username.get()) +': '+ str (scores)+ '              '
    else:
        rank = 'Last'
        Bob = str(username.get()) +': '+ str (scores)+ '              '

    yourRank = 'You rank '+rank
    
    rankings = '1.'+George+': 1000\n2.'+Bobby+' : 900\n3.'+Jeff+'  : 800\n4.'+Jeb+'   : 700\n5.'+Holly+' : 600\n6.'+Mitch+' : 500\n7.'+Tom+'   : 400\n8.'+Bill+'  : 300\n9.'+Joe+'   : -200\n10.'+Bob+'  : -300\n'

    yourRankLabel  = ttk.Label(resultsFrame,text = yourRank,font=("Courier", 14),background = 'white',anchor = 'w')
    yourRankLabel.place(x=750, y=500, width = 150, height = 50)

    rankingTitleLabel  = ttk.Label(resultsFrame,text = rankings,background = 'white',anchor = 'w')
    rankingTitleLabel.place(x=750, y=250, width = 100, height = 200)

    photo = ''
    #play sounds based on how well they did
    if scores > 200:
        winsound.PlaySound('yay.wav',winsound.SND_ASYNC)


    else:
        winsound.PlaySound('sadViolin.wav',winsound.SND_ASYNC)



    
    quitButton = ttk.Button(resultsFrame, text = "Quit", command = quitProgram)
    quitButton.place(x = 200, y = 500, width = 100, height = 50)

    rewardButton = ttk.Button(resultsFrame, text = "Reward", command = openweb)
    rewardButton.place(x = 500, y = 500, width = 100, height = 50)

    playAgainLabel = ttk.Label(resultsFrame, text = 'play again to earn different reward',background = 'white',anchor = 'w')
    playAgainLabel.place(x=450, y=550, width = 200, height = 30)
    #Exit window
def quitProgram():

    window.destroy()

#play youtube video
#Randomly choose youtube video
videos = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ','https://www.youtube.com/watch?v=IaLLKXy_iP0','https://www.youtube.com/watch?v=Fv-QmBtOtd8']
new = 1
randvid = random.randrange(0,3)
url = videos[randvid]



def openweb():
    webbrowser.open(url,new=new)

#Pictures
picList = ['q1.png','q2.png','q3.png','q4.png','q5.png','q6.png','q7.png',]
#All true false Questions

TFQuestions = ['The finals in the NFL is called the superbowl',
               'The NFL stands for no fun league',
               'The Carolina Panthers were not part of the original nfl',
               'The Cleveland Browns won The Superbowl in 2015',
               'A touchdown is worth 6 points',
               'Aaron Donald has 1 MVP',
               'The Chiefs are in the nfc south',
               'The main job of the cornerback is to throw the ball',
               'The nfl is currently in a “bubble”',
               'Lamar Jackson won the mvp in 2019']

#all Multiple choice question
TFQuestionsUsed = []

MCQuestions = ['Who is the passing touchdown career leader?',
              'The weight of a football is approximately (answer) pounds?',
              'What is the length of an nfl football field in yards ?',
              'Who is the QB with most superbowl wins ?',
              'Who is the nfl career receiving yards leader ?',
              'The most touchdowns in a season by a QB is?',
              'The team with best win percentage over the last 20 years is?',
              'Who is the oldest person to win an MVP?',
              'How many WR have won MVP?',' Who is the player that won the most MVPs?',]
#options for multiple choice questions
OptionA = ['Bret Farve','3','200','Aaron Rodgers','Terrel Owens','50','Packers','Jerry Rice','3','Tom Brady']
OptionB = ['Joe Montana','2','100','Joe Montana','N’keal Harry','55','Steelers','Joe Montana','2','Aaron Rodgers']
OptionC = ['Tom Brady','1','250','Tom Brady','Jerry Rice','65','Patriots','Lawrence Taylor','4','Payton Manning']
OptionD = ['Drew Brees','4','150','Bret Farve','Randy Moss','60','Browns','Tom Brady','0','Eli Manning']



window = tk.Tk('')

#Global Variable for registration
username = tk.StringVar()
difficulty = tk.IntVar()

#Global variable for TF1
TF1ans = tk.IntVar()
scores = 0
TFscore = 0
answers = []
correctAnswers = [1,2,1,2,1,2,2,2,2,1]
x = 0
TFquestionsAvailable = [0,1,2,3,4,5,6,7,8,9]
#Global variables for Multiple choice page
McAns = tk.IntVar()
userInputMC = []
answersMC = [3,3,2,3,3,2,3,4,4,3]
MCscore = 0
xNum = 0

#global variable for Challenge frame
challengeAns = tk.IntVar()
challengQuestions = ['When was the NFL founded?',
                     'Who is the nfl commisioner?',
                     'WHo is the QB for the new york jets? ',
                     'Who is the Current receiving Yard Leader?',
                     'At what position was Tom Brady Drafted?',
                     'Where were the Raiders were originally from? ',
                     'How many nfl teams are named after birds?',
                     'How many super bowls have gone to overtime?',
                     'Where is the football hall of fame located?',
                     'What team went to 4 straight superbowls without winning?',]

challengeOptionA = ['1890','Rodger Godel','Teddy Bridgewater','Tyreek Hill','1','New York','3','1','New York','Patriots']
challengeOptionB = ['1950','Elon Musk','Sam Darnold','DK Metcalf','2','Chicago','4','2','Ohio','Steelers']
challengeOptionC = ['1942','Edward Smith','Dion Sanders','Stefon Diggs','5','Scranton','5','3','Michigan','Browns']
challengeOptionD = ['1920','Julius Verena','Trevor Lawrence','Randy Moss','199','Oakland','6','0','Texas','Bills']

challengeAnswers = [4,1,2,3,4,4,3,1,2,4]

questionsAvailable = [0,1,2,3,4,5,6,7,8,9]

#cscore stands for challenge score    
cscore = 0
#r will later be used as a random number to pick question
r = 0
#count used to tell what question you are on
count = 0

# Setup the window

frameWidth = 1000
frameHeight = 600
window.minsize(frameWidth, frameHeight)

#set up all frames
#forget all frames ecept the first one
registrationFrame=ttk.Frame(window, width = frameWidth, height = frameHeight)
registrationFrame.place(x = 0, y = 0)

TFframe1=ttk.Frame(window, width = frameWidth, height = frameHeight)
registrationFrame.place(x = 0, y = 0)
TFframe1.place_forget

McFrame=ttk.Frame(window, width = frameWidth, height = frameHeight)

McFrame.place_forget

challengeFrame=ttk.Frame(window, width = frameWidth, height = frameHeight)

resultsFrame=ttk.Frame(window, width = frameWidth, height = frameHeight)
resultsFrame.place(x = 0, y = 0)
resultsFrame.place_forget()


#set up first frame
setupRegistrationFrame()


