import {createContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {AulaGetAdapter} from "./adapters/MedioGetAdapter.ts";
import {AulaCreateAdapter} from "./adapters/MedioCreateAdapter.ts";
import {useEditAula} from "./hooks/useEditMedio.ts";
import {useCreateAula} from "./hooks/useCreateMedio.ts";
import {useGetAulas} from "./hooks/useGetMedio.ts";
import {useDeleteAula} from "./hooks/useDeleteMedio.ts";
import AddAulaForm from "./components/AddMedioForm.tsx";
interface IAulaContext {
    searchText?: string;
    dataTable?: AulaGetAdapter[];
    editting?: AulaCreateAdapter;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (aula?: AulaCreateAdapter) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (aulaEdit: AulaCreateAdapter) => void;
    onAddTableItem?: (aulaEdit: AulaCreateAdapter) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const AulaContext = createContext<IAulaContext>(
    {}
);

export default function AulasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<AulaCreateAdapter | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {
        editedAula,
        isLoading: isEditting,
        editAula
    } = useEditAula()
    const {
        newAula,
        isLoading: isCreatting,
        createAula
    } = useCreateAula()

    const {
        isGetLoading,
        aulas,
        getAulas,
    } = useGetAulas()

    const {
       deleteAula,
        deletedAulaId,
    } = useDeleteAula()

    useEffect(() => {
        getAulas()
    }, [editedAula, newAula , deletedAulaId]);

    const onDeleteTableItem = (deletedAulaId : string ) => {
        deleteAula(deletedAulaId)
    }

    const onEditTableItem = (asignaruraEdit: AulaCreateAdapter) => {
        editAula(asignaruraEdit)

    }

    const onAddTableItem = (aula: AulaCreateAdapter) => {
        createAula(aula)
    }
    return (
        <AulaContext.Provider value={{
            isGetLoading: isGetLoading,
            dataTable: aulas,
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
                    <AddAulaForm />
                }
            </div>
        </AulaContext.Provider>
    )
}