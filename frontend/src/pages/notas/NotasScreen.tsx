// frontend/src/pages/notas/NotasScreen.tsx
import {createContext, useContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {NotaCreateAdapter} from "./adapters/NotaCreateAdapter.ts";
import AddNotaForm from "./components/AddNotaForm.tsx";
import {useApiNotas} from "./hooks/useApiNotas.ts";
import {DBObject} from "../../types.ts";
import {AppContext} from "../../App.tsx";
import {useApiEstudiante} from "../estudiantes/hooks/useApiEstudiante.ts";
import {useApiAsignatura} from "../asignaturas/hooks/useApiAsignatura.ts";
import {useApiProfesor} from "../profesores/hooks/useApiProfesor.ts";

interface INotasContext {
    searchText?: string;
    dataTable?: INotaTableRow[];
    editting?: NotaCreateAdapter;
    showModal?: boolean;
    isGetLoading?: boolean;
    isCreatting?: boolean;
    isEditting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (nota?: NotaCreateAdapter) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (notaEdit: NotaCreateAdapter[]) => void;
    onAddTableItem?: (notaEdit: NotaCreateAdapter[]) => void;
}

export const NotasContext = createContext<INotasContext>({});

interface INotaTableRow extends DBObject {
    id: string,
    teacher: string;
    student: string;
    subject: string;
    note_value: number;
}


export default function NotasScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<NotaCreateAdapter | undefined>();
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const {getEstudiantes} = useApiEstudiante()
    const {getAsignaturas} = useApiAsignatura()
    const {getProfesores} = useApiProfesor()
    const {asignaturas, estudiantes, profesores} = useContext(AppContext)
    const {
        notas,
        deleteNota,
        createNota,
        updateNota,
        getNotas,
    } = useApiNotas();

    useEffect(() => {
        getNotas();
        getAsignaturas()
        getEstudiantes()
        getProfesores()
    }, []);

    const onDeleteTableItem = (deletedNotaId: string) => {
        deleteNota(deletedNotaId);
    };

    const onEditTableItem = (notasEdit: NotaCreateAdapter[]) => {
        setIsEditing(true);
        notasEdit.forEach((item) => {
            updateNota(item);
        })
        setIsEditing(false);
    };

    const onAddTableItem = (notas: NotaCreateAdapter[]) => {
        setIsCreating(true);
        notas.forEach((item) => {
            createNota(item);
        })
        setIsCreating(false);
    };
    const [dataTable, setDataTable] = useState<INotaTableRow[]>([])
    useEffect(() => {
        const data: INotaTableRow[] = notas?.map((item) => {
            return {
                id: item.id,
                student: estudiantes?.find((i) => i.id === item.student_id)?.name ?? "Desconocido",
                teacher: profesores?.find((i) => i.id === item.teacher_id)?.name ?? "Desconocido",
                subject: asignaturas?.find((i) => i.id === item.subject_id)?.name ?? "Desconocido",
                note_value: item.note_value
            }
        }) ?? []
        setDataTable(data)
    }, [notas]);
    useEffect(() => {
        setDataTable(
            dataTable?.filter((row) => {
                return Object.values(row).some((value) => {
                    return value?.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }) ?? []
        )
    }, [searchText, notas]);


    return (
        <NotasContext.Provider value={{
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