import re

task_file=open('taskfiles/task5.txt', 'r')
num_good=0
# test_string1='xyxy'
# test_string2='qjhvhtzxzqqjkmpb'
# test_string3='xxyxx'
# test_string4='uurcxstgmygtbstg'
# test_string5='ieodomkazucvgmuy'

def evaluate_good(stringsubject):
    # print("Evaluating {0}".format(stringsubject))
    global num_good
    two_pair= False
    eve= False
    num_gw=0
    if re.search(r"(..).*\1",stringsubject):
        two_pair=True
        # print("Two pairs")
    if re.search(r"(\w).\1", stringsubject):
        eve=True
        # print("letter split by letter")
    if two_pair & eve:
        # print("{0} is a good string".format(stringsubject))
        num_good+=1
    return

for line in task_file:
    evaluate_good(line)
# evaluate_good(test_string1)
# evaluate_good(test_string2)
# evaluate_good(test_string3)
# evaluate_good(test_string4)
# evaluate_good(test_string5)

print("There are {0} good strings!".format(num_good))
