import {useContext, useState} from "react"
import aulaApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";
import {AulaCreateAdapter} from "../adapters/AulaCreateAdapter.ts";
import {AulaCreateDto} from "../models/AulaCreateDto.ts";

export const useCreateAula = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [newAula, setNewAula] = useState<AulaCreateAdapter>()
    const {setError} = useContext(AppContext)

    const createAula = async (aula: AulaCreateAdapter) => {

        setIsLoading(true)
        const res = await aulaApi.postAula(aula)
        if (res.ok) {
            const data: AulaCreateDto = await res.json()
            setNewAula(new AulaCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        newAula,
        createAula,
    }
}