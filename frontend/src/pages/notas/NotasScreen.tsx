// frontend/src/pages/notas/AusenciasScreen.tsx
import {createContext, useContext, useEffect, useMemo, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import AddNotaForm from "./components/AddNotaForm.tsx";
import {useApiNotas} from "./hooks/useApiNotas.ts";
import {DBObject} from "../../types.ts";
import {AppContext} from "../../App.tsx";
import {INotaDB} from "./models/INotaDB.ts";
import {RolesEnum} from "../../api/RolesEnum.ts";

interface INotasContext {
    searchText?: string;
    dataTable?: INotaTableRow[];
    editting?: INotaTableRow;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (NotaDB?: INotaTableRow) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (notaEdit: Partial<INotaDB>) => void;
    onAddTableItem?: (notaEdit: Partial<INotaDB>[]) => void;
}

export const NotasContext = createContext<INotasContext>({});

interface INotaTableRow extends DBObject {
    id: string,
    studentName?: string;
    teacherName?: string;
    subjectName?: string;
    last_modified_by?: string
    note_value: number;
}


export default function NotasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<INotaTableRow | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const {notas, allowRoles} = useContext(AppContext)
    const {
        deleteNota,
        createNota,
        updateNota,
        getNotas,
    } = useApiNotas();

    useEffect(() => {
        getNotas();
    }, []);

    const onDeleteTableItem = (deletedNotaId: string) => {
        deleteNota(deletedNotaId);
    };

    const onEditTableItem = (notasEdit: Partial<INotaDB>) => {
        updateNota(editting!.id, notasEdit)
        setEditting(undefined)
    };

    const onAddTableItem = (notas: Partial<INotaDB>[]) => {
        setIsCreating(true);
        notas.forEach((item) => {
            createNota(item);
        })
        setIsCreating(false);
    };
    const [dataTable, setDataTable] = useState<INotaTableRow[]>([])
    const data = useMemo<INotaTableRow[]>(() => {
        return notas?.map((item) => {
            if (allowRoles!([RolesEnum.STUDENT])) {
                return {
                    id: item.id,
                    teacherName: `${item.teacher.name} ${item.teacher.lastname}`,
                    subjectName: item.subject?.name,
                    last_modified_by: `${item.last_modified_by.name} ${item.last_modified_by.lastname}`,
                    note_value: item?.note_value
                }
            }
            if (allowRoles!([RolesEnum.SECRETARY]))
                return {
                    id: item.id,
                    studentName: `${item.student.name} ${item.student.lastname}`,
                    teacherName: `${item.teacher.name} ${item.teacher.lastname}`,
                    subjectName: item.subject?.name,
                    last_modified_by: `${item.last_modified_by.name} ${item.last_modified_by.lastname}`,
                    note_value: item?.note_value
                }
            else
                return {
                    id: item.id,
                    studentName: `${item.student.name} ${item.student.lastname}`,
                    subjectName: item.subject?.name,
                    last_modified_by: `${item.last_modified_by.name} ${item.last_modified_by.lastname}`,
                    note_value: item?.note_value
                }

        }) ?? []
    }, [notas]);

    useEffect(() => {

        setDataTable(data)
    }, [notas]);
    useEffect(() => {
        const filteredData = data?.filter((item) => {
            return Object.values(item).some((value) =>
                value?.toString().toLowerCase().includes(searchText.toLowerCase())
            );
        }) ?? [];
        setDataTable(filteredData);
    }, [searchText, notas]);
    return (
        <NotasContext.Provider value={{
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
                    <AddNotaForm/>
                }
            </div>
        </NotasContext.Provider>
    );
}