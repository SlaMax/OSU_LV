try:
    print("UPIŠI BROJ")
    x=float(input())

    if x < 0.6:
        y='F'
    elif x <= 0.7:
        y='D'
    elif x <= 0.8:
        y='C'
    elif x <= 0.9:
        y='B'
    elif 0.9 < x < 1:
        y='A'
    else:
        raise Exception(f"Morate unjeti broj između 0 i 1")    

except ValueError: 
    print("Morate unijeti broj, ne slovo.")

except Exception as eror : 
    print(eror)

else:
    print(y)
   
    

