import {createContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {AsignaturaCreateAdapter} from "./adapters/AsignaturaCreateAdapter.ts";
import AddAsignaturaForm from "./components/AddAsignaturaForm.tsx";
import {AsignaturaGetAdapter} from "./adapters/AsignaturaGetAdapter.ts";
import {useEditAsignatura} from "./hooks/useEditAsignatura.ts";
import {useCreateAsignatura} from "./hooks/useCreateAsignatura.ts";
import {useGetAsignaturas} from "./hooks/useGetAsignatura.ts";
import {useDeleteAsignatura} from "./hooks/useDeleteAsignatura.ts";

interface IAsignaturaContext {
    searchText?: string;
    dataTable?: AsignaturaGetAdapter[];
    editting?: AsignaturaCreateAdapter;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (asignatura?: AsignaturaCreateAdapter) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (asignaturaEdit: AsignaturaCreateAdapter) => void;
    onAddTableItem?: (asignaturaEdit: AsignaturaCreateAdapter) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const AsignaturaContext = createContext<IAsignaturaContext>(
    {}
);

export default function AsignaturasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<AsignaturaCreateAdapter | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {
        editedAsignatura,
        isLoading: isEditting,
        editAsignatura
    } = useEditAsignatura()
    const {
        newAsignatura,
        isLoading: isCreatting,
        createAsignatura
    } = useCreateAsignatura()

    const {
        isGetLoading,
        asignaturas,
        getAsignaturas,
    } = useGetAsignaturas()

    const {
       deleteAsignatura,
        deletedAsignaturaId,
    } = useDeleteAsignatura()

    useEffect(() => {
        getAsignaturas()
    }, [editedAsignatura, newAsignatura , deletedAsignaturaId]);

    const onDeleteTableItem = (deletedAsignaturaId : string ) => {
        deleteAsignatura(deletedAsignaturaId)
    }

    const onEditTableItem = (asignaturaEdit: AsignaturaCreateAdapter) => {
        editAsignatura(asignaturaEdit)

    }

    const onAddTableItem = (asignatura: AsignaturaCreateAdapter) => {
        createAsignatura(asignatura)
    }
    return (
        <AsignaturaContext.Provider value={{
            isGetLoading: isGetLoading,
            dataTable: asignaturas,
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
                    <AddAsignaturaForm />
                }
            </div>
        </AsignaturaContext.Provider>
    )
}