import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {NotasContext} from "../NotasScreen.tsx";
import {NotaGetAdapter} from "../adapters/NotaGetAdapter.ts";

export default function Body(){
    const {dataTable,  setEditting, onDeleteTableItem, isGetLoading} = useContext(NotasContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={NotaGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       console.log(item)
                       setEditting!(item!)
                   }}
            />
    )
}