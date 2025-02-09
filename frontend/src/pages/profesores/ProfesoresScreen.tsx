import {createContext, useContext, useEffect, useState} from "react";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {ProfesorCreateAdapter} from "./adapters/ProfesorCreateAdapter.ts";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {useApiProfesor} from "./hooks/useApiProfesor.ts";
import {AppContext} from "../../App.tsx";
import {IEditRow} from "../../types/IEditRow.ts";
import {useApiValorationPeriod} from "../info/hooks/useApiValorationPeriod.ts";

interface IProfesorContext {
    searchText?: string;
    dataTable?: IDataRow[];
    editting?: IEditRow<ProfesorCreateAdapter>;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (edit: IEditRow<ProfesorCreateAdapter> | undefined) => void;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
    onAddTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
}

interface IDataRow{
    id: string;
    name: string;
    lastname: string;
    specialty: string;
    contractType: string;
    experience: number;
    salary: number;
    email: string;
    username: string
    subjects: string[];
    valoracion: number;
}

export const ProfesorContext = createContext<IProfesorContext>(
    {}
);

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IEditRow<ProfesorCreateAdapter> | undefined>()
    const [showModal, setShowModal] = useState(false)
    const {getValorationPeriod} = useApiValorationPeriod()
    const {profesores} = useContext(AppContext)
    const {
        deleteProfesor,
        createProfesor,
        updateProfesor,
        getProfesores,
    } = useApiProfesor()
    useEffect(() => {
        getProfesores()
        getValorationPeriod()
    }, []);

    const onDeleteTableItem = (deletedProfesorId : string ) => {
        deleteProfesor(deletedProfesorId )
        getProfesores()
    }

    const onEditTableItem = (profesorEdit: ProfesorCreateAdapter) => {
        updateProfesor(editting!.id, profesorEdit)
        setEditting!(undefined);
    }

    const onAddTableItem = (profesor: ProfesorCreateAdapter) => {
        createProfesor(profesor)
    }

    const data: IDataRow[] = profesores?.map((p) => {
        return {
            id: p.id,
            name: p.name,
            lastname: p.lastname,
            specialty: p.specialty,
            contractType: p.contractType,
            experience: p.experience,
            salary: p.salary,
            email: p.email,
            username: p.username,
            subjects: p.subjects.map((item)=> item.name),
            valoracion: p.valoracion,
        }
    }) ?? []

    const [dataTable, setDataTable] = useState<IDataRow[]>(data ?? [])
    useEffect(() => {
        setDataTable(data!)
    }, [profesores]);
    useEffect(() => {
        setDataTable(
            data?.filter((row) => {
                return Object.values(row).some((value) => {
                    return value?.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }) ?? []
        )
    }, [searchText, profesores]);



    return (
        <ProfesorContext.Provider value={{
            dataTable: dataTable,
            searchText: searchText,
            editting: editting,
            showModal: showModal,
            setShowModal: setShowModal,
            setEditting: setEditting,
            setSearchText: setSearchText,
            onDeleteTableItem: onDeleteTableItem,
            onEditTableItem: onEditTableItem,
            onAddTableItem: onAddTableItem,
        }
        }>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar/>
                <Body />
                {(showModal || editting) &&
                    <AddProfesorForm />
                }
            </div>
        </ProfesorContext.Provider>
    )
}