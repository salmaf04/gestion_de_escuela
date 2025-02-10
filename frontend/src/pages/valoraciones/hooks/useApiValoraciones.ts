import { useState, useEffect, useContext } from "react";
import { EndpointEnum } from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";

import { AppContext } from "../../../App.tsx";
import { ValoracionPorAsignaturadeProfesorGetAdapter } from "../adapters/ValoracionPromediodeProfesorGetAdapter.ts";
import { ValoracionPorAsignaturaDeProfesorGetDB } from "../models/models.ts";

const valoracionPorAsignaturaDeProfesorEndpoint = EndpointEnum.VALORATION;

export const useApiValoraciones = () => {
    const [valoraciones, setValoraciones] = useState<ValoracionPorAsignaturadeProfesorGetAdapter[]>([]);
    const { setError } = useContext(AppContext);

    const getValoracionesdeProfesores = async () => {
        const res = await apiRequest.getApi(valoracionPorAsignaturaDeProfesorEndpoint);
        if (res.ok) {
            const data: ValoracionPorAsignaturaDeProfesorGetDB[] = await res.json();
            const valoracionesArray = data.map((valoracion: ValoracionPorAsignaturaDeProfesorGetDB) => new ValoracionPorAsignaturadeProfesorGetAdapter(valoracion));
            setValoraciones(valoracionesArray);
        } else {
            setError!(new Error(res.statusText));
        }
    };

    useEffect(() => {
        getValoracionesdeProfesores();
    }, []);

    return { valoraciones };
};