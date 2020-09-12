# First steps on git

## 1. Review the project folder
Move to the Markdown sample folder
```
cd Markdown_Notes
```

List all files in the current directory
```
ls -ls
```

To know the full path of your current directory is
```
pwd
```

## 2. Initialize your project
```
git init
```
When .git folder is created, the folder become in working directory
 **Remember, the .git folder is untouchtable**

## 3. Git project configuration
### 3.1. Add email 
We add the email in git configuration

Example
```
git config --global user.email "<user@mail.com>"
```

### 3.2. Add user name
```
git config --global user.name "<your user name>" 
```

## 4. Show the status of the project
```
git status
```
- In green color shows the files in staging area
- In red color shows the files without tracking. 


## 5. Adding files to stagin area

The basic syntax is 
```
git add <full_path>/<file_name>
```

Adding the file Git_FirstSteps.md to stagin area
```
git add Git_FirstSteps.md
```

Then, check the status
```
git status
```

When you want to add all files use the shortcut
```
git add .
```

To remove a file from stagin area 
```
git rm --cached <file_name>
```

Remove Git_FirstSteps.md from staging area
```
git rm --cached Git_FirstSteps.md
```

See the file is again untracked
```
git status
```

Finally add the Git_FirstSteps.md to stage again
```
git add Git_FirstSteps.md
```


## 6. Commit files
Commit files is version the files in git repository
There are two ways to commit our files.

### 6.1 Just Commit, and see the vim terminal
```
git commit
```

Write the comment for your commit. The comment is a description of your work. 

Then exit of vim terminal typing esc and then :wq
```
:wq
```

+ w is for write
+ q is for quite

### 6.2 Commit with the -m argument

```
git commit -m "First commit 🚀"
```
Yes.. you can add emojis in your messages


## 7. Show the hash for commit

With log command shows infor of your commits
```
git log
```

## 8. Discard changes in files

### 8.1 checkout command
If you want to remove the recent changes you use the command checkout
```
git checkout -- <file_name>
git checkout -- app.js
```

### 8.2 restore command
``` 
git restore <file_name>
```

## 9. Show the difference from previous version
```
git diff
```

+ -- minus to show what was removed
+ ++ plus to show what was add

## 10. Ignoring files in tracking 

Create a .gitignore file, and list all files and folders you dont want to track.

```
touch .gitignore
```

You can add by filename or wild cards
The files and folders to ignore depends on project and technologies, this is one sample.

```
*.txt
*.log
node_modules
```

## 11. Push your code to GitHub

- Create you account of Git 
- Create a repository call  Steps_MarkDown_Git
- Add the remote repository (verify in GitHub)
- Execute push command

```
git push -u orign master
```

## Resources


### Web Resources

- [Git Documentation](https://git-scm.com/doc)
- [Reference Manual](https://git-scm.com/docs)


### Youtube Resources
- [Fazt: Git and Github | Practical Course from Scratch](https://www.youtube.com/watch?v=HiXLkL42tMU&pp=QAA%3D)
- [Pelado Nerd: Tutorial de GIT para principantes! - Usando la linea de comandos en Git](https://www.youtube.com/watch?v=kEPF-MWGq1w)
- [Pelado Nerd: Tutorial de GIT - Parte 2 / Arreglando tus errores con la linea de comandos y usando Github.com](https://www.youtube.com/watch?v=7-JHoPyJy-Q)
- [Traversy Media: Git & GitHub Crash Course For Beginners](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
