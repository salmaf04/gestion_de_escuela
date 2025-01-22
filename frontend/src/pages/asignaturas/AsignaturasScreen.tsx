// frontend/src/pages/asignaturas/AsignaturasScreen.tsx
import { createContext, useEffect, useState } from "react";
import { AsignaturaGetAdapter } from "./adapters/AsignaturaGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { AsignaturaCreateAdapter } from "./adapters/AsignaturaCreateAdapter.ts";
import AddAsignaturaForm from "./components/AddAsignaturaForm.tsx";
import { useApiAsignatura } from "./hooks/useApiAsignatura.ts";

interface IAsignaturaContext {
    searchText?: string;
    dataTable?: AsignaturaGetAdapter[];
    editting?: AsignaturaCreateAdapter;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (asignatura?: AsignaturaCreateAdapter) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (asignaturaEdit: AsignaturaCreateAdapter) => void;
    onAddTableItem?: (asignaturaEdit: AsignaturaCreateAdapter) => void;
}

export const AsignaturaContext = createContext<IAsignaturaContext>({});

export default function AsignaturasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<AsignaturaCreateAdapter | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {
        asignaturas,
        deleteAsignatura,
        createAsignatura,
        updateAsignatura,
        getAsignaturas,
    } = useApiAsignatura();

    useEffect(() => {
        getAsignaturas();
    }, []);

    const onDeleteTableItem = (deletedAsignaturaId: string) => {
        deleteAsignatura(deletedAsignaturaId);
    };

    const onEditTableItem = (asignaturaEdit: AsignaturaCreateAdapter) => {
        setIsEditing(true);
        updateAsignatura(asignaturaEdit);
        setIsEditing(false);
    };

    const onAddTableItem = (asignatura: AsignaturaCreateAdapter) => {
        setIsCreating(true);
        createAsignatura(asignatura);
        setIsCreating(false);
    };

    return (
        <AsignaturaContext.Provider value={{
            dataTable: asignaturas,
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