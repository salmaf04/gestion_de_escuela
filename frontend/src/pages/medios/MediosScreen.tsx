// frontend/src/pages/medios/MediosScreen.tsx
import { createContext, useEffect, useState } from "react";
import { MedioGetAdapter } from "./adapters/MedioGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { MedioCreateAdapter } from "./adapters/MedioCreateAdapter.ts";
import AddMedioForm from "./components/AddMedioForm.tsx";
import { useApiMedios } from "./hooks/useApiMedios.ts";

interface IMedioContext {
    searchText?: string;
    dataTable?: MedioGetAdapter[];
    editting?: MedioCreateAdapter;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (medio?: MedioCreateAdapter) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (medioEdit: MedioCreateAdapter) => void;
    onAddTableItem?: (medioEdit: MedioCreateAdapter) => void;
}

export const MedioContext = createContext<IMedioContext>({});

export default function MediosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<MedioCreateAdapter | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {
        medios,
        deleteMedio,
        createMedio,
        updateMedio,
        getMedios,
    } = useApiMedios();

    useEffect(() => {
        getMedios();
    }, []);

    const onDeleteTableItem = (deletedMedioId: string) => {
        deleteMedio(deletedMedioId);
    };

    const onEditTableItem = (medioEdit: MedioCreateAdapter) => {
        setIsEditing(true);
        updateMedio(medioEdit);
        setIsEditing(false);
    };

    const onAddTableItem = (medio: MedioCreateAdapter) => {
        setIsCreating(true);
        createMedio(medio);
        setIsCreating(false);
    };

    return (
        <MedioContext.Provider value={{
            dataTable: medios,
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
                    <AddMedioForm />
                }
            </div>
        </MedioContext.Provider>
    );
}