import {useContext, useState} from "react";
import {UsuarioGetAdapter} from "../adapters/UsuarioGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {IUsuarioCreateDB} from "../models/IUsuarioCreateDB.ts";
import {IUsuarioDB} from "../models/IUsuarioDB.ts";

const endpoint = EndpointEnum.USUARIOS

export const useApiUsuarios = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, usuarios: usuariosAppContext, setUsuarios: setUsuariosAppContext, personalId, setMessage} = useContext(AppContext)

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
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getUsuarios()
        setIsLoading(false);
    };

    const solicitarUsuario = async (classRoom: {classroom_id: string}) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(EndpointEnum.CLASSROOM_REQUEST+"/"+personalId, classRoom);
        if (!res.ok)
            setError!(new Error(res.statusText));
        else
            setMessage!("Solicitud enviada correctamente")
        await getUsuarios()
        setIsLoading(false);
    };

    return {
        isLoading,
        getUsuarios,
        createUsuario,
        deleteUsuario,
        updateUsuario,
        solicitarUsuario
    }
}