from abc import ABC, abstractmethod
from typing import List, Any

class LabPredictor(ABC):
    def __init__(self, model: Any=None) -> None:
        self.model = model

    @abstractmethod
    def predict(self, input_text: str) -> List[str]:
        """ the main predictor function. this should return a list of strings that will be visible in the frontend keyboard

        Args:
            input_text (str): the input text from the frontend keyboard
        """
        raise NotImplementedError

    @abstractmethod
    def train(self, train_data: List[str]) -> None:
        """ the main training function. this should train the model with the given train_data

        Args:
            train_data (List[str]): the training data
        """
        raise NotImplementedError
