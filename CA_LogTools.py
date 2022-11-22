import PySimpleGUIQt as sg

# [2022-11-15 15:57:51]
def timeConstructer(timePoint):
    lol = ""
    timePointList = list((timePoint))
    year = timePointList[1:5]
    month = timePointList[6:8]
    day = timePointList[9:11]
    hour = timePointList[12:14]
    minute = timePointList[15:17]
    second = timePointList[18:20]
    return int(f"{lol.join(year)}{lol.join(month)}{lol.join(day)}{lol.join(hour)}{lol.join(minute)}{lol.join(second)}")

def checkForTime(timePointA, timePointB, timePointCheck):
    if timePointA < timePointCheck < timePointB:
        return True
    else:
        return False

def searchBetweenTime(timePointA, timePointB, log, out):
    x = ""
    for line in log:
        time = x.join(line[0:21])
        time = timeConstructer(time)
        if checkForTime(timePointA, timePointB, time):
            out.write(line)

#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text("Craft Attack search tool by Looter V.2.1")],
            [sg.Text("Logfile:"), sg.Input(), sg.FileBrowse()],
            [sg.Text("Output file"), sg.Input("out.txt"), sg.FileBrowse()],
            [sg.Text("Enter the players name"), sg.InputText()],
            [sg.Text("Coordinates")],
            [sg.Text("X:"), sg.InputText(), sg.Text("Y:"), sg.InputText(), sg.Text("Z:"), sg.InputText()],
            [sg.Text("First Point in Time")],

            [sg.Text("Year:"), sg.InputText(size_px=[60,20], key="Year1"), sg.Text("Month:"), sg.InputText(size_px=[40, 20], key="Month1"),
             sg.Text("Day:"), sg.InputText(size_px=[40, 20], key="Day1"), sg.Text("Hour:"), sg.InputText(size_px=[40, 20], key="Hour1"),
             sg.Text("Minute:"), sg.InputText(size_px=[40, 20], key= "Minute1"), sg.Text("Second:"), sg.InputText(size_px=[40, 20], key="Second1")],

            [sg.Text("Second Point in Time")],
            [sg.Text("Year:"), sg.InputText(size_px=[60, 20], key="Year2"), sg.Text("Month:"), sg.InputText(size_px=[40, 20], key="Month2"),
             sg.Text("Day:"), sg.InputText(size_px=[40, 20], key="Day2"), sg.Text("Hour:"), sg.InputText(size_px=[40, 20], key="Hour2"),
             sg.Text("Minute:"), sg.InputText(size_px=[40, 20], key="Minute2"), sg.Text("Second:"), sg.InputText(size_px=[40, 20], key="Second2")],

            [sg.Text("Select, what you want to search for")],
            #[sg.Button("Coordinates"), sg.Button("Player name"), sg.Button("Time")],
            [sg.Checkbox("Playername", key="-usePlayerName-"), sg.Checkbox("Use cords", key="-useCords-"), sg.Checkbox("Use time", key="-useTime-")],
            [sg.Checkbox("Should stay open (can cause bugs)", key="-stayOpen-")],
            [sg.Button("Submit"), sg.Button("Cancel")]
            ]

# Create the Window
window = sg.Window('CraftAttack log searching tool ', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Submit":
        TimeA = ["Year1", "Month1", "Day1", "Hour1", "Minute1", "Second1"]
        TimeB = ["Year2", "Month2", "Day2", "Hour2", "Minute2", "Second2"]
        if values["-useTime-"] == True:
            timePointA = int(f"{values[TimeA[0]]}{values[TimeA[1]]}{values[TimeA[2]]}{values[TimeA[3]]}{values[TimeA[4]]}{values[TimeA[5]]}")
            timePointB = int(f"{values[TimeB[0]]}{values[TimeB[1]]}{values[TimeB[2]]}{values[TimeB[3]]}{values[TimeB[4]]}{values[TimeB[5]]}")

        out = open(values[1], "a")

        for line in open(values[0]):
            counter = 0
            truelist = [False, False, False]
            if values["-usePlayerName-"] == True:
                print("Playername has been called")
                if line.__contains__(values[2]):
                    truelist[0] = True
            else:
                truelist[0] = True


            if values["-useCords-"]:
                print("Cords is called")
                if line.__contains__(f"X= {values[3]}, Y= {values[4]}, Z= {values[5]}"):
                    truelist[1] = True
            else:
                truelist[1] = True


            if values["-useTime-"] == True:
                print("Time is called")
                x = ""
                time = x.join(line[0:21])
                time = timeConstructer(time)
                print(f"A: {timePointA}; B: {timePointB}; time: {time}")
                if timePointA < time < timePointB:
                    print("Is in right time window")
                    truelist[2] = True
                else:
                    truelist[2] = False

            else:
                truelist[2] = True

            for i in truelist:
                print(f"Calling true list: {truelist}")

                if i:
                    counter = counter + 1
            if counter == 3:
                print("Line gets pushed")
                out.write(line)
        out.close()
        if values["-stayOpen-"] == False:
            break




    # print('You entered ', values[0])



window.close()