"""Accept any city from the user and display monument of that city.
                  City                                 Monument
                  Delhi                               Red Fort
                  Agra                                Taj Mahal
                  Jaipur                              Jal Mahal"""


city=input("Input your city").lower()  # Converted red string to lowecase

if(city=="delhi"):
    print("Redfort")
elif(city=='agra'):
    print("Taj Mahal")
elif(city=='jaipur'):
    print("Jal Mahal")
else:
    print("Wrong city")