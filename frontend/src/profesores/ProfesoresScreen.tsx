import {createContext, useContext, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "./adapters/ProfesorGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {useGetProfesores} from "./hooks/useGetProfesores.ts";
import {ProfesorCreateAdapter} from "./adapters/ProfesorCreateAdapter.ts";
import {AppContext} from "../App.tsx";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {useEditProfesor} from "./hooks/useEditProfesor.ts";
import {useCreateProfesor} from "./hooks/useCreateProfesor.ts";
import {useDeleteProfesor} from "./hooks/useDeleteProfesor.ts";

interface IProfesorContext {
    searchText?: string;
    dataTable?: ProfesorGetAdapter[];
    editting?: ProfesorCreateAdapter;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (profesor?: ProfesorCreateAdapter) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
    onAddTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const ProfesorContext = createContext<IProfesorContext>(
    {}
);

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<ProfesorCreateAdapter | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {setError} = useContext(AppContext)
    const {
        editedProfesor,
        isLoading: isEditting,
        editProfesor
    } = useEditProfesor()
    const {
        newProfesor,
        isLoading: isCreatting,
        createProfesor
    } = useCreateProfesor()

    const {
        isGetLoading,
        profesores,
        getProfesores,
    } = useGetProfesores(setError!)

    const {
       deleteProfesor,
        deletedProfesorId,
    } = useDeleteProfesor()

    useEffect(() => {
        getProfesores()
    }, [editedProfesor, newProfesor , deletedProfesorId]);

    const onDeleteTableItem = (deletedProfesorId : string ) => {
        deleteProfesor(deletedProfesorId , setError! )
    }

    const onEditTableItem = (profesorEdit: ProfesorCreateAdapter) => {
        editProfesor(profesorEdit, setError!)

    }

    const onAddTableItem = (profesor: ProfesorCreateAdapter) => {
        createProfesor(profesor, setError!)
    }
    return (
        <ProfesorContext.Provider value={{
            isGetLoading: isGetLoading,
            dataTable: profesores,
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
                    <AddProfesorForm />
                }
            </div>
        </ProfesorContext.Provider>
    )
}