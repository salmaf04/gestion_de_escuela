import { useApiFuncionalidades } from "./hooks/useApiFuncionalidades.ts";
import Table from "./components/Table.tsx";
import ExportFuncionalidadesButton from "../../components/ExportFuncionalidadesButton.tsx";
import { ProfesorEspGetDB, FiltrodeMantenimientoGetDB, CostoPromedioGetDB, ValoracionPromediodeProfesorGetDB, ValoracionPromediodeEstudianteGetDB, SalariosdeProfesoresGetDB } from "../../models/models.ts";

type Adapter = ProfesorEspGetDB | FiltrodeMantenimientoGetDB | CostoPromedioGetDB | ValoracionPromediodeProfesorGetDB | ValoracionPromediodeEstudianteGetDB | SalariosdeProfesoresGetDB;

function FuncionalidadesScreen() {
    const {
        profesores,
        filtrodeMantenimento,
        costoPromedio,
        valoracionPromedioProfesor,
        valoracionPromedioEstudiante,
        salariosProfesores
    } = useApiFuncionalidades();

    const data: { title: string, headers: string[], showHeaders: string[], items: Adapter[] }[] = [
        {
            title: 'Profesores por Especialidad',
            headers: ['name', 'specialty', 'mean', 'state'],
            showHeaders: ['Nombre', 'Especialidad', 'Medio', 'Estado'],
            items: profesores
        },
        {
            title: 'Mantenimientos',
            headers: ['number', 'other', 'teaching_material', 'technological_mean', 'total_after_two_years'],
            showHeaders: ['Numero de Aula', 'Otro', 'Material de enseñanza', 'Medio tecnológico', 'Total despues de dos años'],
            items: filtrodeMantenimento
        },
        {
            title: 'Costo Promedio de Medios',
            headers: ['mean_name', 'average_cost'],
            showHeaders: ['Nombre del Medio', 'Costo Promedio'],
            items: costoPromedio
        },
        {
            title: 'Valoraciones de Profesores',
            headers: ['name', 'average_valoration', 'subjects'],
            showHeaders: ['Nombre', 'Valoración Promedio', 'Asignaturas'],
            items: valoracionPromedioProfesor
        },
        {
            title: 'Valoraciones de Estudiantes',
            headers: ['name', 'teacher_name', 'teacher_valoration'],
            showHeaders: ['Nombre', 'Nombre del Profesor', 'Valoración del Profesor'],
            items: valoracionPromedioEstudiante
        },
        {
            title: 'Sanciones de Profesores',
            headers: ['name', 'valorations', 'date', 'means'],
            showHeaders: ['Nombre', 'Valoraciones', 'Fecha', 'Medios'],
            items: salariosProfesores
        }
    ];

    return (
        <div className={' flex flex-col m2 px-6'}>
           <div>
                {data.map((section, index) => (
                    <Table
                        key={index}
                        title={section.title}
                        headers={section.headers}
                        items={section.items}
                        showHeaders={section.showHeaders}
                    />
                ))}
            </div>
            <ExportFuncionalidadesButton  data={data}  options={data.map(option => option.title)} />

        </div>
    );
}

export default FuncionalidadesScreen;