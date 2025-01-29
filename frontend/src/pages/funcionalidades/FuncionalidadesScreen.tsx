import { useApiFuncionalidades } from "./hooks/useApiFuncionalidades.ts";
import Table from "./components/Table.tsx";

function FuncionalidadesScreen() {
    const { profesores } = useApiFuncionalidades();
    const {filtrodeMantenimento } = useApiFuncionalidades();



    const profesor_Esp_headers = ['name', 'specialty', 'mean', 'state'];
    const  profesor_Esp_showHeaders = ['Nombre', 'Especialidad', 'Medio', 'Estado'];
    const filtrodemantenimiento_headers = ['classroom_id', 'other', 'teaching_material', 'technological_mean', 'total maintenances after two years']

    const filtrodemantenimiento_showHeaders = ['ID de aula', 'Otro', 'Material de enseñanza', 'Medio tecnológico', 'Total'];
    console.log(filtrodeMantenimento)


    return (
        <div>
            <h1>Funcionalidad 1 </h1>
            <Table headers={profesor_Esp_headers} items={profesores} showHeaders={profesor_Esp_showHeaders} />
            <h1>Funcionalidad 2 </h1>
            <Table headers = {filtrodemantenimiento_headers} items={filtrodeMantenimento} showHeaders={filtrodemantenimiento_showHeaders} />


        </div>

    );
}

export default FuncionalidadesScreen;