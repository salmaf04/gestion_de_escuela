// frontend/src/pages/aulas/AulasScreen.tsx
import { createContext, useEffect, useState } from "react";
import { AulaGetAdapter } from "./adapters/AulaGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { AulaCreateAdapter } from "./adapters/AulaCreateAdapter.ts";
import AddAulaForm from "./components/AddAulaForm.tsx";
import { useApiAulas } from "./hooks/useApiAulas.ts";

interface IAulasContext {
    searchText?: string;
    dataTable?: AulaGetAdapter[];
    editting?: AulaCreateAdapter;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (aula?: AulaCreateAdapter) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (aulaEdit: AulaCreateAdapter) => void;
    onAddTableItem?: (aulaEdit: AulaCreateAdapter) => void;
}

export const AulasContext = createContext<IAulasContext>({});

export default function AulasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<AulaCreateAdapter | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {
        aulas,
        deleteAula,
        createAula,
        updateAula,
        getAulas,
    } = useApiAulas();

    useEffect(() => {
        getAulas();
    }, []);

    const onDeleteTableItem = (deletedAulaId: string) => {
        deleteAula(deletedAulaId);
    };

    const onEditTableItem = (aulaEdit: AulaCreateAdapter) => {
        setIsEditing(true);
        updateAula(aulaEdit);
        setIsEditing(false);
    };

    const onAddTableItem = (aula: AulaCreateAdapter) => {
        setIsCreating(true);
        createAula(aula);
        setIsCreating(false);
    };

    return (
        <AulasContext.Provider value={{
            dataTable: aulas,
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
                    <AddAulaForm />
                }
            </div>
        </AulasContext.Provider>
    );
}