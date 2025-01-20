import Table from "../../components/Table.tsx";
import {useContext} from "react";
import {EstudianteContext} from "../EstudiantesScreen.tsx";
import {EstudianteGetAdapter} from "../adapters/EstudianteGetAdapter.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(EstudianteContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={EstudianteGetAdapter.Properties.slice(1)}
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