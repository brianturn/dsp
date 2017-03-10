# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>> 1. pwd (show current working directory)
>> 2. mkdir (create directory)
>> 3. rmdir (delete directory)
>> 4. touch *filename* (creates a file)
>> 5. rm (deletes file)
>> 6. rm -r (deletes a directory and it's contents)
>> 7. mv *filename* *newfilename* (renames filename to new filename)
>> 8. ls -a (lists hidden files)
>> 9. cp *filename* *directoryname/* (copies file to specificed directory)
>> 10. * (wildcard selects all)
>> 11. open *filename* (opens file)
>> 12. grep -l *word* (returns a list of files with specified word)


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> 1. ls (lists files in working directory)
>> 2. ls -a (lists hidden files in working directory)
>> 3. ls -l (long version of files showing permissions, number of directories, user, size, date last modified, filename)
>> 4. ls -lh (prints long version with human readable file size i.e. 10MB)
>> 5. ls -lah (prints long version including hidden files with human readable file size i.e. 10MB)
>> 6. ls -t (prints files in reverse chrono from date last modified)
>> 7. ls -Glp (prints files in long format minus owner)
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> 1. ls -log (without group or owner)
>> 2. ls -lm (comma separated format)
>> 3. ls -lp (displays directory with /)
>> 4. ls -R (displays subdirectories and the files inside them)
>> 5. ls -1 (display each directory on a row, more readable)

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> Repeats an operation on a list of files, usually produced with a 'find' or 'grep' command and passed through a pipe.

```console
find . -name "*.py" | xargs grep "time"
```

>> The above code finds all files in the current directory ending in .py and returns all files containing the word "time".

 

