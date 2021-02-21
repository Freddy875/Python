#Favorite movie

def Title():
    TitleName = "Star Wars: A new Hope"
    return TitleName


def Director():
    Name = "George Lucas"
    return Name

def Duraction():
    OriginalVersion = 121
    SpecialVersion = 125
    Long = (OriginalVersion < SpecialVersion)
    return Long

def Profits():
    Budget = 13.000
    Takings= 775.385 
    #The Budget and Takings is in USD
    Money = (Takings > Budget)
    return Money


print("What is your favoriete movie? " + Title())
print("Who is the director? " + Director())
print("The Special Version from Star Wars is longer than the Original Version")
print(bool(Duraction()))
print("Star Wars had more takings than budget")
print(bool(Profits()))




