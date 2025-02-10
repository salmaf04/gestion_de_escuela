import {useContext, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import {ProfesorDB, ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {getProfesorCreateDbFromAdapter} from "../utils/utils.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";
import {IValorationCreate} from "../models/IValorationCreate.ts";
import {ISancionCreate} from "../models/ISancionCreate.ts";
import {useApiAsignatura} from "../../asignaturas/hooks/useApiAsignatura.ts";

const endpoint = EndpointEnum.PROFESORES

export const useApiProfesor = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, profesores: profesoresAppContext, setProfesores: setProfesoresAppContext, setMessage} = useContext(AppContext)
    const [profesor, setProfesor] = useState<ProfesorGetAdapter>()
    const getProfesores = async () => {
        setIsLoading(true)
        if (profesoresAppContext) {
            setIsLoading(false)
        }
         const res = await apiRequest.getApi(endpoint)
         if (res.ok) {
             const data: ProfesorGetResponse = await res.json()
             const profesorArray = Object.values(data)
                 .map((profesor: ProfesorDB) => new ProfesorGetAdapter(profesor))
             setProfesoresAppContext!(profesorArray)
         } else {
             setError!(new Error(res.statusText))
         }
        setIsLoading(false)
    }

    const createProfesor = async (profesor: ProfesorCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, getProfesorCreateDbFromAdapter(profesor))
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getProfesores()
        setIsLoading(false)
    }
    const updateProfesor = async (id: string, profesor: ProfesorCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, profesor)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getProfesores()
        setIsLoading(false)
    }

    const deleteProfesor = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (res.ok)
            setMessage!('Profesor eliminado correctamente')
        else
            setError!(new Error(res.statusText));
        await getProfesores()
        setIsLoading(false);
    };

    const valorarProfesor = async (valoracion: IValorationCreate) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(EndpointEnum.VALORATION, valoracion);
        if (!res.ok)
            setError!(new Error(res.statusText));
        else
            setMessage!("Solicitud enviada correctamente")
        await getProfesores()
        setIsLoading(false);
    };
    const sancionarProfesor = async (data: ISancionCreate) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(EndpointEnum.SANCION, data);
        if (!res.ok)
            setError!(new Error(res.statusText));
        else
            setMessage!("Solicitud enviada correctamente")
        await getProfesores()
        setIsLoading(false);
    };

    const getProfesor = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.getApi(endpoint, getQueryParamsFromObject({id: id}));
        if (res.ok){
            const data: ProfesorDB[] = await res.json()
            setProfesor(new ProfesorGetAdapter(data[0]))
        }
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getProfesores()
        setIsLoading(false);
    };


    return {
        isLoading,
        getProfesores,
        createProfesor,
        deleteProfesor,
        updateProfesor,
        valorarProfesor,
        getProfesor,
        profesor,
        sancionarProfesor
    }
}