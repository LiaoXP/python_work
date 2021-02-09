import unittest

from survey import AnonymousSurvey

class TestAnonoymousSurvey(unittest.TestCase):
    """Test for class AnonymousSurvey"""
    def setUp(self):
        """create a question and a group of answers, for the test methods below"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]
        return super().setUp()
    def test_store_single_response(self):
        """test if single response will be stored properly"""
        
        
        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """test if three responses can be stored properly"""

        

        
        

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()