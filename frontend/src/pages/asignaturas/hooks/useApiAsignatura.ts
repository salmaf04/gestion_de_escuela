import {useContext, useState} from "react";
import {AsignaturaGetAdapter} from "../adapters/AsignaturaGetAdapter.ts";
import {AsignaturaGetDB, AsignaturaGetResponse} from "../models/AsignaturaGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {AsignaturaCreateAdapter} from "../adapters/AsignaturaCreateAdapter.ts";
import {useApiCurso} from "../../cursos/hooks/useApiCurso.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";

const endpoint = EndpointEnum.ASIGNATURAS

export const useApiAsignatura = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, asignaturas: asignaturasAppContext, setAsignaturas: setAsignaturasAppContext, cursos} = useContext(AppContext)
    const {getCursos} = useApiCurso()

    const getAsignaturas = async () => {
        setIsLoading(true)
        if (asignaturasAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        getCursos()
        if (res.ok) {
            const data: AsignaturaGetResponse = await res.json()
            const asignaturaArray = Object.values(data)
                .map((asignatura: AsignaturaGetDB) => new AsignaturaGetAdapter(asignatura, cursos!.find((item) => item.id === asignatura.course_id)!))
            setAsignaturasAppContext!(asignaturaArray)
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    const createAsignatura = async (asignatura: AsignaturaCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, asignatura)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getAsignaturas()
        setIsLoading(false)
    }
    const updateAsignatura = async (id: string, asignatura: Partial<AsignaturaCreateAdapter>) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, {}, getQueryParamsFromObject(asignatura))
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getAsignaturas()
        setIsLoading(false)
    }

    const deleteAsignatura = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getAsignaturas()
        setIsLoading(false);
    };

    return {
        isLoading,
        getAsignaturas,
        createAsignatura,
        deleteAsignatura,
        updateAsignatura
    }
}