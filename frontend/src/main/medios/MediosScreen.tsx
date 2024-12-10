import {useEffect, useState} from "react";
import {data, header} from "./data/Example_data.tsx";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import Table from "../components/Table.tsx";
import AddMediosForm from "./components/AddMediosForm.tsx";
import {Medio} from "../types.ts";
import AddMediosForm from "../solicitud_medios/components/AddMediosForm.tsx";

export default function MediosScreen() {
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

    const [editing, setEditing] = useState<Medio | null>(null);
    return (
        <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>
            {isAdding && <AddMediosForm
                onAccept={(formData) => {
                    //todo POST request Medio
                    setDataTable([...dataTable, formData])
                    setIsAdding(false)
                }}

                onCancel={() => setIsAdding(false)}
            />}
            {editing && <AddMediosForm
                onAccept={(formData) => {
                    //todo PUT request Medio
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
                       //todo DELETE request Medio
                       console.log('delete')
                       setDataTable(dataTable.filter((item) => {
                           return item.Id !== index
                       }))
                   }}
                   onEditRow={(index) => {
                        setEditing(
                            dataTable.find((item) => item.Id === index) || new Medio('', '', '', '')
                        )
                   }}
            />
        </div>
    )
}