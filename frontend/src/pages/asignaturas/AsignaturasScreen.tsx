// frontend/src/pages/asignaturas/AsignaturasScreen.tsx
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

interface IAsignaturaContext {
    searchText?: string;
    dataTable?: IAsignaturaTableRow[];
    edittingId?: string;
    showModal?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEdittingId?: (idAsignatura?: string) => void;
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
}

export const AsignaturaContext = createContext<IAsignaturaContext>({});

export default function AsignaturasScreen() {
    const [searchText, setSearchText] = useState('');
    const [edittingId, setEdittingId] = useState<string | undefined>(); //id del elemento que se esta editando
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {asignaturas, aulas} = useContext(AppContext)
    const {getAulas} = useApiAulas()
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
    }, []);

    const onDeleteTableItem = (deletedAsignaturaId: string) => {
        deleteAsignatura(deletedAsignaturaId);
    };

    const onEditTableItem = (asignaturaEdit: AsignaturaCreateAdapter) => {
        setIsEditing(true);
        updateAsignatura!(edittingId!, asignaturaEdit);
        setEdittingId(undefined)
        setIsEditing(false);
    };

    const onAddTableItem = (asignatura: AsignaturaCreateAdapter) => {
        setIsCreating(true);
        createAsignatura(asignatura);
        setIsCreating(false);
    };

    const [dataTable, setDataTable] = useState<IAsignaturaTableRow[]>([])

    const data = useMemo<IAsignaturaTableRow[]>(() => {
        return asignaturas?.map((item) => {
            return {
                id: item!.id,
                name: item.name ?? "Desconocido",
                hourly_load: item.hourly_load ?? 0,
                study_program: item.study_program ?? 0,
                classroom_name: aulas?.find((i) => i.id === item.classroom_id)?.location ?? "Desconocido",
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
            edittingId: edittingId,
            showModal: showModal,
            isCreatting: isCreating,
            isEditting: isEditing,
            setShowModal: setShowModal,
            setEdittingId: setEdittingId,
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
                {(showModal || edittingId) &&
                    <AddAsignaturaForm />
                }
            </div>
        </AsignaturaContext.Provider>
    );
}