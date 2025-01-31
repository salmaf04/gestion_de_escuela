// `frontend/src/pages/funcionalidades/FuncionalidadesScreen.tsx`
import {useApiFuncionalidades} from "./hooks/useApiFuncionalidades.ts";
import Table from "./components/Table.tsx";

function FuncionalidadesScreen() {
    const {
        profesores,
        filtrodeMantenimento,
        costoPromedio,
        valoracionPromedioProfesor,
        valoracionPromedioEstudiante,
        salariosProfesores
    } = useApiFuncionalidades();


    const profesor_Esp_headers = ['name', 'specialty', 'mean', 'state'];
    const profesor_Esp_showHeaders = ['Nombre', 'Especialidad', 'Medio', 'Estado'];
    const filtrodemantenimiento_headers = ['classroom_id', 'other', 'teaching_material', 'technological_mean', 'total maintenances after two years'];
    const filtrodemantenimiento_showHeaders = ['ID de aula', 'Otro', 'Material de enseñanza', 'Medio tecnológico', 'Total'];
    const costoPromedio_headers = [ 'mean_name','average_cost'];
    const costoPromedio_showHeaders = [ 'Nombre del Medio','Costo Promedio'];
    const valoracionPromedioProfesor_headers = ['name', 'average_valoration', 'subjects'];
    const valoracionPromedioProfesor_showHeaders = ['Nombre', 'Valoración Promedio', 'Asignaturas'];
    const valoracionPromedioEstudiante_headers = ['name',  'teacher_name', 'teacher_valoration'];
    const valoracionPromedioEstudiante_showHeaders = ['Nombre', 'Nombre del Profesor', 'Valoración del Profesor'];
    const salariosProfesores_headers = ['name', 'valorations', 'date', 'means'];
    const salariosProfesores_showHeaders = ['Nombre', 'Valoraciones', 'Fecha', 'Medios'];

    return (
        <div>
            <Table headers={profesor_Esp_headers} items={profesores} showHeaders={profesor_Esp_showHeaders}/>
            <Table headers={filtrodemantenimiento_headers} items={filtrodeMantenimento}
                   showHeaders={filtrodemantenimiento_showHeaders}/>
            <Table headers={costoPromedio_headers} items={costoPromedio} showHeaders={costoPromedio_showHeaders}/>
            <Table headers={valoracionPromedioProfesor_headers} items={valoracionPromedioProfesor}
                   showHeaders={valoracionPromedioProfesor_showHeaders}/>
            <Table headers={valoracionPromedioEstudiante_headers} items={valoracionPromedioEstudiante}
                   showHeaders={valoracionPromedioEstudiante_showHeaders}/>
            <Table title={'Sanciones de Profesores'} headers={salariosProfesores_headers} items={salariosProfesores}
                   showHeaders={salariosProfesores_showHeaders}/>
        </div>
    );
}

export default FuncionalidadesScreen;