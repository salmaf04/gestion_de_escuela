import { useState, useEffect, useContext } from "react";
import { EndpointEnum } from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";

import { AppContext } from "../../../App.tsx";
import { ProfesorEspGetDB, FiltrodeMantenimientoGetDB, CostoPromedioGetDB, ValoracionPromediodeProfesorGetDB, ValoracionPromediodeEstudianteGetDB, SalariosdeProfesoresGetDB } from "../models/models.ts";
import { ProfesorEspGetAdapter } from "../adapters/ProfesorEspGetAdapter.ts";
import { FiltrodeMantenimientoGetAdapter } from "../adapters/FiltrodeMantenimientoGetAdapter.ts";
import { CostoPromedioGetAdapter } from "../adapters/CostoPromedioGetAdapter.ts";
import { ValoracionPromediodeProfesorGetAdapter } from "../adapters/ValoracionPromediodeProfesorGetAdapter.ts";
import { ValoracionPromediodeEstudianteGetAdapter } from "../adapters/ValoracionPromediodeEstudianteGetAdapter.ts";
import {SalariosdeProfesoresGetAdapter} from "../adapters/SalariosdeProfesorGetAdapter.ts"

const profesorEndpoint = EndpointEnum.ESP_PROFESOR;
const filtrodeMantenimentoEndpoint = EndpointEnum.FILTRO_DE_MANTENIMENTO;
const costoPromedioEndpoint = EndpointEnum.COSTO_PROMEDIO;
const valoracionPromedioProfesorEndpoint = EndpointEnum.VALORACION_PROMEDIO_PROFESOR;
const valoracionPromedioEstudianteEndpoint = EndpointEnum.VALORACION_PROMEDIO_ESTUDIANTE;
const salariosProfesoresEndpoint = EndpointEnum.SALARIOS_PROFESORES;

export const useApiFuncionalidades = () => {
    const [profesores, setProfesores] = useState<ProfesorEspGetAdapter[]>([]);
    const [filtrodeMantenimento, setfiltrodeMantenimento] = useState<FiltrodeMantenimientoGetAdapter[]>([]);
    const [costoPromedio, setCostoPromedio] = useState<CostoPromedioGetAdapter[]>([]);
    const [valoracionPromedioProfesor, setValoracionPromedioProfesor] = useState<ValoracionPromediodeProfesorGetAdapter[]>([]);
    const [valoracionPromedioEstudiante, setValoracionPromedioEstudiante] = useState<ValoracionPromediodeEstudianteGetAdapter[]>([]);
    const [salariosProfesores, setSalariosProfesores] = useState<SalariosdeProfesoresGetAdapter[]>([]);
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

    const getFiltrodeMantenimiento = async () => {
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

    const getValoracionPromedioProfesor = async () => {
        const res = await apiRequest.getApi(valoracionPromedioProfesorEndpoint);
        if (res.ok) {
            const data: ValoracionPromediodeProfesorGetDB[] = await res.json();
            const valoracionPromedioProfesorArray = data.map(item => new ValoracionPromediodeProfesorGetAdapter(item));
            setValoracionPromedioProfesor(valoracionPromedioProfesorArray);
        } else {
            setError!(new Error(res.statusText));
        }
    };

    const getValoracionPromedioEstudiante = async () => {
        const res = await apiRequest.getApi(valoracionPromedioEstudianteEndpoint);
        if (res.ok) {
            const data: ValoracionPromediodeEstudianteGetDB[] = await res.json();
            const valoracionPromedioEstudianteArray = data.map(item => new ValoracionPromediodeEstudianteGetAdapter(item));
            setValoracionPromedioEstudiante(valoracionPromedioEstudianteArray);
        } else {
            setError!(new Error(res.statusText));
        }
    };

    const getSalariosProfesores = async () => {
        const res = await apiRequest.getApi(salariosProfesoresEndpoint);
        if (res.ok) {
            const data: SalariosdeProfesoresGetDB[] = await res.json();
            const salariosProfesoresArray = data.map(item => new SalariosdeProfesoresGetAdapter(item));
            setSalariosProfesores(salariosProfesoresArray);
        } else {
            setError!(new Error(res.statusText));
        }
    };

    useEffect(() => {
        getEspProfesores();
        getFiltrodeMantenimiento();
        getCostoPromedio();
        getValoracionPromedioProfesor();
        getValoracionPromedioEstudiante();
        getSalariosProfesores();
    }, []);

    return { profesores, filtrodeMantenimento, costoPromedio, valoracionPromedioProfesor, valoracionPromedioEstudiante, salariosProfesores };
};