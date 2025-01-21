import {createContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {MantenimientoGetAdapter} from "./adapters/MantenimientoGetAdapter.ts";
import {MantenimientoCreateAdapter} from "./adapters/MantenimientoCreateAdapter.ts";
import AddMantenimientoForm from "./components/AddMantenimientoForm.tsx";
import {useEditMantenimiento} from "./hooks/useEditMantenimiento.ts";
import {useCreateMantenimiento} from "./hooks/useCreateMantenimiento.ts";
import {useGetMantenimientos} from "./hooks/useGetMantenimiento.ts";
import {useDeleteMantenimiento} from "./hooks/useDeleteMantenimiento.ts";
interface IMantenimientoContext {
    searchText?: string;
    dataTable?: MantenimientoGetAdapter[];
    editting?: MantenimientoCreateAdapter;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (mantenimiento?: MantenimientoCreateAdapter) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (mantenimientoEdit: MantenimientoCreateAdapter) => void;
    onAddTableItem?: (mantenimientoEdit: MantenimientoCreateAdapter) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

export const MantenimientoContext = createContext<IMantenimientoContext>(
    {}
);

export default function MantenimientosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<MantenimientoCreateAdapter | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {
        editedMantenimiento,
        isLoading: isEditting,
        editMantenimiento
    } = useEditMantenimiento()
    const {
        newMantenimiento,
        isLoading: isCreatting,
        createMantenimiento
    } = useCreateMantenimiento()

    const {
        isGetLoading,
        mantenimientos,
        getMantenimientos,
    } = useGetMantenimientos()

    const {
       deleteMantenimiento,
        deletedMantenimientoId,
    } = useDeleteMantenimiento()

    useEffect(() => {
        getMantenimientos()
    }, [editedMantenimiento, newMantenimiento , deletedMantenimientoId]);

    const onDeleteTableItem = (deletedMantenimientoId : string ) => {
        deleteMantenimiento(deletedMantenimientoId)
    }

    const onEditTableItem = (asignaruraEdit: MantenimientoCreateAdapter) => {
        editMantenimiento(asignaruraEdit)

    }

    const onAddTableItem = (mantenimiento: MantenimientoCreateAdapter) => {
        createMantenimiento(mantenimiento)
    }
    return (
        <MantenimientoContext.Provider value={{
            isGetLoading: isGetLoading,
            dataTable: mantenimientos,
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
                    <AddMantenimientoForm />
                }
            </div>
        </MantenimientoContext.Provider>
    )
}