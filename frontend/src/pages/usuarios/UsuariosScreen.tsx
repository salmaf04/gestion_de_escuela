import {createContext, useContext, useEffect, useMemo, useState} from "react";
import Body from "./components/Body.tsx";
import {useApiUsuarios} from "./hooks/useApiUsuarios.ts";
import {DBObject} from "../../types.ts";
import {AppContext} from "../../App.tsx";
import ToolBar from "../../components/ToolBar.tsx";
import AddUsuarioForm from "./components/AddUsuarioForm.tsx";
import {IUsuarioLocal} from "./models/IUsuarioLocal.ts";

interface IUsuariosContext {
    searchText?: string;
    dataTable?: IUsuarioTableRow[];
    editting?: IUsuarioTableRow;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (UsuarioDB?: IUsuarioTableRow) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (usuarioEdit: Partial<IUsuarioLocal>) => void;
    onAddTableItem?: (usuarioEdit: Partial<IUsuarioLocal>[]) => void;
}

export const UsuariosContext = createContext<IUsuariosContext>({});

interface IUsuarioTableRow extends DBObject {
    id: string,
    username: string,
    name: string,
    lastname: string,
}

export default function UsuariosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IUsuarioTableRow | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const {usuarios} = useContext(AppContext)
    const {
        deleteUsuario,
        getUsuarios,
    } = useApiUsuarios();

    useEffect(() => {
        getUsuarios();
    }, []);

    const onDeleteTableItem = (deletedUsuarioId: string) => {
        deleteUsuario(deletedUsuarioId);
    };

    const onEditTableItem = (usuariosEdit: Partial<IUsuarioLocal>) => {
        setEditting(undefined)
    };

    const onAddTableItem = (usuarios: Partial<IUsuarioLocal>[]) => {
        setIsCreating(true);
        usuarios.forEach((item) => {
        })
        setIsCreating(false);
    };
    const [dataTable, setDataTable] = useState<IUsuarioTableRow[]>([])
    const data = useMemo<IUsuarioTableRow[]>(() => {
        return usuarios?.map((item) => {
            return {
                id: item.id,
                username: item.username,
                name: item.name,
                lastname: item.lastname,
            }
        }) ?? []
    }, [usuarios]);

    useEffect(() => {

        setDataTable(data)
    }, [usuarios]);
    useEffect(() => {
        const filteredData = data?.filter((item) => {
            return Object.values(item).some((value) =>
                value?.toString().toLowerCase().includes(searchText.toLowerCase())
            );
        }) ?? [];
        setDataTable(filteredData);
    }, [searchText, usuarios]);
    return (
        <UsuariosContext.Provider value={{
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
                <ToolBar context={UsuariosContext}/>
                <Body/>
                {(showModal || editting) &&
                    <AddUsuarioForm />
                }
            </div>
        </UsuariosContext.Provider>
    );
}