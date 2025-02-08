import {useContext, useState} from "react";
import {UsuarioGetAdapter} from "../adapters/UsuarioGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {IUsuarioCreateDB} from "../models/IUsuarioCreateDB.ts";
import {IUsuarioDB} from "../models/IUsuarioDB.ts";
import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";
import {useApiDecano} from "./useApiDecano.ts";
import {useApiSecretaria} from "../../info/hooks/useApiSecretaria.ts";
import {useApiAdministrador} from "../../info/hooks/useApiAdministrador.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";

const endpoint = EndpointEnum.USUARIOS

export const useApiUsuarios = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, usuarios: usuariosAppContext, setUsuarios: setUsuariosAppContext} = useContext(AppContext)
    const {deleteProfesor} = useApiProfesor()
    const {deleteEstudiante} = useApiEstudiante()
    const {deleteDecano} = useApiDecano()
    const {deleteSecretaria} = useApiSecretaria()
    const {deleteAdministrador} = useApiAdministrador()

    const getUsuarios = async () => {
        setIsLoading(true)
        if (usuariosAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: IUsuarioDB = await res.json()
            const usuarioArray = Object.values(data)
                .map((usuario: IUsuarioDB) => new UsuarioGetAdapter(usuario))
            setUsuariosAppContext!(usuarioArray)
        } else {
            setError!(new Error(res.statusText))
        }

        setIsLoading(false)
    }

    const createUsuario = async (usuario: IUsuarioCreateDB) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, usuario)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getUsuarios()
        setIsLoading(false)
    }
    const updateUsuario = async (id: string, usuario: IUsuarioCreateDB) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, usuario)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getUsuarios()
        setIsLoading(false)
    }

    const deleteUsuario = async (id: string) => {
        setIsLoading(true);
        const role = usuariosAppContext!.find(usuario => usuario.id === id)!.type
        switch (role) {
            case RolesEnum.TEACHER:
                await deleteProfesor(id)
                break
            case RolesEnum.STUDENT:
                await deleteEstudiante(id)
                break
            case RolesEnum.DEAN:
                await deleteDecano(id)
                break
            case RolesEnum.SECRETARY:
                await deleteSecretaria(id)
                break
            case RolesEnum.ADMIN:
                await deleteAdministrador(id)
                break
            default:
                break
        }
        await getUsuarios()
        setIsLoading(false);
    };

    return {
        isLoading,
        getUsuarios,
        createUsuario,
        deleteUsuario,
        updateUsuario,
    }
}