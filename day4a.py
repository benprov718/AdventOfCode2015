import hashlib

found=False

real_secret="yzbqklnj"
test_secret1="abcdef"
test_secret2="pqrstuv"
test_num1=609040
test_hit1=609043
test_num2=1048900
test_hit2=1048970



def findHash(secret, number):
    hash_str = secret + number.__str__()
    hash = hashlib.md5(hash_str.encode()).hexdigest()
    # print(hash)

    if hash.startswith('00000'):
        # print("This starts with 0000: {0}".format(hash))
        return True
    else:
        # print("This does not start with 0000: {0}".format(hash))
        return False
    pass

number=0
secret=real_secret
while found is False:
    result=findHash(secret, number)
    if result is False:
        number+=1
    else:
        print("{0} is the number that gets secret {1} to produce a hash starting with 00000".format(number,secret))
        found=True