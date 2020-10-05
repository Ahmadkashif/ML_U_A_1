##
## This is the main Assignment runner function.
#
from Question__1_ import question1
from Question__2_ import question2
from Question__4_ import question4

question1Input = "qwertyuiopasdfghjklzxcvbnm";
question2Input = [[33, 120], [40], [30, 56, 25], [33, 120], [33], [40]];
question4Input1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
question4Input2 = {
    'x':3,
    'l':4,
    'a':2,
    'b':3,
    'c':4
}
print(">>>>>question 1 output<<<<<")
print(question1(question1Input))
print(">>>>>question 2 output<<<<<")
print(question2(question2Input))
print(">>>>>question 4 output<<<<<")
print(question4(question4Input1,question4Input2))
