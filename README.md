# HashCrack(SHA1)
  Created by Cavan Dunkley for CSC 4980/6980
  The following code is used to to find a password form a list of a millions passwords
  after taking in a hash as an arguement or a hash and salt as an argument.
## Prerequistes
Must be runnin atleast Python 2.7
Will not run on Python 3 and higher(without adjustments)

## Installation
You Can Download Python 2.7 at the following [link](https://www.python.org/download/releases/2.7/)

## Test Hash Problems
- **Test Program Hash:** b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
- **Medium Hacker Hash:** 801cdea58224c921c21fd2b183ff28ffa910ce31
- **Leet Hacker Hash:** ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 **(Salt Term:)** f0744d60dd500c92c0d37c16174cc58d3c4bdd8e

## Password Answers(Number of Password Viewed before answer)
- **Test Program Hash:**  letmein(15)
- **Medium Hacker Hash:**  vjhtrhsvdctcegth(999967)
- **Leet Hacker Hash:** harib(546154)

## Getting Started(Running the program)
#### Windows
```
C:<The path to where your file is> python hashcrack.py arg1
C:<The path where your file is> python hashcrack.py arg1 arg2
``` 
-Arg1 would be the hash that we are finding
-Arg2 would be in cases that we have a salted hash

### MAC
```
cd /location of file/
python hashcrack.py arg1 
python hashcrack.py arg1 arg2
```
-Arg1 would be the hash that we are finding
-Arg2 would be in cases that we have a salted hash
