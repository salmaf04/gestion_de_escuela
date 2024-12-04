from mean.mean_common.schemas import MeanModel
from sqlalchemy.orm import Session
from database.tables import MeanTable
from sqlalchemy import select
from .filters import MeanFilterSet , MeanFilterSchema


class MeanListingService:
    def get_means(self, session: Session, filter_params: MeanFilterSchema) -> list[MeanTable] :
        query = select(MeanTable)
        filter_set = MeanFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
