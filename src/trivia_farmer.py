import json
from typing_extensions import Self


class TriviaAnswer:

    def __init__(self: Self, file_path: str) -> None:
        """Initialise the TriviaAnswer class by loading the database of questions - answers, or creating an empty one if it doesn't exist

        Args:
                file_path (str): path to the JSON file containing the database, relative to the directory containing this file.
        """
        self.file_path = file_path
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                self.answers = json.load(f)
        except:
            self.answers = {}

    def save_data(self: Self) -> None:
        """Save the in-memory datastructure to disk"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.answers, f)

    def set_data(self: Self, question: str, answer: str) -> bool:
        """Save the answer to a particular question to the in-memory data structure

        Args:
                question (str): Trivia question
                answer (str): The corresponding answer, as determined by the parser

        Returns:
                bool: True if the question has not been seen before, False otherwise.
        """
        if question not in self.answers:
            self.answers[question] = answer
            self.save_data()
            return True
        return False

    def get_answer(self: Self, question: str) -> str:
        """Retrieve the answer to a particular question

        Args:
                question (str): The question that needs answering

        Returns:
                str: the coresponding answer, empty string if the answer is not available
        """
        return (self.answers).get(question, "")

    def data(self: Self):
        """Return the in-memory map containing the data


        Returns:
                map[str,str]: In-memory mapping of questions to answers
        """
        return self.answers

