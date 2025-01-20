import {useContext, useState} from "react";
import mediorApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";
import {MedioCreateAdapter} from "../adapters/MedioCreateAdapter.ts";
import {MedioCreateDto} from "../models/MedioCreateDto.ts";

export const useEditMedio = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [editedMedio, setEditedMedio] = useState<MedioCreateAdapter>()
    const {setError} = useContext(AppContext)

    const editMedio = async (medio: MedioCreateAdapter) => {
        setIsLoading(true)
        const res = await mediorApi.putMedio(medio)
        if (res.ok) {
            const data: MedioCreateDto = await res.json()
            setEditedMedio(new MedioCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        editedMedio,
        editMedio,
    }
}