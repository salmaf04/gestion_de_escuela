import {DBObject} from "../../../types.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export interface IUsuarioLocal extends DBObject{
    id: string,
    username: string,
    name: string,
    lastname: string,
    type: RolesEnum,
}