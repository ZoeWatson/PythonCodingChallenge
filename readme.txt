Hello! 
Author: Zoe Watson, linked in: https://www.linkedin.com/in/zma-watson/

build instructions
Run start.py to launch the program.
Note: it should launch from there fine, but I haven't been able to test on another machine.

This program is designed to intake logfiles and report how many incident of a fault sequence
are contained within. The fault sequence is indicated by four operations that occur in sequence: 
1.	Stage 3 for five minutes or more
2.	Stage 2, 
3.	Any number of cycles between stage 2 and 3 for any duration
4.	Stage 0 

Application Map 
GUI.py is charged with creating the graphical interface functions 
logIncidentCounter.py is charged with counting the incidents in the event log 
logSanitizer.py is charged with sanitizing the event log so it can be counted
Main is charged with creating the application
Start is run to start the program
Test files are labeled TestFileName
The folder TestFiles has sample files to test the program on

Assumptions
- data is chorological order 
- unit can only be in stages [0,1,2,3]
- the unit cannot not have a stage or be in 2 or more stages at once 
- Logs are stored in tab-delimited files with each row containing a Date-Time/Value pair.
- An entry is recorded each time the unit changes stage
- the log file records the stage as integer values [0,1,2,3] there is no records like 
        [zero, 0-apple, 1.5, ect.]
- the log files records the date as year-month-day hour:minute:second 
- the log file records date-time in the first column, value in the second
- Only 1 an incident occurs at a time:
    if an incident occurs in the middle of an incident it is counted as one incident
    EX: [stage 3 for 5 mins, stage 2, stage 3 for 5 mins, stage 2, stage 0]
    would be 1 incident not two. 

Theory and Methods:
- Language
The first step of the project was choosing what language would be the right tool for the job.

The project goals had two components, 1. Build the described system, and 2. Demonstrate my fit for 
the role. In service of the second consideration I had hoped to use one of the languages described in 
the job post, (C#, C++, or PHP and JavaScript/TypeScript, Node.js),  however they turned out not to be 
a good fit.

I identified 3 key needs the project needed to fulfill based on the assignment documentation: 
The product requires user input of files. 
The product may be hosted or desktop but since I’m traveling it needs to be desktop due to spotty Wi-Fi.
The product must have a user interface.

Lastly and this is somewhat meta, the product must be written fast. There is only a week given to 
write the app, and I had my own time commitments as well. 

Within in these constraints I considered the following
Node.js [Electron] : poor testing architecture, unstable.
JavaScript : no easy way to make a desktop app without electron, and thus poor testing architecture. 
C# :  isn't compatible with Linux and mac and I wasn’t told what the program would be tested on.
C++ : heavy architecture, not a good fit for a quick app like this.
Python : built in GUI, automatic testing, and user input modules, fast and desktop based. 

So despite it not being in the job description I found Python to be the best fit for the project. 

- Documentation
My inline documentation is a bit thin. My goal is to write code so readable that inline documentation 
isn’t needed because the function/variable names serve to convey their functions. Though it’s the 
reader’s discretion if I achieved that. 

- Testing
I neglected user input and GUI testing. While there are tests you can write to test GUI and UI 
the complexity would require additional time.
I would have also liked to have created larger files to test on. My largest file is only 200+ where 
log files routinely go over 10,000+
I'd also have liked to write tests in more of a given-when-then model. 

- AI 
 I used Chat GPT with caution to write unit tests.
 I wouldn't do so on production code due to security concerns, but in this case it saved time 
 while allowing for more complete testing than I would have been able to write myself in the 
 time I had.
I also used chat GPT to generate long log files to test on.

- Reflection
Overall this took closer to 8 hours instead of five, perils of writing code stop and go
instead of in one sitting. I broke the problem down into three components, the incident counter,
the log sanitizer and the GUI. I built the GUI and the log sanitizer first, then the incident counter. 
Finally I wrote the tests. (not best practice I know, but needs must and it allowed me to experiment
with ChatGPT which I appreciated.)

My method was to keep the code as readable and robust as possible. Focusing particularly on
single responsibility and dependency inversion. I also spent a fair amount of time 
thinking about the user experience, which led to bonus features like system reporting when and 
where in the log the incidents occurred. 

If I were to invest more time into this system I’d:
Make the UI more reactive
Create user messaging for invalid data
Make  the invalid data sanitizing more robust. 
Refactor so the code is more object oriented. 
Refactor so the tests are more strictly unit tests. 







