import {useContext, useState} from "react";
import medioApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";
import {MedioGetAdapter} from "../adapters/MedioGetAdapter.ts";
import {MedioDB, MedioGetResponse} from "../models/MedioGetResponse.ts";

export const useGetMedios = () => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [medios, setMedios] = useState<MedioGetResponse[]>()
    const {setError} = useContext(AppContext)


    const getMedios = async () => {
        setIsGetLoading(true)
        const res = await medioApi.getMedios()
        if (res.ok) {
            const data: MedioGetResponse = await res.json()

            setMedios(Object.values(data)
                .map((medio: MedioDB) => new MedioGetAdapter(medio)))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        medios,
        getMedios,
    }
}