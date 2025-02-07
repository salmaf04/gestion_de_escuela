import {DBObject} from "../../../types.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export interface IUsuarioDB extends DBObject{
    id: string,
    username: string,
    name: string,
    lastname: string,
    email: string,
    roles: RolesEnum[],
    type: RolesEnum
}