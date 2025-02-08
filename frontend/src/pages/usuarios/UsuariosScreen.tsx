import {createContext, useContext, useEffect, useMemo, useState} from "react";
import Body from "./components/Body.tsx";
import {useApiUsuarios} from "./hooks/useApiUsuarios.ts";
import {DBObject} from "../../types.ts";
import {AppContext} from "../../App.tsx";
import AddUsuarioForm from "./components/AddUsuarioForm.tsx";
import {rolesDisplayParser} from "../../utils/utils.ts";
import ToolBar from "./components/ToolBar.tsx";

interface IUsuariosContext {
    searchText?: string;
    dataTable?: IUsuarioTableRow[];
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
}

export const UsuariosContext = createContext<IUsuariosContext>({});

interface IUsuarioTableRow extends DBObject {
    id: string,
    username: string,
    name: string,
    lastname: string,
    email: string,
    roles: string,
    type: string,
}

export default function UsuariosScreen() {
    const [searchText, setSearchText] = useState('');
    const [showModal, setShowModal] = useState(false);
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
    const [dataTable, setDataTable] = useState<IUsuarioTableRow[]>([])
    const data = useMemo<IUsuarioTableRow[]>(() => {
        return usuarios?.map((item) => {
            return {
                id: item.id,
                username: item.username,
                name: item.name,
                lastname: item.lastname,
                email: item.email,
                roles: item.roles.map((item)=>rolesDisplayParser[item]).join(', '),
                type: item.type,
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
            showModal: showModal,
            setShowModal: setShowModal,
            setSearchText: setSearchText,
            onDeleteTableItem: onDeleteTableItem,
        }}>
            <div className={'w-full h-full flex flex-col'}>
                <ToolBar />
                <Body/>
                {(showModal) &&
                    <AddUsuarioForm />
                }
            </div>
        </UsuariosContext.Provider>
    );
}