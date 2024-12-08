import Table from "../components/Table.tsx";
import {data, header} from "./data/Example_data.tsx";
import SearchInput from "../components/SearchInput.tsx";
import AddButton from "../components/AddButton.tsx";
import {useEffect, useState} from "react";
import AddForm from "./components/AddForm.tsx";

export default function EstudiantesScreen() {
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
    return (
        <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>
            {isAdding && <AddForm />}
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText} setSearchText={(text: string)=>{
                    setSearchText(text)
                }} />
                <AddButton onClick={()=> setIsAdding(!isAdding)} />
            </div>
                <Table className={'h-5/6'} Data={dataTable} header={header}/>
        </div>
    )
}