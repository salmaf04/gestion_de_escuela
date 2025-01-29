import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {CursoContext} from "../CursosScreen.tsx";
import {CursoGetAdapter} from "../adapters/CursoGetAdapter.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(CursoContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={CursoGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       setEditting!(item!)
                   }}
            />
    )
}