// frontend/src/pages/medios/CursosScreen.tsx
import {createContext, useContext, useEffect, useMemo, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import { MedioCreateAdapter } from "./adapters/MedioCreateAdapter.ts";
import AddMedioForm from "./components/AddMedioForm.tsx";
import {AppContext} from "../../App.tsx";
import {AulaGetAdapter} from "../aulas/adapters/AulaGetAdapter.ts";
import {DBObject} from "../../types.ts";
import {MedioGetAdapter} from "./adapters/MedioGetAdapter.ts";
import {useApiAulas} from "../aulas/hooks/useApiAulas.ts";
import {useApiMedio} from "./hooks/useApiMedios.ts";

interface IMedioContext {
    searchText?: string;
    dataTable?: IMedioTableRow[];
    editting?: IMedioTableRow;
    showModal?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (idMedio?: IMedioTableRow) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (medioEdit: MedioCreateAdapter) => void;
    onAddTableItem?: (medioEdit: MedioCreateAdapter) => void;
    aulas?: AulaGetAdapter[],
    medios?: MedioGetAdapter[],
    isLoading?: boolean
}

interface IMedioTableRow extends DBObject {
    id: string;
    name: string;
    state: string;
    location: string;
    classroom_name: string;
    type: string;
}

export const MedioContext = createContext<IMedioContext>({});

export default function MediosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IMedioTableRow | undefined>(); //id del elemento que se esta editando
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {medios, aulas} = useContext(AppContext)
    const {getAulas} = useApiAulas()
    const {
        deleteMedio,
        createMedio,
        updateMedio,
        getMedios,
        isLoading
    } = useApiMedio();

    useEffect(() => {
        getMedios();
        getAulas()
    }, []);

    const onDeleteTableItem = (deletedMedioId: string) => {
        deleteMedio(deletedMedioId);
    };

    const onEditTableItem = (medioEdit: MedioCreateAdapter) => {
        setIsEditing(true);
        updateMedio!(editting!.id, medioEdit);
        setEditting(undefined)
        setIsEditing(false);
    };

    const onAddTableItem = (medio: MedioCreateAdapter) => {
        setIsCreating(true);
        createMedio(medio);
        setIsCreating(false);
    };

    const [dataTable, setDataTable] = useState<IMedioTableRow[]>([])
    console.log(medios)
    const data = useMemo<IMedioTableRow[]>(() => {
        return medios?.map((item) => {
            return {
                id: item.id,
                name: item.name,
                state: item.state,
                location: item.location,
                type: item.type,
            }
        }) ?? []
    }, [medios]);

    useEffect(() => {

        setDataTable(data)
    }, [medios]);
    useEffect(() => {
        const filteredData = data?.filter((item) => {
            return Object.values(item).some((value) =>
                value?.toString().toLowerCase().includes(searchText.toLowerCase())
            );
        }) ?? [];
        setDataTable(filteredData);
    }, [searchText, medios]);
    return (
        <MedioContext.Provider value={{
            dataTable: dataTable,
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
            aulas: aulas,
            medios: medios,
            isLoading: isLoading
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