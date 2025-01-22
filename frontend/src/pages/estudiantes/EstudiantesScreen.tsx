import { createContext, useContext, useEffect, useState } from "react";
import { EstudianteGetAdapter } from "./adapters/EstudianteGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { EstudianteCreateAdapter } from "./adapters/EstudianteCreateAdapter.ts";
import { AppContext } from "../../App.tsx";
import AddEstudianteForm from "./components/AddEstudianteForm.tsx";
import {useApiEstudiante} from "./hooks/useApiEstudiante.ts";
import {IEditRow} from "../../types/IEditRow.ts";


interface IEstudianteContext {
    searchText?: string;
    dataTable?: EstudianteGetAdapter[];
    editting?: IEditRow<EstudianteCreateAdapter>;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (estudiante?: IEditRow<EstudianteCreateAdapter>) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (estudianteEdit: EstudianteCreateAdapter) => void;
    onAddTableItem?: (estudianteEdit: EstudianteCreateAdapter) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const EstudianteContext = createContext<IEstudianteContext>({});

export default function EstudiantesScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IEditRow<EstudianteCreateAdapter> | undefined>();
    const [showModal, setShowModal] = useState(false);
    const {estudiantes} = useContext(AppContext)
    const {
        getEstudiantes,
        deleteEstudiante,
        updateEstudiante,
        createEstudiante,
        isLoading
    } = useApiEstudiante()

    useEffect(() => {
        getEstudiantes!();
    }, []);

    const onDeleteTableItem = (deletedEstudianteId: string) => {
        deleteEstudiante(deletedEstudianteId);
    };

    const onEditTableItem = (estudianteEdit: EstudianteCreateAdapter) => {
        updateEstudiante(editting!.id, estudianteEdit);
        setEditting!(undefined);
    };

    const onAddTableItem = (estudiante: EstudianteCreateAdapter) => {
        createEstudiante(estudiante);
    };
    const [dataTable, setDataTable] = useState<EstudianteGetAdapter[]>(estudiantes ?? [])
    useEffect(() => {
        setDataTable(estudiantes!)
    }, [estudiantes]);
    useEffect(() => {
        setDataTable(
            estudiantes?.filter((row) => {
                return Object.values(row).some((value) => {
                    return value?.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }) ?? []
        )
    }, [searchText, estudiantes]);
    return (
        <EstudianteContext.Provider value={{
            isGetLoading: isLoading,
            dataTable: dataTable,
            searchText: searchText,
            editting: editting,
            showModal: showModal,
            setShowModal: setShowModal,
            setEditting: setEditting,
            setSearchText: setSearchText,
            onDeleteTableItem: onDeleteTableItem,
            onEditTableItem: onEditTableItem,
            onAddTableItem: onAddTableItem,
        }}>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar />
                <Body />
                {(showModal || editting) &&
                    <AddEstudianteForm />
                }
            </div>
        </EstudianteContext.Provider>
    );
}