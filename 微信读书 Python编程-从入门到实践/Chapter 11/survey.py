class AnonymousSurvey():
    def __init__(self, question):
        """store a question and prepare for storing the answer"""

        self.question = question
        self.responses = []

    def show_question(self):
        """show questionare"""

        print(self.question)

    def store_response(self, new_response):
        """store single set of questionare"""

        self.responses.append(new_response)

    def show_results(self):
        """show all received questionare"""

        print("Survey results:")

        for response in self.responses:
            print("-" + response)