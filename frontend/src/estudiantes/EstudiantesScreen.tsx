import {createContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {EstudianteGetAdapter} from "./adapters/EstudianteGetAdapter.ts";
import {EstudianteCreateAdapter} from "./adapters/EstudianteCreateAdapter.ts";
import {useEditEstudiante} from "./hooks/useEditEstudiante.ts";
import {useCreateEstudiante} from "./hooks/useCreateEstudiante.ts";
import {useGetEstudiantes} from "./hooks/useGetEstudiante.ts";
import {useDeleteEstudiante} from "./hooks/useDeleteEstudiante.ts";
import AddEstudianteForm from "./components/AddEstudianteForm.tsx";
interface IEstudianteContext {
    searchText?: string;
    dataTable?: EstudianteGetAdapter[];
    editting?: EstudianteCreateAdapter;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (estudiante?: EstudianteCreateAdapter) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (estudianteEdit: EstudianteCreateAdapter) => void;
    onAddTableItem?: (estudianteEdit: EstudianteCreateAdapter) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const EstudianteContext = createContext<IEstudianteContext>(
    {}
);

export default function EstudiantesScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<EstudianteCreateAdapter | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {
        editedEstudiante,
        isLoading: isEditting,
        editEstudiante
    } = useEditEstudiante()
    const {
        newEstudiante,
        isLoading: isCreatting,
        createEstudiante
    } = useCreateEstudiante()

    const {
        isGetLoading,
        estudiantes,
        getEstudiantes,
    } = useGetEstudiantes()

    const {
       deleteEstudiante,
        deletedEstudianteId,
    } = useDeleteEstudiante()

    useEffect(() => {
        getEstudiantes()
    }, [editedEstudiante, newEstudiante , deletedEstudianteId]);

    const onDeleteTableItem = (deletedEstudianteId : string ) => {
        deleteEstudiante(deletedEstudianteId)
    }

    const onEditTableItem = (asignaruraEdit: EstudianteCreateAdapter) => {
        editEstudiante(asignaruraEdit)

    }

    const onAddTableItem = (estudiante: EstudianteCreateAdapter) => {
        createEstudiante(estudiante)
    }
    return (
        <EstudianteContext.Provider value={{
            isGetLoading: isGetLoading,
            dataTable: estudiantes,
            searchText: searchText,
            editting: editting,
            showModal: showModal,
            setShowModal: setShowModal,
            setEditting: setEditting,
            setSearchText: setSearchText,
            onDeleteTableItem: onDeleteTableItem,
            onEditTableItem: onEditTableItem,
            onAddTableItem: onAddTableItem,
            isEditting: isEditting,
            isCreatting: isCreatting
        }
        }>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar/>
                <Body />
                {(showModal || editting) &&
                    <AddEstudianteForm />
                }
            </div>
        </EstudianteContext.Provider>
    )
}