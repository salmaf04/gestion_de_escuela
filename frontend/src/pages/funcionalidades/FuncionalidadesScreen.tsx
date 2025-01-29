import { useApiFuncionalidades } from "./hooks/useApiFuncionalidades.ts";
import ProfesoresEsp_Table from "./components/ProfesoresEsp_Table.tsx";

function FuncionalidadesScreen() {
    const { profesores } = useApiFuncionalidades();

    console.log(profesores);
    return (
        <div>
            <h1>Funcionalidad 1 </h1>
            <ProfesoresEsp_Table profesores={profesores}/>
        </div>

    );
}

export default FuncionalidadesScreen;