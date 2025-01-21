import {useContext, useState} from "react"
import medioApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";
import {MedioCreateAdapter} from "../adapters/MedioCreateAdapter.ts";
import {MedioCreateDto} from "../models/MedioCreateDto.ts";

export const useCreateMedio = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [newMedio, setNewMedio] = useState<MedioCreateAdapter>()
    const {setError} = useContext(AppContext)

    const createMedio = async (medio: MedioCreateAdapter) => {

        setIsLoading(true)
        const res = await medioApi.postMedio(medio)
        if (res.ok) {
            const data: MedioCreateDto = await res.json()
            setNewMedio(new MedioCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        newMedio,
        createMedio,
    }
}