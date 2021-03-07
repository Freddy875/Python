myUniqueList = []

LeftoverList = []

def appeandElement(element):
    flag = False
    if element not in myUniqueList:
        myUniqueList.append(element)
        flag = True
        return flag
    else:
        LeftoverList.append(element)
        flag = False
        return flag

def messenger(element):
    if(appeandElement(element)):
        print(element, "added to the unique list")
    else:
        print(element,"added to the leftover list")

appeandElement(1)
appeandElement(2)
appeandElement(3)
appeandElement(1)
appeandElement(3)
appeandElement("Hello")
appeandElement(2)
appeandElement("Hello")

print("Unique element list: ",myUniqueList)
print("Leftover list: ",LeftoverList)


    