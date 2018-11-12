import pdb

def for_jump(count):
    print("entered in to the function")
    lis = [1,2,3,4,5,6]
    print("reaching to the for loop")
    for var in lis:
        print("enter in to the loop")
        count += 1
        print(var)
        print(count)


pdb.run("for_jump(2)")

# from forloop to outside but cannot jump from outside into a loop
#from outside to finally but cannot jump from finnaly to outside
#l - will show the current exceuting breakpoint
# !pdb.run("for_jump(9)") - can change the value while debugging but the cursor will not change