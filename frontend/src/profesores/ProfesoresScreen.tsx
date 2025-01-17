import {useEffect, useState} from "react";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import Table from "../components/Table.tsx";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {deleteProfesor, getProfesores, postProfesor} from "./api/requests.ts";
import Alert from "../components/Alert.tsx";
import Spinner from "../components/Spinner.tsx";
import {ProfesorGetAdapter} from "./adapters/ProfesorGetAdapter.ts";
import {getProfesorFromResponse} from "./utils/utils.ts";

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [dataTable, setDataTable] = useState<ProfesorGetAdapter[]>([]);
    const [dataTableShow, setDataTableShow] = useState<ProfesorGetAdapter[]>(dataTable);
    const [isTableLoading, setIsTableLoading] = useState(false)
    useEffect(() => {
        setDataTableShow(dataTable)
    }, [dataTable]);
    //
    useEffect(() => {
        if (searchText){
            setDataTableShow(
                [...dataTable].filter((row) => {
                    return Object.values(row).some((value) => {
                        return value.toString().toLowerCase().includes(searchText.toLowerCase())
                    })
                }))
        } else {
            setDataTableShow(dataTable)
        }
    }, [searchText]);
    useEffect(() => {
        setIsTableLoading(true)
        getProfesores().then(res => {
            setDataTable(getProfesorFromResponse(res))
            console.log(res)
        }).catch((e) => {
            setError(e)
        }).finally(()=> setIsTableLoading(false))/*
        setDataTable(dataExample)
        setDataTableShow(dataExample)*/
    }, []);
    const [isAdding, setIsAdding] = useState(false);
    const [editing, setEditing] = useState<ProfesorGetAdapter | null>(null);
    const [isLoading, setisLoading] = useState(false);
    const [error, setError] = useState('')
    return (
        <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>
            {
                error && <Alert title={'Error:'} message={error} className={'bg-red-200'} onClick={() => {
                    setError('')
                }}/>
            }
            {isAdding && <AddProfesorForm
                onAccept={(formData) => {
                    setisLoading(true)
                    postProfesor(formData).then(res => {
                        if (res.ok) {
                            res.json().then((data: ProfesorGetAdapter) => {
                                setDataTable([...dataTable, data])
                                setIsAdding(false)
                            })
                        } else {
                            setError(res.statusText)
                        }
                    }).finally(() => {
                        setisLoading(false)
                    })


                }}
                isLoading={isLoading}
                onCancel={() => setIsAdding(false)}
            />}
            {editing && <AddProfesorForm
                isLoading={isLoading}
                onAccept={(formData) => {
                    //todo PUT request Profesor
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
            {
                isTableLoading && <Spinner />
            }
            <Table className={'h-5/6'} Data={dataTableShow} header={ProfesorGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       deleteProfesor(index).then(res => {
                           if (res.ok) {
                               setDataTable(dataTable.filter((item) => {
                                   return item.id !== index
                               }))
                           } else {
                               setError(res.statusText)
                           }
                       })
                   }}
                   onEditRow={(index) => {
                       setEditing(
                           dataTable.find((item) => item.id === index) || null
                       )
                   }}
            />
        </div>
    )
}