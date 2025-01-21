import {useContext, useState} from "react";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import {ProfesorDB, ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointType} from "../../../api/EndpointType.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {getProfesorCreateDbFromAdapter} from "../utils/utils.ts";

const endpoint = EndpointType.PROFESORES

export const useApiProfesor = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [profesores, setProfesores] = useState<ProfesorGetAdapter[]>()
    const {setError, profesores: profesoresAppContext, setProfesores: setProfesoresAppContext} = useContext(AppContext)

    const getProfesores = async () => {
        setIsLoading(true)
        if (profesoresAppContext)
            setProfesores(profesoresAppContext)
        else {
            const res = await apiRequest.getApi(endpoint)
            if (res.ok) {
                const data: ProfesorGetResponse = await res.json()
                const profesorArray = Object.values(data)
                    .map((profesor: ProfesorDB) => new ProfesorGetAdapter(profesor))
                setProfesores(profesorArray)
                setProfesoresAppContext!(profesorArray)
            } else {
                setError!(new Error(res.statusText))
            }
        }
        setIsLoading(false)
    }

    const createProfesor = async (profesor: ProfesorCreateAdapter) => {
        setIsLoading(true)
        console.log(profesor)
        const res = await apiRequest.postApi(endpoint, getProfesorCreateDbFromAdapter(profesor))
        if (!res.ok)
            setError!(new Error(res.statusText))
        setIsLoading(false)
    }
    const updateProfesor = async (profesor: ProfesorCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, getProfesorCreateDbFromAdapter(profesor))
        if (!res.ok)
            setError!(new Error(res.statusText))
        setIsLoading(false)
    }

    const deleteProfesor = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        profesores,
        isLoading,
        getProfesores,
        createProfesor,
        deleteProfesor,
        updateProfesor
    }
}