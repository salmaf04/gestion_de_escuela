import {IUsuarioLocal} from "../models/IUsuarioLocal.ts";

export class UsuarioAdapter implements IUsuarioLocal{
    static Properties = ['ID', 'Nombre', 'Apellidos', 'Usuario', 'Roles']
    id: string
    name: string
    username: string
    lastname: string


    constructor(user: IUsuarioLocal){
        this.id = user.id
        this.username = user.username
        this.name = user.name
        this.lastname = user.lastname
    }
}