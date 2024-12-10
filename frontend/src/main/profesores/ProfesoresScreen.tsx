import {useEffect, useState} from "react";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import Table from "../components/Table.tsx";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {deleteProfesor, getProfesores, postProfesor} from "./api/requests.ts";
import Alert from "../../components/Alert.tsx";
import {ProfesorGet} from "./dto/types.ts";

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [dataTable, setDataTable] = useState<ProfesorGet[]>([]);
    useEffect(() => {
        getProfesores().then(res => {
            const x: ProfesorGet[] = []
            let i = 0;
            while (res[i]) {
                x.push(res[i])
                i++
            }
            setDataTable(x)
        })
    }, []);
    useEffect(() => {
        setDataTable(
            [...dataTable].filter((row) => {
                return Object.values(row).some((value) => {
                    return value.toString().toLowerCase().includes(searchText.toLowerCase())
                })
            }))
    }, [searchText]);
    const [isAdding, setIsAdding] = useState(false);
    const [editing, setEditing] = useState<ProfesorGet | null>(null);
    const [isLoading, setIsLoading] = useState(false);
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
                    setIsLoading(true)
                    postProfesor(formData).then(res => {
                        if (res.ok) {
                            res.json().then((data: ProfesorGet) => {
                                setDataTable([...dataTable, data])
                                setIsAdding(false)
                            })
                        } else {
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
            <Table className={'h-5/6'} Data={dataTable} header={ProfesorGet.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       deleteProfesor(index).then(res => {
                           if (res.ok) {
                               setDataTable(dataTable.filter((item) => {
                                   return item.id !== index
                               }))
                           }else{
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