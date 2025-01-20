import {createContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {MedioGetAdapter} from "./adapters/MedioGetAdapter.ts";
import {MedioCreateAdapter} from "./adapters/MedioCreateAdapter.ts";
import AddMedioForm from "./components/AddMedioForm.tsx";
import {useEditMedio} from "./hooks/useEditMedio.ts";
import {useCreateMedio} from "./hooks/useCreateMedio.ts";
import {useGetMedios} from "./hooks/useGetMedio.ts";
import {useDeleteMedio} from "./hooks/useDeleteMedio.ts";
interface IMedioContext {
    searchText?: string;
    dataTable?: MedioGetAdapter[];
    editting?: MedioCreateAdapter;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (medio?: MedioCreateAdapter) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (medioEdit: MedioCreateAdapter) => void;
    onAddTableItem?: (medioEdit: MedioCreateAdapter) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const MedioContext = createContext<IMedioContext>(
    {}
);

export default function MediosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<MedioCreateAdapter | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {
        editedMedio,
        isLoading: isEditting,
        editMedio
    } = useEditMedio()
    const {
        newMedio,
        isLoading: isCreatting,
        createMedio
    } = useCreateMedio()

    const {
        isGetLoading,
        medios,
        getMedios,
    } = useGetMedios()

    const {
       deleteMedio,
        deletedMedioId,
    } = useDeleteMedio()

    useEffect(() => {
        getMedios()
    }, [editedMedio, newMedio , deletedMedioId]);

    const onDeleteTableItem = (deletedMedioId : string ) => {
        deleteMedio(deletedMedioId)
    }

    const onEditTableItem = (asignaruraEdit: MedioCreateAdapter) => {
        editMedio(asignaruraEdit)

    }

    const onAddTableItem = (medio: MedioCreateAdapter) => {
        createMedio(medio)
    }
    return (
        <MedioContext.Provider value={{
            isGetLoading: isGetLoading,
            dataTable: medios,
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
                    <AddMedioForm />
                }
            </div>
        </MedioContext.Provider>
    )
}