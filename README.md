# Test-Exam-Generator
Generate test exams providing a text file with the suitable format.
Created with Python37

## How to use?

It is thought to be very simple and useful.

You only need a file in .txt with the adequate format (See The Format section)


*If you have a pdf file try a website converter (example : https://www.pdf2go.com) or something like this script *

https://gist.github.com/vinovator/c78c2cb63d62fdd9fb67

```
python TestGen.py {filename}

example :

python TestGen.py TestExample

(The .txt is included in the program, so you don't need to write it again)
```
## Useful variables
I've created this tool thinking that not all test are the same, so u could need to personalize this program.
To make it easier these are the variables u can control :


Number of options (a,b,c,d) = 4
``` 
numOpciones = 4
``` 
The word that delimits the solutions (See the format section)
``` 
WORD = "RESPUESTAS"
``` 
If you have some dir with exams, for example.

/home/user/exams
- /exam1
- /exam2

You could set RUTA = "/home/user/exams/" so you only would need to enter the name of the file and not the full path
``` 
RUTA = ''

```
## The Format

This tool tries to be universal, but due to variety of exams that exists, we need to follow a little format in order to make this program work correctly.

#### Questions:
Should start with 
```
NUMBER) or NUMBER.
```
#### Answers
Should start with 
```
a) or a. 
(Also working with caps)
```
#### Solutions
There are many ways of specify the solutions of the test.
I recomend to follow one of these:
```
1 a
1-a
1- a
1. d.
etc...
(Also working with caps)
```

In the script i specified a word to delimit the start of the solutions.
It is "RESPUESTAS" but u can change that with a little modification of the code.

### Simple example of the format

#### Questions and Answers example
![alt text](https://i.imgur.com/JpLMh2w.png)
#### Solutions example
![alt text](https://i.imgur.com/Z5CPX2z.png)



#### TODO

- Format code, make it readable (I'm a mess, sorry)
- Run some tests with many files
- Try to improve the pdf to txt tool.
