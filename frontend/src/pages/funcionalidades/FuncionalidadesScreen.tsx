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
    const filtrodemantenimiento_headers = ['number', 'other', 'teaching_material', 'technological_mean', 'total_after_two_years'];
    const filtrodemantenimiento_showHeaders = ['Numero de Aula', 'Otro', 'Material de enseñanza', 'Medio tecnológico', 'Total despues de dos años'];
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
            <Table title={'Profesores por Especialidad'} headers={profesor_Esp_headers} items={profesores} showHeaders={profesor_Esp_showHeaders}/>
            <Table title={'Mantenimientos'} headers={filtrodemantenimiento_headers} items={filtrodeMantenimento}
                   showHeaders={filtrodemantenimiento_showHeaders}/>
            <Table title={'Costo Promedio de Medios'} headers={costoPromedio_headers} items={costoPromedio} showHeaders={costoPromedio_showHeaders}/>
            <Table title={'Valoraciones de Profesores'} headers={valoracionPromedioProfesor_headers} items={valoracionPromedioProfesor}
                   showHeaders={valoracionPromedioProfesor_showHeaders}/>
            <Table title={'Valoraciones de Estiduantes'} headers={valoracionPromedioEstudiante_headers} items={valoracionPromedioEstudiante}
                   showHeaders={valoracionPromedioEstudiante_showHeaders}/>
            <Table title={'Sanciones de Profesores'} headers={salariosProfesores_headers} items={salariosProfesores}
                   showHeaders={salariosProfesores_showHeaders}/>
        </div>
    );
}

export default FuncionalidadesScreen;