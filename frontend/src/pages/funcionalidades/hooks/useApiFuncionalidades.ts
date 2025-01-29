import { useState, useEffect, useContext } from "react";
import { EndpointEnum } from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";

import { AppContext } from "../../../App.tsx";
import {ProfesorEspGetDB} from "../models/models.ts";
import {ProfesorEspGetAdapter} from "../adapters/ProfesorEspGetAdapter.ts";

const endpoint = EndpointEnum.ESP_PROFESOR;

export const useApiFuncionalidades = () => {
    const [profesores, setProfesores] = useState<ProfesorEspGetAdapter[]>([]);
    const { setError } = useContext(AppContext);

    const getEspProfesores = async () => {
        const res = await apiRequest.getApi(endpoint);
        if (res.ok) {
            const data: ProfesorEspGetAdapter[] = await res.json();
            const profesoresArray = Object.values(data).map((profesor: ProfesorEspGetDB) => new ProfesorEspGetAdapter(profesor));
            setProfesores(profesoresArray);
        } else {
            setError!(new Error(res.statusText));
        }
    };

    useEffect(() => {
        getEspProfesores();
    }, []);

    return { profesores };
};