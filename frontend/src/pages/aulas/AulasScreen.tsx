import {createContext, useContext, useEffect, useMemo, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {AulaCreateAdapter} from "./adapters/AulaCreateAdapter.ts";
import AddAulaForm from "./components/AddAulaForm.tsx";
import {AppContext} from "../../App.tsx";
import {IEditRow} from "../../types/IEditRow.ts";
import {useApiAulas} from "./hooks/useApiAulas.ts";

interface IAulaContext {
    searchText?: string;
    dataTable?: IAulaTableRow[];
    editting?: IEditRow<IAulaTableRow>;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (edit: IEditRow<IAulaTableRow> | undefined) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (aulaEdit: AulaCreateAdapter) => void;
    onAddTableItem?: (aulaEdit: AulaCreateAdapter) => void;
    isLoading?: boolean
}

export const AulasContext = createContext<IAulaContext>(
    {}
);

interface IAulaTableRow{
    id: string;
    number: string
    location: string;
    capacity: number;
}

export default function AulasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IEditRow<IAulaTableRow> | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {aulas} = useContext(AppContext)
    const {
        deleteAula,
        createAula,
        updateAula,
        getAulas,
        isLoading,
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

    const [dataTable, setDataTable] = useState<IAulaTableRow[]>([])

    const data = useMemo<IAulaTableRow[]>(() => {
        return aulas?.map((item) => {
            return {
                id: item!.id,
                number: item.number,
                location: item.location,
                capacity: item.capacity
            }
        }) ?? []
    }, [aulas]);
    useEffect(() => {
        setDataTable(data!)
    }, [aulas]);
    useEffect(() => {
        setDataTable(
            data?.filter((row) => {
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