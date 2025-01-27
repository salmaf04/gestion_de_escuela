// frontend/src/pages/notas/hooks/useApiNotas.ts
import { useContext, useState } from "react";
import { INotaDB } from "../models/INotaDB.ts";
import { AppContext } from "../../../App.tsx";
import apiRequest from "../../../api/apiRequest.ts";
import { getNotaCreateDbFromAdapter } from "../utils/utils.ts";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";
import {useApiAsignatura} from "../../asignaturas/hooks/useApiAsignatura.ts";
import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {INotaLocal} from "../models/INotaLocal.ts";
import {NotaAdapter} from "../adapters/NotaAdapter.ts";

const endpoint = EndpointEnum.NOTAS;

export const useApiNotas = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [notas, setNotas] = useState<INotaLocal[]>();
    const {getEstudiantes} = useApiEstudiante()
    const {getAsignaturas} = useApiAsignatura()
    const {getProfesores} = useApiProfesor()



    const { setError, notas: notasAppContext, setNotas: setNotasAppContext, profesores, asignaturas, estudiantes } = useContext(AppContext);

    const getNotas = async () => {
        setIsLoading(true);
        if (notasAppContext)
            setNotas(notasAppContext);
        else {
            await getProfesores()
            await getEstudiantes()
            await getAsignaturas()
            const res = await apiRequest.getApi(endpoint);
            if (res.ok) {
                const data: INotaDB[] = await res.json();
                const notaArray: INotaLocal[] = Object.values(data)
                    .map((nota: INotaDB) => {
                        return new NotaAdapter(
                            nota,
                            estudiantes!.find((estudiante) => estudiante.id === nota.student_id)!,
                            asignaturas!.find((asignatura) => asignatura.id === nota.subject_id)!,
                            profesores!.find((profesor) => profesor.id === nota.teacher_id)!,
                    )

                    });
                setNotas(notaArray);
                setNotasAppContext!(notaArray);
            } else {
                setError!(new Error(res.statusText));
            }
        }
        setIsLoading(false);
    };

    const createNota = async (nota: Partial<INotaDB>) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, getNotaCreateDbFromAdapter(nota));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateNota = async (id: string, nota: Partial<INotaDB>) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, id ,getNotaCreateDbFromAdapter(nota));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const deleteNota = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        notas,
        isLoading,
        getNotas,
        createNota,
        deleteNota,
        updateNota
    };
};