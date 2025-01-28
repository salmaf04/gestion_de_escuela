import { createContext, useContext, useEffect, useState } from "react";
import { EstudianteGetAdapter } from "./adapters/EstudianteGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { AppContext } from "../../App.tsx";
import AddEstudianteForm from "./components/AddEstudianteForm.tsx";
import {useApiEstudiante} from "./hooks/useApiEstudiante.ts";
import {IEditRow} from "../../types/IEditRow.ts";
import {IEstudianteLocal} from "./models/IEstudianteLocal.ts";
import {IEstudianteDB} from "./models/IEstudianteDB.ts";


interface IEstudianteContext {
    searchText?: string;
    dataTable?: EstudianteGetAdapter[];
    editting?: IEditRow<Partial<IEstudianteLocal>>;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (estudiante?: IEditRow<Partial<IEstudianteLocal>>) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (estudianteEdit: Partial<IEstudianteLocal>) => void;
    onAddTableItem?: (estudianteEdit: Partial<IEstudianteLocal>) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const EstudianteContext = createContext<IEstudianteContext>({});

export default function EstudiantesScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IEditRow<Partial<IEstudianteLocal>> | undefined>();
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

    const onEditTableItem = (estudianteEdit: Partial<IEstudianteLocal>) => {
        const toEdit: Partial<IEstudianteDB> = {
            ...estudianteEdit,
            course_id: estudianteEdit.course?.id
        }
        updateEstudiante(editting!.id, toEdit);
        setEditting!(undefined);
    };

    const onAddTableItem = (estudiante: Partial<IEstudianteLocal>) => {
        const toCreate: Partial<IEstudianteDB> = {
            ...estudiante,
            course_id: estudiante.course?.id
        }
        createEstudiante(toCreate);
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