// frontend/src/pages/cursos/CursosScreen.tsx
import {createContext, useContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import AddCursoForm from "./components/AddCursoForm.tsx";
import {AppContext} from "../../App.tsx";
import {AulaGetAdapter} from "../aulas/adapters/AulaGetAdapter.ts";
import {ICursoCreateDB} from "./models/ICursoCreateDB.ts";
import {ICursoGetDB} from "./models/ICursoGetDB.ts";
import {useApiCurso} from "./hooks/useApiCurso.ts";
import {ICursoGetLocal} from "./models/ICursoGetLocal.ts";

interface ICursoContext {
    searchText?: string;
    dataTable?: ICursoGetLocal[];
    editting?: ICursoGetLocal;
    showModal?: boolean;
    isCreatting?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (idCurso?: ICursoGetLocal) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (cursoEdit: Partial<ICursoCreateDB>) => void;
    onAddTableItem?: (cursoAdd: ICursoCreateDB) => void;
    aulas?: AulaGetAdapter[],
    cursos?: ICursoGetDB[],
    isLoading?: boolean
}

export const CursoContext = createContext<ICursoContext>({});

export default function CursosScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<ICursoGetLocal | undefined>(); //id del elemento que se esta editando
    const [showModal, setShowModal] = useState(false);
    const [isCreating, setIsCreating] = useState(false);
    const {cursos, aulas} = useContext(AppContext)
    const {
        deleteCurso,
        createCurso,
        updateCurso,
        getCursos,
        isLoading
    } = useApiCurso();

    useEffect(() => {
        getCursos();
    }, []);

    const onDeleteTableItem = (deletedCursoId: string) => {
        deleteCurso(deletedCursoId);
    };

    const onEditTableItem = (cursoEdit: Partial<ICursoCreateDB>) => {
        updateCurso!(editting!.id!, cursoEdit);
        setEditting(undefined)
    };

    const onAddTableItem = (curso: ICursoCreateDB) => {
        setIsCreating(true);
        createCurso(curso);
        setIsCreating(false);
    };

    const [dataTable, setDataTable] = useState<ICursoGetDB[]>([])
    useEffect(() => {
        console.log(cursos)
        setDataTable(cursos!)
    }, [cursos]);
    useEffect(() => {
        setDataTable(
            cursos?.filter((row) => {
                return Object.values(row).some((value) => {
                    return value?.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }) ?? []
        )
    }, [searchText, cursos]);
    console.log(showModal)
    return (
        <CursoContext.Provider value={{
            dataTable: dataTable,
            searchText: searchText,
            editting: editting,
            showModal: showModal,
            isCreatting: isCreating,
            setShowModal: setShowModal,
            setSearchText: setSearchText,
            onDeleteTableItem: onDeleteTableItem,
            onEditTableItem: onEditTableItem,
            onAddTableItem: onAddTableItem,
            aulas: aulas,
            cursos: cursos,
            isLoading: isLoading
        }}>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar />
                <Body />
                {(showModal || editting) &&
                    <AddCursoForm />
                }
            </div>
        </CursoContext.Provider>
    );
}