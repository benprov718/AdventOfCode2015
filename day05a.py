import re

task_file=open('taskfiles/task5.txt', 'r')
good_vowels='aeiou'
bad_strings=['ab','cd','pq','xy']
num_good=0
# test_string1='ugknbfddgicrmopn'
# test_string2='aaa'
# test_string3='jchzalrnumimnmhp'
# test_string4='haegwjzuvuyypxyu'
# test_string5='dvszwmarrgswjxmb'


def evaluate_good(stringsubject):
    # print("Evaluating {0}".format(stringsubject))
    global num_good
    double= False
    num_gw=0
    for element in bad_strings:
        if element in stringsubject:
            return
    for letter in stringsubject:
        if ( letter in good_vowels ):
            num_gw+=1
    if re.search(r"(.)\1",stringsubject):
        double=True
    if ( num_gw >= 3) & double:
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
