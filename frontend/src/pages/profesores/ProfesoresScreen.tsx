import {createContext, useContext, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "./adapters/ProfesorGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {ProfesorCreateAdapter} from "./adapters/ProfesorCreateAdapter.ts";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {useApiProfesor} from "./hooks/useApiProfesor.ts";
import {AppContext} from "../../App.tsx";

interface IEditProfesor {
    id: string,
    body: ProfesorCreateAdapter
}

interface IProfesorContext {
    searchText?: string;
    dataTable?: ProfesorGetAdapter[];
    editting?: IEditProfesor;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (edit: IEditProfesor | undefined) => void;
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
    const [editting, setEditting] = useState<IEditProfesor | undefined>()
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
        updateProfesor(editting!.id, profesorEdit)
        setEditting!(undefined);
    }

    const onAddTableItem = (profesor: ProfesorCreateAdapter) => {
        createProfesor(profesor)
    }

    const [dataTable, setDataTable] = useState<ProfesorGetAdapter[]>(profesores ?? [])
    useEffect(() => {
        setDataTable(profesores!)
    }, [profesores]);
    useEffect(() => {
        setDataTable(
            profesores?.filter((row) => {
                return Object.values(row).some((value) => {
                    return value?.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }) ?? []
        )
    }, [searchText, profesores]);



    return (
        <ProfesorContext.Provider value={{
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