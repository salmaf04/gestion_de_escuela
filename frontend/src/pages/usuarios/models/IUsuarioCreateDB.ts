import {RolesEnum} from "../../../api/RolesEnum.ts";

export interface IUsuarioCreateDB {
    username: string,
    name: string,
    lastname: string,
    email: string,
    roles: RolesEnum[],
    type: RolesEnum
}