# QuizLearn
Hello, and welcome to my latest project– and by latest, I mean a program I started writing a few months back, until I got lazy and abandoned it without even creating a README. How foolish I was... Anyways, I have returned, and have pretty much finished the program. What does it do? Oh, right. This is a README, after all. This program indexes notecard sets on the site [quizlet.com](https://quizlet.com), and finds mnemonic devices for each term. Quizlet's little memorization tests work decently for learning terms, but what you *really* need are unique puns that are so ridiculously stupid that you can't possibly forget them. Instead of having to think of your own puns, QuizLearn searches the [mnemonicdictionary](http://www.mnemonicdictionary.com) website for the best fits.

Here's how to use it...

## Installation
Given that you are on Github looking at programs made with python, I am going to guess you have python installed (or you at least have a Mac with python pre-installed). If not, head over to their [website](https://www.python.org) and grab it.

Now, fire up Terminal and download a few libraries with the python package manager (pip). We will use libraries these to grab data from the quizlet and mnemonicdictionary websites.

`$ pip install beautifulsoup4`  
`$ pip install requests`

## Usage
Download the program, and execute it with python.

```bash  
$ git clone https://github.com/Manwholikespie/QuizLearn.git  
$ cd QuizLearn  
$ python quiz.py```


From here, all that's left to do is paste in the url of the quizlet you want to index and hit Enter.

![image](http://i.imgur.com/XxOqmK3.png)

## Upcoming Features:
- Generate notecard images

## Special Thanks
I would like to thank every single Indian that posted on mnemonicdictionary in Hindu. Having my program spit out random Unicode gibberish beacuse it can't transform Hindu into native python strings is really great.