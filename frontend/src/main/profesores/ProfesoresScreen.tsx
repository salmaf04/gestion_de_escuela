import {useEffect, useState} from "react";
import {data, header} from "../estudiantes/data/Example_data.tsx";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import Table from "../components/Table.tsx";

export default function ProfesoresScreen(){
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
    return (
        <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText} setSearchText={(text: string)=>{
                    setSearchText(text)
                }} />
                <AddButton />
            </div>
            <Table className={'h-5/6'} Data={dataTable} header={header}></Table>

        </div>
    )
}