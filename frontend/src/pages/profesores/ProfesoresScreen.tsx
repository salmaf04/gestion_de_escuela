import {createContext, useContext, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "./adapters/ProfesorGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {ProfesorCreateAdapter} from "./adapters/ProfesorCreateAdapter.ts";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {useApiProfesor} from "./hooks/useApiProfesor.ts";
import {AppContext} from "../../App.tsx";

interface IProfesorContext {
    searchText?: string;
    dataTable?: ProfesorGetAdapter[];
    editting?: ProfesorCreateAdapter;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (profesor?: ProfesorCreateAdapter) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
    onAddTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
}

export const ProfesorContext = createContext<IProfesorContext>(
    {}
);

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<ProfesorCreateAdapter | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {profesores} = useContext(AppContext)
    const {
        deleteProfesor,
        createProfesor,
        updateProfesor,
        getProfesores,
    } = useApiProfesor()
    useEffect(() => {
        getProfesores()
    }, []);

    const onDeleteTableItem = (deletedProfesorId : string ) => {
        deleteProfesor(deletedProfesorId )
        getProfesores()
    }

    const onEditTableItem = (profesorEdit: ProfesorCreateAdapter) => {
        updateProfesor(profesorEdit)
    }

    const onAddTableItem = (profesor: ProfesorCreateAdapter) => {
        createProfesor(profesor)

    }
    return (
        <ProfesorContext.Provider value={{
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