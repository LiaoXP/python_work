from survey import AnonymousSurvey
#define a question, and create an instance of AnonymouSurvey,
#which represents the survey

question = "What language did you first learn to speak?"

my_survey = AnonymousSurvey(question)

#show the question and store the answer
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Your language: ")
    if response == "q":
        break
    my_survey.store_response(response)

#show results
print("\nThanks for participating!")
my_survey.show_results()