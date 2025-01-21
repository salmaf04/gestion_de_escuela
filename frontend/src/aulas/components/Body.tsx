import Table from "../../components/Table.tsx";
import {useContext} from "react";
import {AulaContext} from "../AulasScreen.tsx";
import {AulaGetAdapter} from "../adapters/AulaGetAdapter.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(AulaContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={AulaGetAdapter.Properties.slice(1)}
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