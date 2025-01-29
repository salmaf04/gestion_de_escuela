import { useState, useEffect, useContext } from "react";
import { EndpointEnum } from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";

import { AppContext } from "../../../App.tsx";
import {ProfesorEspGetDB, FiltrodeMantenimientoGetDB, CostoPromedioGetDB} from "../models/models.ts";
import { ProfesorEspGetAdapter } from "../adapters/ProfesorEspGetAdapter.ts";
import { FiltrodeMantenimientoGetAdapter } from "../adapters/FiltrodeMantenimientoGetAdapter.ts";
import {CostoPromedioGetAdapter} from "../adapters/CostoPromedioGetAdapter.ts";

const profesorEndpoint = EndpointEnum.ESP_PROFESOR;
const filtrodeMantenimentoEndpoint = EndpointEnum.FILTRO_DE_MANTENIMENTO;
const costoPromedioEndpoint = EndpointEnum.COSTO_PROMEDIO;

export const useApiFuncionalidades = () => {
    const [profesores, setProfesores] = useState<ProfesorEspGetAdapter[]>([]);
    const [filtrodeMantenimento, setfiltrodeMantenimento] = useState<FiltrodeMantenimientoGetAdapter[]>([]);
    const [costoPromedio, setCostoPromedio] = useState<CostoPromedioGetAdapter[]>([]);
    const { setError } = useContext(AppContext);

    const getEspProfesores = async () => {
        const res = await apiRequest.getApi(profesorEndpoint);
        if (res.ok) {
            const data: ProfesorEspGetAdapter[] = await res.json();
            const profesoresArray = Object.values(data).map((profesor: ProfesorEspGetDB) => new ProfesorEspGetAdapter(profesor));
            setProfesores(profesoresArray);
        } else {
            setError!(new Error(res.statusText));
        }
    };

   const getFiltrodeMaintenimiento = async () => {
    const res = await apiRequest.getApi(filtrodeMantenimentoEndpoint);
    if (res.ok) {
        const data: FiltrodeMantenimientoGetDB = await res.json();
        const [classrooms, summary] = data;
        const totalMaintenances = summary["total maintenances after two years"];
        const costoPromedioArray = classrooms.map(classroom => new FiltrodeMantenimientoGetAdapter(classroom, totalMaintenances));
        setfiltrodeMantenimento(costoPromedioArray);
    } else {
        setError!(new Error(res.statusText));
    }
};
    const getCostoPromedio = async () => {
        const res = await apiRequest.getApi(costoPromedioEndpoint);
        if (res.ok) {
            const data: CostoPromedioGetDB[] = await res.json();
            const costoPromedioArray = data.map(item => new CostoPromedioGetAdapter(item));
            setCostoPromedio(costoPromedioArray);
        } else {
            setError!(new Error(res.statusText));
        }
    };


    useEffect(() => {
        getEspProfesores();
        getFiltrodeMaintenimiento();
        getCostoPromedio();
    }, []);

    return { profesores, filtrodeMantenimento , costoPromedio };
};