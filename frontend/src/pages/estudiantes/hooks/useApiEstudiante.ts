import {useContext, useState} from "react";
import {EstudianteGetAdapter} from "../adapters/EstudianteGetAdapter.ts";
import {EstudianteGetDB, EstudianteGetResponse} from "../models/EstudianteGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {EstudianteCreateAdapter} from "../adapters/EstudianteCreateAdapter.ts";
import {getEstudianteCreateDbFromAdapter} from "../utils/utils.ts";

const endpoint = EndpointEnum.ESTUDIANTES

export const useApiEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, estudiantes: estudiantesAppContext, setEstudiantes: setEstudiantesAppContext} = useContext(AppContext)

    const getEstudiantes = async () => {
        setIsLoading(true)
        if (estudiantesAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: EstudianteGetResponse = await res.json()
            const estudianteArray = Object.values(data)
                .map((estudiante: EstudianteGetDB) => new EstudianteGetAdapter(estudiante))
            setEstudiantesAppContext!(estudianteArray)
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    const createEstudiante = async (estudiante: EstudianteCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, getEstudianteCreateDbFromAdapter(estudiante))
        if (!res.ok)
            setError!(new Error(res.statusText))
        else
            await getEstudiantes()
        setIsLoading(false)
    }
    const updateEstudiante = async (id: string, estudiante: EstudianteCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, getEstudianteCreateDbFromAdapter(estudiante))
        if (!res.ok)
            setError!(new Error(res.statusText))
        else
            await getEstudiantes()
        setIsLoading(false)
    }

    const deleteEstudiante = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        else
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