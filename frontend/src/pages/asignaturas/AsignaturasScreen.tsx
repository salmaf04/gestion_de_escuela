// frontend/src/pages/asignaturas/CursosScreen.tsx
import {createContext, useContext, useEffect, useMemo, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { AsignaturaCreateAdapter } from "./adapters/AsignaturaCreateAdapter.ts";
import AddAsignaturaForm from "./components/AddAsignaturaForm.tsx";
import { useApiAsignatura } from "./hooks/useApiAsignatura.ts";
import {AppContext} from "../../App.tsx";
import {AulaGetAdapter} from "../aulas/adapters/AulaGetAdapter.ts";
import {DBObject} from "../../types.ts";
import {AsignaturaGetAdapter} from "./adapters/AsignaturaGetAdapter.ts";
import {useApiAulas} from "../aulas/hooks/useApiAulas.ts";
import {useApiCurso} from "../cursos/hooks/useApiCurso.ts";

interface IAsignaturaContext {
    searchText?: string;
    dataTable?: IAsignaturaTableRow[];
    editting?: IAsignaturaTableRow;
    showModal?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (idAsignatura?: IAsignaturaTableRow) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (asignaturaEdit: AsignaturaCreateAdapter) => void;
    onAddTableItem?: (asignaturaEdit: AsignaturaCreateAdapter) => void;
    aulas?: AulaGetAdapter[],
    asignaturas?: AsignaturaGetAdapter[],
    isLoading?: boolean
}

interface IAsignaturaTableRow extends DBObject {
    id: string,
    name: string;
    hourly_load: number;
    classroom_name: string
    study_program: number;
    course_year: number
}

export const AsignaturaContext = createContext<IAsignaturaContext>({});

export default function AsignaturasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IAsignaturaTableRow | undefined>(); //id del elemento que se esta editando
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {asignaturas, aulas} = useContext(AppContext)
    const {getAulas} = useApiAulas()
    const {getCursos} = useApiCurso()
    const {
        deleteAsignatura,
        createAsignatura,
        updateAsignatura,
        getAsignaturas,
        isLoading
    } = useApiAsignatura();

    useEffect(() => {
        getAsignaturas();
        getAulas()
        getCursos()
    }, []);

    const onDeleteTableItem = (deletedAsignaturaId: string) => {
        deleteAsignatura(deletedAsignaturaId);
    };

    const onEditTableItem = (asignaturaEdit: AsignaturaCreateAdapter) => {
        setIsEditing(true);
        updateAsignatura!(editting!.id, asignaturaEdit);
        setEditting(undefined)
        setIsEditing(false);
    };

    const onAddTableItem = (asignatura: AsignaturaCreateAdapter) => {
        setIsCreating(true);
        createAsignatura(asignatura);
        setIsCreating(false);
    };

    const [dataTable, setDataTable] = useState<IAsignaturaTableRow[]>([])
    console.log(asignaturas)
    const data = useMemo<IAsignaturaTableRow[]>(() => {
        return asignaturas?.map((item) => {
            return {
                id: item!.id,
                name: item.name ?? "Desconocido",
                hourly_load: item.hourly_load ?? 0,
                study_program: item.study_program ?? 0,
                classroom_name: `Aula ${item?.classroom?.number ?? "Desconocida"}`,
                course_year: item.course?.year ?? 0
            }
        }) ?? []
    }, [asignaturas]);

    useEffect(() => {

        setDataTable(data)
    }, [asignaturas]);
    useEffect(() => {
        const filteredData = data?.filter((item) => {
            return Object.values(item).some((value) =>
                value?.toString().toLowerCase().includes(searchText.toLowerCase())
            );
        }) ?? [];
        setDataTable(filteredData);
    }, [searchText, asignaturas]);
    return (
        <AsignaturaContext.Provider value={{
            dataTable: dataTable,
            searchText: searchText,
            editting: editting,
            showModal: showModal,
            isCreatting: isCreating,
            isEditting: isEditing,
            setShowModal: setShowModal,
            setEditting: setEditting,
            setSearchText: setSearchText,
            onDeleteTableItem: onDeleteTableItem,
            onEditTableItem: onEditTableItem,
            onAddTableItem: onAddTableItem,
            aulas: aulas,
            asignaturas: asignaturas,
            isLoading: isLoading
        }}>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar />
                <Body />
                {(showModal || editting) &&
                    <AddAsignaturaForm />
                }
            </div>
        </AsignaturaContext.Provider>
    );
}