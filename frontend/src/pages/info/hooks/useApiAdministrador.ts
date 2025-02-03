// frontend/src/pages/administradores/hooks/useApiAusencias.ts
import { useContext, useState } from "react";
import { AppContext } from "../../../App.tsx";
import apiRequest from "../../../api/apiRequest.ts";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";
import {IAdministradorDB} from "../models/IAdministradorDB.ts";

const endpoint = EndpointEnum.ADMIN;

export const useApiAdministradores = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [administradores, setAdministradores] = useState<IAdministradorDB[]>();
    const [administrador, setAdministrador] = useState<IAdministradorDB>()

    const { setError, administradores: administradoresAppContext, setAdministradores: setAdministradoresAppContext } = useContext(AppContext);

    const getAdministradores = async () => {
        setIsLoading(true);
        if (administradoresAppContext)
            setAdministradores(administradoresAppContext);

        const res = await apiRequest.getApi(endpoint);
        if (res.ok) {
            const data: IAdministradorDB[] = await res.json();
            setAdministradores(data);
            setAdministradoresAppContext!(data);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    const createAdministrador = async (administrador: Partial<IAdministradorDB>) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, administrador);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateAdministrador = async (id: string, administrador: Partial<IAdministradorDB>) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, id, {}, getQueryParamsFromObject(administrador))
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const deleteAdministrador = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const getAdministrador = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.getApi(endpoint, getQueryParamsFromObject({id: id}));
        if (res.ok){
            const data: IAdministradorDB[] = await res.json()
            setAdministrador(data[0])
        }
        else
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        administradores,
        isLoading,
        getAdministradores,
        createAdministrador,
        deleteAdministrador,
        updateAdministrador,
        getAdministrador,
        administrador
    };
};