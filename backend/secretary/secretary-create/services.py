from sqlalchemy.orm import Session
from .schemas import SecretaryCreateModel
from database.tables import SecretaryTable

class SecretaryCreateService :

    def create_secretary(self, session: Session, secretary:SecretaryCreateModel) -> SecretaryTable :
        secretary_dict = secretary.model_dump()

        new_secretary = SecretaryTable(**secretary_dict)
        session.add(new_secretary)
        session.commit()
        return new_secretary

    

class SecretaryPaginationService :
    def get_secretary_by_email(self, session: Session, email: str) -> SecretaryTable :
        query = session.query(SecretaryTable).filter(SecretaryTable.email == email)

        result = query.first()

        return result



