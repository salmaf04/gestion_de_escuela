import {createContext, useContext, useEffect, useMemo, useState} from "react";
import Body from "./components/Body.tsx";
import {useApiUsuarios} from "./hooks/useApiUsuarios.ts";
import {DBObject} from "../../types.ts";
import {AppContext} from "../../App.tsx";
import {IUsuarioDB} from "./models/IUsuarioDB.ts";
import ToolBar from "../../components/ToolBar.tsx";
import AddUsuarioForm from "./components/AddUsuarioForm.tsx";

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
    onEditTableItem?: (usuarioEdit: Partial<IUsuarioDB>) => void;
    onAddTableItem?: (usuarioEdit: Partial<IUsuarioDB>[]) => void;
}

export const UsuariosContext = createContext<IUsuariosContext>({});

interface IUsuarioTableRow extends DBObject {
    id: string,
    teacherName?: string;
    studentName?: string;
    subjectName?: string;
    note_value: number;
}


export default function UsuariosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IUsuarioTableRow | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const {usuarios} = useContext(AppContext)
    const {
        deleteUsuario,
        createUsuario,
        updateUsuario,
        getUsuarios,
    } = useApiUsuarios();

    useEffect(() => {
        getUsuarios();
    }, []);

    const onDeleteTableItem = (deletedUsuarioId: string) => {
        deleteUsuario(deletedUsuarioId);
    };

    const onEditTableItem = (usuariosEdit: Partial<IUsuarioDB>) => {
        updateUsuario(editting!.id, usuariosEdit)
        setEditting(undefined)
    };

    const onAddTableItem = (usuarios: Partial<IUsuarioDB>[]) => {
        setIsCreating(true);
        usuarios.forEach((item) => {
            createUsuario(item);
        })
        setIsCreating(false);
    };
    const [dataTable, setDataTable] = useState<IUsuarioTableRow[]>([])
    const data = useMemo<IUsuarioTableRow[]>(() => {
        return usuarios?.map((item) => {
            return {
                id: item.id,
                studentName: item.student.name,
                teacherName: item.teacher.name,
                subjectName: item.subject.name,
                note_value: item.note_value
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