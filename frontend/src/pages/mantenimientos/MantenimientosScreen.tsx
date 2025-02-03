// frontend/src/pages/mantenimientos/CursosScreen.tsx
import {createContext, useContext, useEffect, useMemo, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import AddMantenimientoForm from "./components/AddMantenimientoForm.tsx";
import {AppContext} from "../../App.tsx";
import {AulaGetAdapter} from "../aulas/adapters/AulaGetAdapter.ts";
import {DBObject} from "../../types.ts";
import {MantenimientoGetAdapter} from "./adapters/MantenimientoGetAdapter.ts";
import {useApiMantenimiento} from "./hooks/useApiMantenimientos.ts";
import {IMantenimientoDB} from "./models/IMantenimientoDB.ts";

interface IMantenimientoContext {
    searchText?: string;
    dataTable?: IMantenimientoTableRow[];
    editting?: IMantenimientoTableRow;
    showModal?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (idMantenimiento?: IMantenimientoTableRow) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (mantenimientoEdit: IMantenimientoDB) => void;
    onAddTableItem?: (mantenimientoEdit: IMantenimientoDB) => void;
    aulas?: AulaGetAdapter[],
    mantenimientos?: MantenimientoGetAdapter[],
    isLoading?: boolean
}

interface IMantenimientoTableRow extends DBObject {
    id: string
    mean_name: string,
    date: string,
    cost: number,
    finished: boolean
}

export const MantenimientoContext = createContext<IMantenimientoContext>({});

export default function MantenimientosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IMantenimientoTableRow | undefined>(); //id del elemento que se esta editando
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {mantenimientos} = useContext(AppContext)
    const {
        deleteMantenimiento,
        createMantenimiento,
        updateMantenimiento,
        getMantenimientos,
        isLoading
    } = useApiMantenimiento();

    useEffect(() => {
        getMantenimientos();
    }, []);

    const onDeleteTableItem = (deletedMantenimientoId: string) => {
        deleteMantenimiento(deletedMantenimientoId);
    };

    const onEditTableItem = (mantenimientoEdit: Partial<IMantenimientoDB>) => {
        setIsEditing(true);
        updateMantenimiento!(editting!.id, mantenimientoEdit);
        setEditting(undefined)
        setIsEditing(false);
    };

    const onAddTableItem = (mantenimiento: IMantenimientoDB) => {
        setIsCreating(true);
        createMantenimiento(mantenimiento);
        setIsCreating(false);
    };

    const [dataTable, setDataTable] = useState<IMantenimientoTableRow[]>([])
    const data = useMemo<IMantenimientoTableRow[]>(() => {
        return mantenimientos?.map((item) => {
            return {
                id: item.id,
                mean_name: item.mean?.name,
                date: item.date,
                cost: item.cost,
                finished: item.finished
            }
        }) ?? []
    }, [mantenimientos]);

    useEffect(() => {

        setDataTable(data)
    }, [mantenimientos]);
    useEffect(() => {
        const filteredData = data?.filter((item) => {
            return Object.values(item).some((value) =>
                value?.toString().toLowerCase().includes(searchText.toLowerCase())
            );
        }) ?? [];
        setDataTable(filteredData);
    }, [searchText, mantenimientos]);
    return (
        <MantenimientoContext.Provider value={{
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
            mantenimientos: mantenimientos,
            isLoading: isLoading
        }}>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar />
                <Body />
                {(showModal || editting) &&
                    <AddMantenimientoForm />
                }
            </div>
        </MantenimientoContext.Provider>
    );
}