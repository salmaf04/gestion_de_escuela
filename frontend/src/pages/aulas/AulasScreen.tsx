import {createContext, useContext, useEffect, useState} from "react";
import {AulaGetAdapter} from "./adapters/AulaGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {AulaCreateAdapter} from "./adapters/AulaCreateAdapter.ts";
import AddAulaForm from "./components/AddAulaForm.tsx";
import {AppContext} from "../../App.tsx";
import {IEditRow} from "../../types/IEditRow.ts";
import {useApiAulas} from "./hooks/useApiAulas.ts";

interface IAulaContext {
    searchText?: string;
    dataTable?: AulaGetAdapter[];
    editting?: IEditRow<AulaCreateAdapter>;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (edit: IEditRow<AulaCreateAdapter> | undefined) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (aulaEdit: AulaCreateAdapter) => void;
    onAddTableItem?: (aulaEdit: AulaCreateAdapter) => void;
    isLoading?: boolean
}

export const AulasContext = createContext<IAulaContext>(
    {}
);

export default function AulasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IEditRow<AulaCreateAdapter> | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {aulas} = useContext(AppContext)
    const {
        deleteAula,
        createAula,
        updateAula,
        getAulas,
        isLoading
    } = useApiAulas()
    useEffect(() => {
        getAulas()
    }, []);

    const onDeleteTableItem = (deletedAulaId : string ) => {
        deleteAula(deletedAulaId )
        getAulas()
    }

    const onEditTableItem = (aulaEdit: AulaCreateAdapter) => {
        updateAula(editting!.id, aulaEdit)
        setEditting!(undefined);
    }

    const onAddTableItem = (aula: AulaCreateAdapter) => {
        createAula(aula)
    }

    const [dataTable, setDataTable] = useState<AulaGetAdapter[]>(aulas ?? [])
    useEffect(() => {
        setDataTable(aulas!)
        console.log(aulas)
    }, [aulas]);
    useEffect(() => {
        setDataTable(
            aulas?.filter((row) => {
                return Object.values(row).some((value) => {
                    return value?.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }) ?? []
        )
    }, [searchText, aulas]);



    return (
        <AulasContext.Provider value={{
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
            isLoading: isLoading,
        }
        }>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar/>
                <Body />
                {(showModal || editting) &&
                    <AddAulaForm />
                }
            </div>
        </AulasContext.Provider>
    )
}