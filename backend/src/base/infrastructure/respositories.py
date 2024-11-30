from abc import ABC, abstractmethod
from models import BaseEntity

class IBaseRepository(ABC) :
    
    @abstractmethod
    def create(self , entity: BaseEntity) -> BaseEntity :
        pass

    @abstractmethod
    def update(self , entity: BaseEntity) -> BaseEntity :
        pass
    
    @abstractmethod
    def delete(self , entity: BaseEntity) -> BaseEntity :
        pass
    
    @abstractmethod
    def read(self , entity: BaseEntity) -> BaseEntity :
        pass
    
     
    