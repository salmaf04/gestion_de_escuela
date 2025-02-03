import {createContext, useContext, useEffect, useMemo, useState} from "react";
import Body from "./components/Body.tsx";
import {AppContext} from "../../App.tsx";
import AddEstudianteForm from "./components/AddEstudianteForm.tsx";
import {useApiEstudiante} from "./hooks/useApiEstudiante.ts";
import {IEditRow} from "../../types/IEditRow.ts";
import {IEstudianteLocal} from "./models/IEstudianteLocal.ts";
import {IEstudianteDB} from "./models/IEstudianteDB.ts";
import {IEstudianteCreateDB} from "./models/IEstudianteCreateDB.ts";
import ToolBar, {IToolbarContext} from "../../components/ToolBar.tsx";
import {RolesEnum} from "../../api/RolesEnum.ts";


interface IEstudianteContext extends IToolbarContext{
    searchText?: string;
    dataTable?: IEstudianteTableRow[];
    editting?: IEditRow<Partial<IEstudianteLocal>>;
    showModal?: boolean;
    setShowModal?: (text: boolean) => void;
    setEditting?: (estudiante?: IEditRow<Partial<IEstudianteTableRow>>) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (estudianteEdit: Partial<IEstudianteLocal>) => void;
    onAddTableItem?: (estudianteEdit: Partial<IEstudianteLocal>) => void;
    isEditting?: boolean;
    isCreatting?: boolean;
}

interface IEstudianteTableRow{
    id: string;
    name: string;
    lastname: string
    age: number;
    email: string;
    extra_activities: boolean;
    username: string;
    course_year: number;
}

export const EstudianteContext = createContext<IEstudianteContext>({});

export default function EstudiantesScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<IEditRow<Partial<IEstudianteLocal>> | undefined>();
    const [showModal, setShowModal] = useState(false);
    const {estudiantes, allowRoles} = useContext(AppContext)
    const {
        getEstudiantes,
        deleteEstudiante,
        updateEstudiante,
        createEstudiante,
        isLoading
    } = useApiEstudiante()

    useEffect(() => {
        getEstudiantes!();
    }, []);

    const onDeleteTableItem = (deletedEstudianteId: string) => {
        deleteEstudiante(deletedEstudianteId);
    };

    const onEditTableItem = (estudianteEdit: Partial<IEstudianteLocal>) => {
        const toEdit: Partial<IEstudianteDB> = {
            ...estudianteEdit,
            course_id: estudianteEdit.course?.id
        }
        updateEstudiante(editting!.id, estudianteEdit);
        setEditting!(undefined);
    };

    const onAddTableItem = (estudiante: Partial<IEstudianteCreateDB>) => {
        const toCreate: Partial<IEstudianteCreateDB> = {
            ...estudiante,
            course_id: estudiante.course_id
        }
        createEstudiante(toCreate);
    };
    const [dataTable, setDataTable] = useState<IEstudianteTableRow[]>([])

    const data = useMemo<IEstudianteTableRow[]>(() => {
        return estudiantes?.map((item) => {
            return {
                id: item.id,
                name: item.name,
                lastname: item.lastname,
                age: item.age,
                email: item.email,
                extra_activities: item.extra_activities,
                username: item.username,
                course_year: item.course?.year,
            }
        }) ?? []
    }, [estudiantes]);

    useEffect(() => {

        setDataTable(data)
    }, [estudiantes]);
    useEffect(() => {
        const filteredData = data?.filter((item) => {
            return Object.values(item).some((value) =>
                value?.toString().toLowerCase().includes(searchText.toLowerCase())
            );
        }) ?? [];
        setDataTable(filteredData);
    }, [searchText, estudiantes]);
    return (
        <EstudianteContext.Provider value={{
            isGetLoading: isLoading,
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

        }}>
            <div className={'w-full h-dvh flex flex-col'}>
                <ToolBar context={EstudianteContext} allowAddButton={allowRoles!([RolesEnum.SECRETARY])} />
                <Body />
                {(showModal || editting) &&
                    <AddEstudianteForm />
                }
            </div>
        </EstudianteContext.Provider>
    );
}