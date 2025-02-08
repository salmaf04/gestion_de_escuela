import {useContext, useState} from "react";
import {EstudianteGetAdapter} from "../adapters/EstudianteGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {IEstudianteDB} from "../models/IEstudianteDB.ts";
import {IEstudianteLocal} from "../models/IEstudianteLocal.ts";
import {useApiCurso} from "../../cursos/hooks/useApiCurso.ts";
import {IEstudianteCreateDB} from "../models/IEstudianteCreateDB.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";
const endpoint = EndpointEnum.ESTUDIANTES

export const useApiEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {getCursos} = useApiCurso()
    const {setError, estudiantes: estudiantesAppContext, setEstudiantes: setEstudiantesAppContext} = useContext(AppContext)
    const [estudiante, setEstudiante] = useState<IEstudianteLocal>()
    const getEstudiantes = async () => {
        setIsLoading(true)
        if (estudiantesAppContext) {
            setIsLoading(false)
        }
        await getCursos()
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: IEstudianteDB[] = await res.json()
            const estudianteArray: IEstudianteLocal[] = Object.values(data)
                .map((estudiante: IEstudianteDB) => new EstudianteGetAdapter(estudiante))
            setEstudiantesAppContext!(estudianteArray)
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    const createEstudiante = async (estudiante: Partial<IEstudianteCreateDB>) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, estudiante)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getEstudiantes()
        setIsLoading(false)
    }
    const updateEstudiante = async (id: string, estudiante: Partial<IEstudianteDB>) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, estudiante)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getEstudiantes()
        setIsLoading(false)
    }

    const deleteEstudiante = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getEstudiantes()
        setIsLoading(false);
    };

    const getEstudiante = async (id: string) => {
        setIsLoading(true);
        await getCursos()
        const res = await apiRequest.getApi(endpoint, getQueryParamsFromObject({id: id}));
        if (res.ok){
            const data: IEstudianteDB[] = await res.json()
            setEstudiante(new EstudianteGetAdapter(data[0]))
        }
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getEstudiantes()
        setIsLoading(false);
    };

    return {
        isLoading,
        getEstudiantes,
        createEstudiante,
        deleteEstudiante,
        updateEstudiante,
        getEstudiante,
        estudiante
    }
}