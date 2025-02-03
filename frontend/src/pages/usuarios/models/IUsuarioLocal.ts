import {DBObject} from "../../../types.ts";

export interface IUsuarioLocal extends DBObject{
    id: string,
    username: string,
    name: string,
    lastname: string,
}