from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

CreateModel = TypeVar('CreateModel')
Model = TypeVar('Model')
ChangeRequest = TypeVar('ChangeRequest')
FilterSchema = TypeVar('FilterSchema')


class IRepository(Generic[CreateModel, Model, ChangeRequest, FilterSchema], ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def get(self, filter_params: FilterSchema) :
        pass

    @abstractmethod
    def get_by_id(self, id: str) :  
        pass

    @abstractmethod
    def delete(self, entity: Model) :
        pass

    @abstractmethod
    def create(self, entity: CreateModel, *args, **kwargs) :
        pass

    @abstractmethod
    def update(self, changes: ChangeRequest, entity: Model, *args, **kwargs) :
        pass