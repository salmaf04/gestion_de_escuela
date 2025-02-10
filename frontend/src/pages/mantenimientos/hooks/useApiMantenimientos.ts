import {useContext, useState} from "react";
import {MantenimientoGetAdapter} from "../adapters/MantenimientoGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {IMantenimientoLocal} from "../models/IMantenimientoLocal.ts";
import {IMantenimientoDB} from "../models/IMantenimientoDB.ts";

const endpoint = EndpointEnum.MANTENIMIENTOS

export const useApiMantenimiento = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, mantenimientos: mantenimientosAppContext, setMantenimientos: setMantenimientosAppContext} = useContext(AppContext)

    const getMantenimientos = async () => {
        setIsLoading(true)
        if (mantenimientosAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: IMantenimientoDB[] = await res.json()

            const mantenimientoArray: IMantenimientoLocal[] = Object.values(data)
                .map((mantenimiento: IMantenimientoDB) => new MantenimientoGetAdapter(mantenimiento))
            setMantenimientosAppContext!(mantenimientoArray)
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    const createMantenimiento = async (mantenimiento: IMantenimientoDB) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, mantenimiento)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getMantenimientos()
        setIsLoading(false)
    }
    const updateMantenimiento = async (id: string, mantenimiento: Partial<IMantenimientoLocal>) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, mantenimiento)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getMantenimientos()
        setIsLoading(false)
    }

    const deleteMantenimiento = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getMantenimientos()
        setIsLoading(false);
    };

    return {
        isLoading,
        getMantenimientos,
        createMantenimiento,
        deleteMantenimiento,
        updateMantenimiento
    }
}