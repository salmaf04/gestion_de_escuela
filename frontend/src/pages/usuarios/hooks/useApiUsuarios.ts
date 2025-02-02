// frontend/src/pages/usuarios/hooks/useApiAusencias.ts
import {useContext, useState} from "react";
import {AppContext} from "../../../App.tsx";
import apiRequest from "../../../api/apiRequest.ts";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";
import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {IUsuarioLocal} from "../models/IUsuarioLocal.ts";
import {ISecretaryDB} from "../models/ISecretaryDB.ts";
import {IAdministradorDB} from "../models/IAdministradorDB.ts";

const endpoint = EndpointEnum.NOTAS;

export const useApiUsuarios = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [usuarios, setUsuarios] = useState<IUsuarioLocal[]>();
    const {getEstudiantes} = useApiEstudiante()
    const {getProfesores} = useApiProfesor()
    const [secretaria, setSecretaria] = useState<ISecretaryDB[]>()
    const [administrador, setAdministrador] = useState<ISecretaryDB[]>()


    const { setError, usuarios: usuariosAppContext} = useContext(AppContext);

    const getUsuarios = async () => {
        setIsLoading(true);
        if (usuariosAppContext)
            setUsuarios(usuariosAppContext);

        await getProfesores()
        await getEstudiantes()
        await getSecretaria()
        await getAdministrador()

        const userArray: IUsuarioLocal[] = []

        setIsLoading(false);
    };

    const getSecretaria = async () => {
        setIsLoading(true);
        const res = await apiRequest.getApi(EndpointEnum.SECRETARIA);
        if (res.ok) {
            const data: ISecretaryDB[] = await res.json();
            setSecretaria(data)
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };
    const getAdministrador = async () => {
        setIsLoading(true);

        const res = await apiRequest.getApi(EndpointEnum.ADMINISTRADOR);
        if (res.ok) {
            const data: IAdministradorDB[] = await res.json();
            setAdministrador(data)
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    const deleteUsuario = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        usuarios,
        isLoading,
        getUsuarios,
        deleteUsuario,
    };
};