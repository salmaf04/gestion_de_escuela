import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {NotasContext} from "../NotasScreen.tsx";
import {NotaAdapter} from "../adapters/NotaAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(NotasContext)
    const {allowRoles} = useContext(AppContext)
    let header: string[] = []
    if (allowRoles!([RolesEnum.STUDENT])) {
        header = ['Profesor', 'Asignatura', "Últ. Modificación", 'Nota']
    }else
    if (allowRoles!([RolesEnum.SECRETARY])) {
        header = NotaAdapter.Properties.slice(1)
    }else
        header = ['Estudiante', 'Asignatura', "Últ. Modificación", 'Nota']

    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []}
                header={header}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       if (allowRoles!([RolesEnum.SECRETARY, RolesEnum.TEACHER])) {
                           const item = dataTable!.find((item) => item.id === index)
                           setEditting!(item!)
                       }
                   }}
                isRemoveActive={allowRoles!([RolesEnum.SECRETARY, RolesEnum.TEACHER])}
            />
    )
}