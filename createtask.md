{% include navbar.html %}

### Final Collegeboard Create Task 

-[Github Pages](https://noahj214.github.io/NoahJengCSP/createtask)

-[Repl](https://replit.com/@NoahJeng/Noah-and-Tim-Create-Task#main.py)

### Idea
I was thinking of doing something like a quiz or survey that the user can interact with. It will be similar to the pair/group create task that we did last tri. 
We did a sports image quiz, where you guess different sports teams based on their logos. For my college board create task, I want to do something similar to this, however not based on sports.
I want to make it on a more useful topic, such as current world issues. I will use a similar format to the imageQuiz. 

### Code
[Image Quiz](https://github.com/NoahJ214/Team-Aaiaa-Project-Tri-2/blob/main/templates/imageQuiz.html)

## Ideas
* GPA Calc for student athletes
* Sports game
* Sports Quiz
## Final Decision
The idea we decided on in the end was a sports logo quiz. With the GPA calculator, we weren't able to get a couple requirements. And we weren't sure what sports game to create without it being wildly complicated. Which left us with our quiz. In our quiz, a sports team will be written at the top and you have to try and guess which logo is that team's out of 4 options. It will keep tally of your score and give you a final score at the end.
| Requirement  | Application |
| ------------- | ------------- |
| One list (or other collection type) | List of Questions for quiz.  |
| One Procedure  | Called function to shuffle quiz questions on load.  |
| Algorithm that includes sequencing, selection, and iteration  | Also included in question order randomizer. |
| Calls to student developed procedure | Calls question shuffler for random question order. |
| User Input  | Logo/answers for each question. |
| Instructions for output  | Final score at the end of the quiz. |

## Create Task Plan: Sports Team Logo Guesser Game

□ Instructions for input from one of the following: ◆ the user (including user actions that trigger events) ◆ a device ◆ an online data stream ◆ a file

User input that will be included is the answers to each question which would be the logos.

□ Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose

We have a list of our various questions and their answers in order to be pulled when the user starts the quiz and creates a randomly ordered quiz for them.

□ At least one procedure that contributes to the program’s intended purpose, where you have defined: ◆ the procedure’s name ◆ the return type (if necessary) ◆ one or more parameters

One Procedure that is included is our shuffle function which is called when the page is opened. When called, it takes the list of questions and randomly orders them for the quiz.

□ An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure

Algorithm will use selection when it picks a question to display. Iteration will be displayed in that the process of displaying a question, getting an inputted logo answer, and telling the user if they are correct will be completed at the end and the player will be given a score depending on their accuracy. 
   
□ Calls to your student-developed procedure

After the player clicks next when getting a logo guess right/wrong a logo will be displayed for the user to guess.

□ Instructions for output (tactile, audible, visual, or textual) based on input and program functionality

Textual output that displays the user's final score at the end. 


Create Task Video: https://www.youtube.com/watch?v=tIFjXzPk2rs&feature=youtu.be
