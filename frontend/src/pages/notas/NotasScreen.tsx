// frontend/src/pages/notas/NotasScreen.tsx
import { createContext, useEffect, useState } from "react";
import { NotaGetAdapter } from "./adapters/NotaGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { NotaCreateAdapter } from "./adapters/NotaCreateAdapter.ts";
import AddNotaForm from "./components/AddNotaForm.tsx";
import { useApiNotas } from "./hooks/useApiNotas.ts";

interface INotasContext {
    searchText?: string;
    dataTable?: NotaGetAdapter[];
    editting?: NotaCreateAdapter;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (nota?: NotaCreateAdapter) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (notaEdit: NotaCreateAdapter[]) => void;
    onAddTableItem?: (notaEdit: NotaCreateAdapter[]) => void;
}

export const NotasContext = createContext<INotasContext>({});

export default function NotasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<NotaCreateAdapter | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {
        notas,
        deleteNota,
        createNota,
        updateNota,
        getNotas,
    } = useApiNotas();

    useEffect(() => {
        getNotas();
    }, []);

    const onDeleteTableItem = (deletedNotaId: string) => {
        deleteNota(deletedNotaId);
    };

    const onEditTableItem = (notasEdit: NotaCreateAdapter[]) => {
        setIsEditing(true);
        notasEdit.forEach((item)=>{
            updateNota(item);
        })
        setIsEditing(false);
    };

    const onAddTableItem = (notas: NotaCreateAdapter[]) => {
        setIsCreating(true);
        notas.forEach((item)=>{
            createNota(item);
        })
        setIsCreating(false);
    };

    return (
        <NotasContext.Provider value={{
            dataTable: notas,
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
                    <AddNotaForm />
                }
            </div>
        </NotasContext.Provider>
    );
}