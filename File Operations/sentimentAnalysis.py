class Sentiment:
    goodList=["happy","smile","good","well"]  # List of all Positive words for comparison
    badList=["sad","bad","hell"]  # List of all Positive words for comparison
    good_out=[]  # Store Positive words from the file
    bad_out=[]   # Store Negative words from the file
    neutral_out=[]  # Store Neutral words from the file

    # Method to parse the file and group words to different list
    def getListFromFile(self,source_file):
        f=open(f"{source_file}")
        for element in f:
            data=element.rstrip("\n").rsplit()
            for content in data:
                if content in self.goodList:
                    self.good_out.append(content)
                elif content in self.badList:
                    self.bad_out.append(content)
                else:
                    self.neutral_out.append(content)

   # Method for finding the list count and Checking the most emotion and print the respective lists
    def mostEmotion(self):
        good_count=len(self.good_out)
        bad_count=len(self.bad_out)
        neutral_count=len(self.neutral_out)

        if(good_count > bad_count) and (good_count>neutral_count): # The emotion is positive
            print("\n\n************ The response is very Positive ************ \n\n\n")
        elif(bad_count>good_count) and (bad_count>neutral_count): # The emotion is negative
            print("\n\n************ The response is Negative  ************\n\n\n")
        else:  # The emotion is Neutral
            print("\n\n\n************  The response is Neutral   *************\n\n\n")
        print("Positive words list contains : \n ",self.good_out," & Word Count = ",good_count)
        print("Negative words list contains : \n ",self.bad_out," & Word Count = ",bad_count)
        print("Neutral words list contains : \n ",self.neutral_out," & Word Count = ",neutral_count)


check=Sentiment() # Object of class Sentiment
check.getListFromFile("sentiment_details") # Passing the file that to be  parsed
check.mostEmotion()
