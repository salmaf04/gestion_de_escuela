from backend.domain.schemas.mean_request import MeanRequestModel


class MeanRequestMapper :
    def to_api(self,teacher_id, mean_id) :
        return MeanRequestModel(
            teacher_id=teacher_id,
            mean_id=mean_id
        )
