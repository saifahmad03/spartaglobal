# Version Control and Git

## What is VCS?

**VCS** stands for **Version Control System**.

A Version Control System is a tool used to track changes made to files over time, particularly when working on software projects.

It allows developers to:

- Track changes to their code
- View previous versions of files
- Restore older versions if something goes wrong
- Work on different features without affecting the main project
- Collaborate with other developers
- See who made changes and when they were made

### Example

Imagine you are developing an application and make a change that accidentally breaks it.

Without version control, you may have to manually work out what you changed.

With version control, you can look at previous versions of the project and restore working code.

---

## What is Git?

**Git** is a distributed Version Control System.

It is used to track changes to files and manage different versions of a project.

Git is commonly used by software developers and data professionals to manage code and collaborate with others.

Git can be used with services such as GitHub, GitLab and Bitbucket.

> **Git and GitHub are not the same thing.**
>
> Git is the version control system.
>
> GitHub is an online platform that can store Git repositories.

---

## How Does Git Work?

Git tracks changes inside a **repository**.

A repository, often called a **repo**, is a project folder that Git is tracking.

A basic Git workflow looks like this:

### 1. Working Directory

This is where you create and edit your files.

For example:

```text
project/
├── README.md
├── main.py
└── data.csv