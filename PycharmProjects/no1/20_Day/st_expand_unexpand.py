# 2spaces - one tab


st = 'Aparna  is     looking pretty'

lis = st.split(' ')
print(lis)
lis1=[ ]
j=0
count=0
count2=0
st1=''

def gen_expand(lis):
    for var in lis:
        yield var

for var in gen_expand(lis):
    if var.isalpha ( ):
        count2+=1

        if (count+1) == 2 or count2 == 2:
            st1+='/t'
            count2=0

        elif count != 0 and (count+1)%2 == 0:
            count1=(count+1)/2
            i=1
            while (i <= count1):
                st1+='/t'
                i+=1

        elif count != 0 and (count+1)%2 != 0:
            count1=(count+1)/2
            i=1
            while (i <= count1):
                st1+='/t'
                i+=1
            st1+='/t'

        st1+=var
        count=0

    elif var == '':
        count+=1

print(st1)

