
age = int (input())


if age <= 1:
    print("infant")
else:
    if age <= 12:
        print("child")
    else:
        if age <= 19:
             print("teen")
        else:
            print("adult")

