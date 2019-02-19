# Test-Exam-Generator
Generate test exams providing a text file with the suitable format.


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
