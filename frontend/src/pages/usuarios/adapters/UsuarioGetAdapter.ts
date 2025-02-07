import {IUsuarioDB} from "../models/IUsuarioDB.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export class UsuarioGetAdapter implements IUsuarioDB{
    static Properties = ['ID', 'Usuario', 'Nombre', 'Apellidos', "Correo", 'Roles', 'Tipo']
    id: string
    name: string
    username: string
    lastname: string
    email: string;
    roles: RolesEnum[];
    type: RolesEnum;

    constructor(user: IUsuarioDB){
        this.id = user.id
        this.username = user.username
        this.name = user.name
        this.lastname = user.lastname
        this.email = user.email
        this.roles = user.roles
        this.type = user.type
    }


}