import { useApiValoraciones } from "./hooks/useApiValoraciones.ts";
import Table from "./components/Table.tsx";
import ExportFuncionalidadesButton from "../../components/ExportFuncionalidadesButton.tsx";
import { FiltrodeMantenimientoGetDB, CostoPromedioGetDB, ValoracionPromediodeProfesorGetDB, ValoracionPromediodeEstudianteGetDB, SalariosdeProfesoresGetDB } from "../../models/models.ts";
import {ValoracionPorAsignaturadeProfesorGetAdapter} from "./adapters/ValoracionPromediodeProfesorGetAdapter.ts";
import SearchInput from "../../components/SearchInput.tsx";
import ExportButton from "../../components/ExportButton.tsx";
import {MedioGetAdapter} from "../medios/adapters/MedioGetAdapter.ts";
import {RolesEnum} from "../../api/RolesEnum.ts";
import AddButton from "../../components/AddButton.tsx";

type Adapter = ValoracionPorAsignaturadeProfesorGetAdapter | FiltrodeMantenimientoGetDB | CostoPromedioGetDB | ValoracionPromediodeProfesorGetDB | ValoracionPromediodeEstudianteGetDB | SalariosdeProfesoresGetDB;

function ValoracionesScreen() {
    const {
        valoraciones

    } = useApiValoraciones();
    console.log(valoraciones)

    const data: { title: string, headers: string[], showHeaders: string[], items: Adapter[] }[] = [
        {

            title: 'Valoración de Profesores',
            headers: ['teacherName', 'teacherLastname', 'subjectName', 'courseYear' , 'valoration'],
            showHeaders: ['Nombre', 'Apellido', 'Asignatura', 'Año' , 'Valoracion'],
            items: valoraciones
        },
    ];

    return (
        <div className={'h-dvh flex flex-col m2 px-6 overflow-y-scroll py-20'}>

            <div>
                <div className={'my-4 flex justify-around'}>
                    <h1 className={' my-2 font-bold text-xl text-center'}>{data[0].title}</h1>
                    <ExportFuncionalidadesButton  data={data} options={data.map(option => option.title)}/>
                </div>

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
            </div>

        </div>
    );
}

export default ValoracionesScreen;