import {useEffect, useState} from "react";
import {data, header} from "./data/Example_data.tsx";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import Table from "../components/Table.tsx";
import AddEstudianteForm from "./components/AddEstudianteForm.tsx";
import {Estudiante} from "../types.ts";
import {getEstudiantes} from "./api/requests.ts";
import {getEstudianteFromResponse} from "./utils/utils.ts";
import {EstudianteGetAdapter} from "./adapters/EstudianteGetAdapter.ts";
import Alert from "../components/Alert.tsx";

export default function EstudiantesScreen() {
    const [dataTable, setDataTable ] = useState<EstudianteGetAdapter[]>([]);
    const [error, setError] = useState('')
    useEffect(() => {

        getEstudiantes().then(res => {
            setDataTable(getEstudianteFromResponse(res))
        }).catch((e) => {
            setError(e)
        })/*
        setDataTable(dataExample)
        setDataTableShow(dataExample)*/
    }, []);

    const [isAdding, setIsAdding] = useState(false);

    const [editing, setEditing] = useState<EstudianteGetAdapter | null>(null);
    return (

        <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>
            {
                error && <Alert title={'Error:'} message={error} className={'bg-red-200'} onClick={() => {
                    setError('')
                }}/>
            }
            {isAdding && <AddEstudianteForm
                onAccept={(formData) => {
                    //todo POST request Estudiante
                    setDataTable([...dataTable, formData])
                    setIsAdding(false)
                }}

                onCancel={() => setIsAdding(false)}
            />}
            {editing && <AddEstudianteForm
                onAccept={(formData) => {

                }}
                formDataEdit={editing}
                onCancel={() => setEditing(null)}
            />}
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}

                <AddButton onClick={() => setIsAdding(true)}/>
            </div>
            <Table className={'h-5/6'} Data={dataTable} header={header}
                   onRemoveRow={(index) => {
                       //todo DELETE request Estudiante
                       console.log('delete')
                       setDataTable(dataTable.filter((item) => {
                           return item.id !== index
                       }))
                   }}
                   onEditRow={(index) => {
                        setEditing(
                            dataTable.find((item) => item.id === index) || new Estudiante('', '', '', false)
                        )
                   }}
            />
        </div>
    )
}