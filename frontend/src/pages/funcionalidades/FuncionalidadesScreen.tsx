// `frontend/src/pages/funcionalidades/FuncionalidadesScreen.tsx`
import { useApiFuncionalidades } from "./hooks/useApiFuncionalidades.ts";
import Table from "./components/Table.tsx";

function FuncionalidadesScreen() {
    const { profesores, filtrodeMantenimento, costoPromedio, valoracionPromedioProfesor, valoracionPromedioEstudiante, salariosProfesores } = useApiFuncionalidades();

    const profesor_Esp_headers = ['name', 'specialty', 'mean', 'state'];
    const profesor_Esp_showHeaders = ['Nombre', 'Especialidad', 'Medio', 'Estado'];
    const filtrodemantenimiento_headers = ['classroom_id', 'other', 'teaching_material', 'technological_mean', 'total maintenances after two years'];
    const filtrodemantenimiento_showHeaders = ['ID de aula', 'Otro', 'Material de enseñanza', 'Medio tecnológico', 'Total'];
    const costoPromedio_headers = ['average_cost', 'mean_id', 'mean_name'];
    const costoPromedio_showHeaders = ['Costo Promedio', 'ID del Medio', 'Nombre del Medio'];
    const valoracionPromedioProfesor_headers = ['name', 'average_valoration', 'subjects'];
    const valoracionPromedioProfesor_showHeaders = ['Nombre', 'Valoración Promedio', 'Asignaturas'];
    const valoracionPromedioEstudiante_headers = ['name', 'student_id', 'teacher_name', 'teacher_valoration'];
    const valoracionPromedioEstudiante_showHeaders = ['Nombre', 'ID del Estudiante', 'Nombre del Profesor', 'Valoración del Profesor'];
    const salariosProfesores_headers = ['name', 'valorations', 'date', 'means'];
    const salariosProfesores_showHeaders = ['Nombre', 'Valoraciones', 'Fecha', 'Medios'];

    return (
        <div>
            <h1>Funcionalidad 1</h1>
            <Table headers={profesor_Esp_headers} items={profesores} showHeaders={profesor_Esp_showHeaders} />
            <h1>Funcionalidad 2</h1>
            <Table headers={filtrodemantenimiento_headers} items={filtrodeMantenimento} showHeaders={filtrodemantenimiento_showHeaders} />
            <h1>Funcionalidad 3</h1>
            <Table headers={costoPromedio_headers} items={costoPromedio} showHeaders={costoPromedio_showHeaders} />
            <h1>Funcionalidad 4</h1>
            <Table headers={valoracionPromedioProfesor_headers} items={valoracionPromedioProfesor} showHeaders={valoracionPromedioProfesor_showHeaders} />
            <h1>Funcionalidad 5</h1>
            <Table headers={valoracionPromedioEstudiante_headers} items={valoracionPromedioEstudiante} showHeaders={valoracionPromedioEstudiante_showHeaders} />
            <h1>Funcionalidad 6</h1>
            <Table headers={salariosProfesores_headers} items={salariosProfesores} showHeaders={salariosProfesores_showHeaders} />
        </div>
    );
}

export default FuncionalidadesScreen;