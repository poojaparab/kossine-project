user_input = input("enter the string:")
a= user_input.split()
a.reverse()
global result_final
def splitting(a):
    result_final = []
    for i in a:
        for j in a:
            latest=""
            if i[-1]==j[0]:
                m=i.index(i[-1])
                b=[m for m in i ]
                b.pop()
                latest=latest.join(b)
                result=latest+j
                if len(result)>11:
                    print(result)


                i=result

            else:
                pass



splitting(a)








