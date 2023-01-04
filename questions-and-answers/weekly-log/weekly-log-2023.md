---
revision:
    "2023-01-03": "(A, mos) First release."
---
Weekly log
=====================

This is the teachers notes on what might be important to do to get a nice journey through these parts of the course.

[[_TOC_]]



Precondition
---------------------

You should have knowledge on Git and GitHub and you should have Git with GitBash installed on your environment.

You should have knowledge on how to write a object oriented program with Python using classes.



Overview of part 2 & part 3
---------------------

"Part 2: Testing" is about testing and documentation of the code.

* Work in teams of two and two and develop an application using object oriented Python.
    * Apply linters to enhance the code.
    * Use unit testing.
* Oppose on other projects by reviewing them.

"Part 3: Clean Code" is about the concept of what makes clean and good code.

* Write a report and summarize your view of the topic and your learnings from the project work and the opposition.



Prepare
---------------------

Prepare yourself through the following.

1. [Work with Git](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/doc/work-with-git.md). Review this article that provides an overview of Git commands and practice the commands on the terminal Git Bash. The article includes a [video playlist](https://www.youtube.com/playlist?list=PLEtyhUSKTK3iTFcdLANJq0TkKo246XAlv) that shows the basics.

Using Git is optional but recommended.



Week 05 - Part 2 Testing
---------------------

Lets start upp part 2 of the course, a project in object oriented Python with unit testing.

**Teacher activities**

* "Lecture 05 - Introduction to the module" is an introduction to part 2 & part 3 of the course.
* Walkthrough of the Assignment 02 project.

* About object oriented programming with Python. Hmmm, is this already fixed?
* About importance of development environment.


### Things to do on your own

To be on top of things you should individually do these exercises that are part of Lecture 05.

* Install the lab environment.
* Try out the example programs in the example repo.
* Ensure you can setup a git repo and connect to GitHub.
* Setup your own personal Python development project using a venv.
    * A [project template](https://gitlab.com/mikael-roos/python-template) is available to make this easier.
* Read the A02 to learn what your team should do in the project.

You should try to do this before you meet with the team. That is the way to prepare yourself and becoming an active team member.



### A healthy team

You now have one week to get your team up to speed with the A02.

* Have a first meeting.
    * Make a health check, ask all members if they feel okey and are onboard and ready.
    * What can each one bring to the table?
* Walkthrouth the A02, prioritize if needed and decide on the project focus.
* Do a rough sketch on the class design (UML).
* Roughly try to divide the work (you do that class and you do that class), you can change this as the project goes on.
* Appoint a Git manager or someone who will be responsible to integrate all the members code into a working version.
* Create the working directory and its structure, put it onto GitHub (or GitLab) so everybody has the same setup and easy access to linters and testtools.
    * A [project template](https://gitlab.com/mikael-roos/python-template) is available to make this easier.
* Make a main.py and you are on your way. Integrate your code at least once a week to avoid integration problems.

Try to have some code written already by early next week. If you have that - then it will be a great start for unittesting.



Week 06 - Unit testing
---------------------

Add unit tests to your project.

**Teacher activities**

The session in class will focus on the exercise "Exercise 2 - Unit testing and code coverage in Python" that will learn you the basics of unit testing and code coverage in Python.

There will also be discussions on how to get going with the team and start with a solid base.

Questions and things to deal with (first session in class were discussions about this)...

* How to get going with the team work
* Coding
    * Read through spec and agree on your focus
    * Sketch an UML diagram
    * Agree on classes and larger modules (with several classes)
    * Work using public interfaces and create empty classes/methods
    * Divide work in team - some do more, some do less - its fine

* Git master & integration manager
    * Setup a git repo for the project
        * Perhaps use the available python template to get a quick start
    * Create empty files, but name them so everybody sees the whole picture
        * Create usable but empty classes & methods for the public interfaces
    * Integrate for the first time and see that it works
        * Make someone responsible for Main/Shell class that tie it all together into an application?
    * Add the testsuite
        * Add empty test files
        * Add testclasses for each testobject
        * Add a empty/assertTrue testcase for each class
        * Run the testsuite and see it work and pass

* Start work
    * Do not change the public interface without having a discussion on it, perhaps GitHub issues would be a great idea
    * Integrate early, at least once a week or when needed
    * Do not integrate before each has a passing testsuite
    * Integrate by:
        * Copying files
        * Fork and pull requests
        * All write to the same repo and work in
            * main
            * branches

**Lectures**

During this week you shall review the pre recorded lectures that also have reading instructions.

* Lecture 6 - Introduction to Software Testing
* Lecture 7 - Software Unit Testing

**Work**

* Add unit testing to A02 (amongst other things).



Week 07 - TDD and Documentation
---------------------

Final week of part 2.

**Teacher activities**

The session in class will focus on the following exercises:

* Exercise 3 - Test Driven Development
* Exercise 4 - Software Documentation

You should now have a pretty good idea on how to structure your code to make it testable. Writing code that is easy to test is a good feature of a programmer.

We will also see how the following code can be tested.

* Randomized values
* Exceptions
* Functions that print

**Lectures**

During this week you shall review the pre recorded lectures that also have reading instructions.

* Lecture 8 - Test-driven development
* Lecture 9 - Software Documentation

**Work**

* Prepare to submit A02 next week.



Week 08 - Part 3 Clean code
---------------------

Start of part 3 of the course.

**Teacher activities**

* "Lecture 10 - Introduction to the module" is an introduction to this part of the course.
* The Assignment 3 "Sustainable programming through good and clean code" will be presented together with guidelines on how to structure the report.

The session in class will focus on the following exercises:

* Exercise 5 - Static code analysis and metrics

**Lectures**

During this week you shall review the prerecored lectures that also have reading instructions.

* Lecture 11 - What about good and clean code?

**Work**

* Deadline to submit A02.



Week 09 - Opposion and Report week
---------------------

**Teacher activities**

* Start the opposition part of A02.
* Classroom session with analysing metrics.
* Helpsession with the writing of the report.

**Lectures**

During this week you shall review the prerecored lectures that also have reading instructions.

* Lecture 12 - Software development philosophies
* Lecture 13 - Static code analysing and metrics

**Work**

* Begin the opposition part of A02.
* Write on your report A03.



Week 10 - Submission week
---------------------

**Teacher activities**

* Supervision and helpsession with the writing of the report.

**Submit your work**

* Submit the opposition report on A02.
* Submit the report on A03.
