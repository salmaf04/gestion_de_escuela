import {useContext, useState} from "react";
import {ICursoGetDB} from "../models/ICursoGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {ICursoCreateDB} from "../models/ICursoCreateDB.ts";

const endpoint = EndpointEnum.CURSOS

export const useApiCurso = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, cursos: cursosAppContext, setCursos: setCursosAppContext} = useContext(AppContext)

    const getCursos = async () => {
        setIsLoading(true)
        if (cursosAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: ICursoGetDB[] = await res.json()
            const cursoArray = Object.values(data)
                .map((curso: ICursoGetDB) => curso)
            setCursosAppContext!(cursoArray)
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    const createCurso = async (curso: ICursoCreateDB) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, curso)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getCursos()
        setIsLoading(false)
    }
    const updateCurso = async (id: string, curso: Partial<ICursoCreateDB>) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, curso)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getCursos()
        setIsLoading(false)
    }

    const deleteCurso = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getCursos()
        setIsLoading(false);
    };

    return {
        isLoading,
        getCursos,
        createCurso,
        deleteCurso,
        updateCurso
    }
}