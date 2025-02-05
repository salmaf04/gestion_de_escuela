// frontend/src/pages/ausencias/hooks/useApiAusencias.ts
import { useContext, useState } from "react";
import { IAusenciaDB } from "../models/IAusenciaDB.ts";
import { AppContext } from "../../../App.tsx";
import apiRequest from "../../../api/apiRequest.ts";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";
import {useApiAsignatura} from "../../asignaturas/hooks/useApiAsignatura.ts";
import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {IAusenciaLocal} from "../models/IAusenciaLocal.ts";
import {AusenciaAdapter} from "../adapters/AusenciaAdapter.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";

const endpoint = EndpointEnum.AUSENCIAS;

export const useApiAusencias = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [ausencias, setAusencias] = useState<IAusenciaLocal[]>();
    const {getEstudiantes} = useApiEstudiante()
    const {getAsignaturas} = useApiAsignatura()
    const {getProfesores} = useApiProfesor()



    const { setError, ausencias: ausenciasAppContext, setAusencias: setAusenciasAppContext, asignaturas, estudiantes } = useContext(AppContext);

    const getAusencias = async () => {
        setIsLoading(true);
        if (ausenciasAppContext)
            setAusencias(ausenciasAppContext);

        await getProfesores()
        await getEstudiantes()
        await getAsignaturas()
        const res = await apiRequest.getApi(endpoint);
        if (res.ok) {
            const data: IAusenciaDB[] = await res.json();
            const ausenciaArray: IAusenciaLocal[] = Object.values(data)
                .map((ausencia: IAusenciaDB) => {
                    return new AusenciaAdapter(
                        ausencia,
                        estudiantes!.find((estudiante) => estudiante.id === ausencia.student_id)!,
                        asignaturas!.find((asignatura) => asignatura.id === ausencia.subject_id)!)

                });
            setAusencias(ausenciaArray);
            setAusenciasAppContext!(ausenciaArray);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    const createAusencia = async (ausencia: Partial<IAusenciaDB>) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, ausencia);
        if (!res.ok)
            setError!(new Error(res.statusText));
        getAusencias()
        setIsLoading(false);
    };

    const updateAusencia = async (id: string, ausencia: Partial<IAusenciaDB>) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, id, {}, getQueryParamsFromObject(ausencia))
        if (!res.ok)
            setError!(new Error(res.statusText));
        getAusencias()
        setIsLoading(false);
    };

    const deleteAusencia = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        getAusencias()
        setIsLoading(false);
    };

    return {
        ausencias,
        isLoading,
        getAusencias,
        createAusencia,
        deleteAusencia,
        updateAusencia
    };
};