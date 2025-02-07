// frontend/src/pages/secretarias/hooks/useApiAusencias.ts
import { useContext, useState } from "react";
import { AppContext } from "../../../App.tsx";
import apiRequest from "../../../api/apiRequest.ts";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";
import {ISecretariaDB} from "../models/ISecretariaDB.ts";

const endpoint = EndpointEnum.SECRETARY;

export const useApiSecretaria = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [secretarias, setSecretarias] = useState<ISecretariaDB[]>();
    const [secretaria, setSecretaria] = useState<ISecretariaDB>()

    const { setError, secretarias: secretariasAppContext, setSecretarias: setSecretariasAppContext } = useContext(AppContext);

    const getSecretarias = async () => {
        setIsLoading(true);
        if (secretariasAppContext)
            setSecretarias(secretariasAppContext);

        const res = await apiRequest.getApi(endpoint);
        if (res.ok) {
            const data: ISecretariaDB[] = await res.json();
            setSecretarias(data);
            setSecretariasAppContext!(data);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    const createSecretaria = async (secretaria: Partial<ISecretariaDB>) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, secretaria);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateSecretaria = async (id: string, secretaria: Partial<ISecretariaDB>) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, id, {}, getQueryParamsFromObject(secretaria))
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const deleteSecretaria = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const getSecretaria = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.getApi(endpoint, getQueryParamsFromObject({id: id}));
        if (res.ok){
            const data: ISecretariaDB[] = await res.json()
            setSecretaria(data[0])
        }
        else
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        secretarias,
        isLoading,
        getSecretarias,
        createSecretaria,
        deleteSecretaria,
        updateSecretaria,
        getSecretaria,
        secretaria
    };
};