import {useEffect, useState} from "react";
import {data, header} from "./data/Example_data.tsx";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import Table from "../components/Table.tsx";
import AddProfesorForm from "./components/AddProfesorForm.tsx";
import {Profesor} from "../types.ts";

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [dataTable, setDataTable] = useState(data);
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
    return (
        <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>
            {isAdding && <AddProfesorForm
                onAccept={(formData) => {
                    //todo POST request Profesor
                    setDataTable([...dataTable, formData])
                    setIsAdding(false)
                }}

                onCancel={() => setIsAdding(false)}
            />}
            {editing && <AddProfesorForm
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
                            dataTable.find((item) => item.Id === index) || new Profesor('', '', '', '', '', '', '', '')
                        )
                   }}
            />
        </div>
    )
}