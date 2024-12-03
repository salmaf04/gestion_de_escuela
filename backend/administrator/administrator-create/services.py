from sqlalchemy.orm import Session
from .schemas import AdministratorCreateModel
from database.tables import AdministratorTable

class AdministratorCreateService :

    def create_administrator(self, session: Session, administrator:AdministratorCreateModel) -> AdministratorTable :
        administrator_dict = administrator.model_dump()

        new_administrator = AdministratorTable(**administrator_dict)
        session.add(new_administrator)
        session.commit()
        return new_administrator

    

class AdministratorPaginationService :
    def get_administrator_by_email(self, session: Session, email: str) -> AdministratorTable :
        query = session.query(AdministratorTable).filter(AdministratorTable.email == email)

        result = query.first()

        return result



