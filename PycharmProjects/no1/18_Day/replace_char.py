st = 'abc'
st1=''
for var in st:
    if var.isalpha():

        var1=ord ( var )
        var2 = var1 +13

        if (122>=var2 and var2>=97) or (90>=var2 and var2>=65):
            st1+=chr(var2)

        elif var2>122 or 90<var2:
            var1=var1-13
            st1+=chr ( var1 )

        elif var2<97 or var2<65:
            var1=var1+13
            st1+=chr ( var1 )
    else:
        st1+=var
print(st1)
