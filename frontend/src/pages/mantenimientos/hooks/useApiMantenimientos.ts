import {useContext, useState} from "react";
import {MantenimientoGetAdapter} from "../adapters/MantenimientoGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {IMantenimientoLocal} from "../models/IMantenimientoLocal.ts";
import {useApiMedio} from "../../medios/hooks/useApiMedios.ts";
import {IMantenimientoDB} from "../models/IMantenimientoDB.ts";

const endpoint = EndpointEnum.MANTENIMIENTOS

export const useApiMantenimiento = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, mantenimientos: mantenimientosAppContext, setMantenimientos: setMantenimientosAppContext, medios} = useContext(AppContext)
    const {getMedios} = useApiMedio()

    const getMantenimientos = async () => {
        setIsLoading(true)
        if (mantenimientosAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        await getMedios()
        if (res.ok) {
            const data: IMantenimientoDB[] = await res.json()

            const mantenimientoArray: IMantenimientoLocal[] = Object.values(data)
                .map((mantenimiento: IMantenimientoDB) => new MantenimientoGetAdapter(mantenimiento, medios!.find((item) => item.id === mantenimiento.mean_id)!))
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