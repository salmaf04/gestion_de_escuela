import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {NotasContext} from "../NotasScreen.tsx";
import {NotaAdapter} from "../adapters/NotaAdapter.ts";

export default function Body(){
    const {dataTable,  setEdittingId, onDeleteTableItem, isGetLoading} = useContext(NotasContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={NotaAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       setEdittingId!(item!.id)
                   }}
            />
    )
}