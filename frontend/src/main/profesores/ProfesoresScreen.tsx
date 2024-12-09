import {useEffect, useState} from "react";
import {data, header} from "../estudiantes/data/Example_data.tsx";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import Table from "../components/Table.tsx";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {Profesor} from "../types.ts";
import {postProfesor} from "./api/requests.ts";
import Alert from "../components/Alert.tsx";

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [dataTable, setDataTable] = useState(data);
    useEffect(() => {
        fetch('http://localhost:8000/teacher/')
    }, []);
    useEffect(() => {
        setDataTable(
            [...data].filter((row) => {
                return Object.values(row).some((value) => {
                    return value.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }))
    }, [searchText]);
    const [isAdding, setIsAdding] = useState(false);
    const [editing, setEditing] = useState<Profesor | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState('')
    return (
        <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>
            {
                error && <Alert title={'Error:'} message={error} className={'bg-red-200'} onClick={()=>{setError('')}} />
            }
            {isAdding && <AddProfesorForm
                onAccept={(formData) => {
                    //todo POST request Profesor
                    setIsLoading(true)
                    postProfesor(formData).then(res => {
                        if (res.ok) {
                            console.log(res)
                            setDataTable([...dataTable, formData])
                            setIsAdding(false)
                            setIsLoading(false)
                        }else {
                            setError(res.statusText)
                        }
                    }).finally(() => {
                        setIsLoading(false)
                    })


                }}
                isLoading={isLoading}
                onCancel={() => setIsAdding(false)}
            />}
            {editing && <AddProfesorForm
                isLoading={isLoading}
                onAccept={(formData) => {
                    //todo PUT request Profesor

                    setDataTable(dataTable.map((item) => item.Id === formData.Id ? formData : item));
                    setEditing(null)
                }}
                formDataEdit={editing}
                onCancel={() => setEditing(null)}
            />}
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText} setSearchText={(text: string) => {
                    setSearchText(text)
                }}/>
                <AddButton onClick={() => setIsAdding(true)}/>
            </div>
            <Table className={'h-5/6'} Data={dataTable} header={header}
                   onRemoveRow={(index) => {
                       //todo DELETE request Profesor
                       console.log('delete')
                       setDataTable(dataTable.filter((item) => {
                           return item.Id !== index
                       }))
                   }}
                   onEditRow={(index) => {
                       setEditing(
                           dataTable.find((item) => item.Id === index) || null
                       )
                   }}
            />
        </div>
    )
}