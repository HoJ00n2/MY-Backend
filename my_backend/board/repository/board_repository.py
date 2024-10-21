from abc import ABC, abstractmethod
class BoardRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create_category(self, name):
        pass

    @abstractmethod
    def create(self, categoryId, title, accountId, content, contentImage):
        pass

    @abstractmethod
    def findByBoardId(self, boardId):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass