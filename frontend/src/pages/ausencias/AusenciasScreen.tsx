// frontend/src/pages/ausencias/AusenciasScreen.tsx
import {createContext, useContext, useEffect, useMemo, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import AddAusenciaForm from "./components/AddAusenciaForm.tsx";
import {useApiAusencias} from "./hooks/useApiAusencias.ts";
import {DBObject} from "../../types.ts";
import {AppContext} from "../../App.tsx";
import {IAusenciaDB} from "./models/IAusenciaDB.ts";

interface IAusenciasContext {
    searchText?: string;
    dataTable?: IAusenciaTableRow[];
    editting?: IAusenciaTableRow;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (AusenciaDB?: IAusenciaTableRow) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (ausenciaEdit: Partial<IAusenciaDB>) => void;
    onAddTableItem?: (ausenciaEdit: Partial<IAusenciaDB>[]) => void;
}

export const AusenciasContext = createContext<IAusenciasContext>({});

interface IAusenciaTableRow extends DBObject {
    id: string,
    studentName?: string;
    subjectName?: string;
    date: string;
}


export default function AusenciasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IAusenciaTableRow | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const {ausencias} = useContext(AppContext)
    const {
        deleteAusencia,
        createAusencia,
        updateAusencia,
        getAusencias,
    } = useApiAusencias();

    useEffect(() => {
        getAusencias();
    }, []);

    const onDeleteTableItem = (deletedAusenciaId: string) => {
        deleteAusencia(deletedAusenciaId);
    };

    const onEditTableItem = (ausenciasEdit: Partial<IAusenciaDB>) => {
        updateAusencia(editting!.id, ausenciasEdit)
        setEditting(undefined)
    };

    const onAddTableItem = (ausencias: Partial<IAusenciaDB>[]) => {
        setIsCreating(true);
        ausencias.forEach((item) => {
            createAusencia(item);
        })
        setIsCreating(false);
    };
    const [dataTable, setDataTable] = useState<IAusenciaTableRow[]>([])
    const data = useMemo<IAusenciaTableRow[]>(() => {
        return ausencias?.map((item) => {
            return {
                id: item.id,
                studentName: item.student.name,
                subjectName: item.subject.name,
                date: item.date
            }
        }) ?? []
    }, [ausencias]);

    useEffect(() => {

        setDataTable(data)
    }, [ausencias]);
    useEffect(() => {
        const filteredData = data?.filter((item) => {
            return Object.values(item).some((value) =>
                value?.toString().toLowerCase().includes(searchText.toLowerCase())
            );
        }) ?? [];
        setDataTable(filteredData);
    }, [searchText, ausencias]);
    return (
        <AusenciasContext.Provider value={{
            dataTable: dataTable,
            searchText: searchText,
            editting: editting,
            showModal: showModal,
            isCreatting: isCreating,
            setShowModal: setShowModal,
            setEditting: setEditting,
            setSearchText: setSearchText,
            onDeleteTableItem: onDeleteTableItem,
            onEditTableItem: onEditTableItem,
            onAddTableItem: onAddTableItem,
        }}>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar/>
                <Body/>
                {(showModal || editting) &&
                    <AddAusenciaForm/>
                }
            </div>
        </AusenciasContext.Provider>
    );
}