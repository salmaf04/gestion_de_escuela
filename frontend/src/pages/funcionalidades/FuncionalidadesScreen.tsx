import { useApiFuncionalidades } from "./hooks/useApiFuncionalidades.ts";
import Table from "./components/Table.tsx";

function FuncionalidadesScreen() {
    const { profesores, filtrodeMantenimento, costoPromedio } = useApiFuncionalidades();

    const profesor_Esp_headers = ['name', 'specialty', 'mean', 'state'];
    const profesor_Esp_showHeaders = ['Nombre', 'Especialidad', 'Medio', 'Estado'];
    const filtrodemantenimiento_headers = ['classroom_id', 'other', 'teaching_material', 'technological_mean', 'total maintenances after two years'];
    const filtrodemantenimiento_showHeaders = ['ID de aula', 'Otro', 'Material de enseñanza', 'Medio tecnológico', 'Total'];
    const costoPromedio_headers = ['average_cost', 'mean_id', 'mean_name'];
    const costoPromedio_showHeaders = ['Costo Promedio', 'ID del Medio', 'Nombre del Medio'];
    console.log(costoPromedio)
    return (
        <div>
            <h1>Funcionalidad 1</h1>
            <Table headers={profesor_Esp_headers} items={profesores} showHeaders={profesor_Esp_showHeaders} />
            <h1>Funcionalidad 2</h1>
            <Table headers={filtrodemantenimiento_headers} items={filtrodeMantenimento} showHeaders={filtrodemantenimiento_showHeaders} />
            <h1>Funcionalidad 3</h1>
            <Table headers={costoPromedio_headers} items={costoPromedio} showHeaders={costoPromedio_showHeaders} />
        </div>
    );
}

export default FuncionalidadesScreen;