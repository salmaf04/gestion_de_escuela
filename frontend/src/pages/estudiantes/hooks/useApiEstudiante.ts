import {useContext, useState} from "react";
import {EstudianteGetAdapter} from "../adapters/EstudianteGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {IEstudianteDB} from "../models/IEstudianteDB.ts";
import {IEstudianteLocal} from "../models/IEstudianteLocal.ts";
import {useApiCurso} from "../../cursos/hooks/useApiCurso.ts";
import {IEstudianteCreateDB} from "../models/IEstudianteCreateDB.ts";

const endpoint = EndpointEnum.ESTUDIANTES

export const useApiEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {getCursos} = useApiCurso()
    const {setError, estudiantes: estudiantesAppContext, setEstudiantes: setEstudiantesAppContext, cursos} = useContext(AppContext)

    const getEstudiantes = async () => {
        setIsLoading(true)
        if (estudiantesAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            await getCursos()
            const data: IEstudianteDB[] = await res.json()
            const estudianteArray: IEstudianteLocal[] = Object.values(data)
                .map((estudiante: IEstudianteDB) => new EstudianteGetAdapter(estudiante, cursos!.find((item)=> item.id === estudiante.course_id)!))
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

    return {
        isLoading,
        getEstudiantes,
        createEstudiante,
        deleteEstudiante,
        updateEstudiante
    }
}