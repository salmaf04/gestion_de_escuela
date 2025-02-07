import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {CursoContext} from "../CursosScreen.tsx";
import {CursoGetAdapter} from "../adapters/CursoGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(CursoContext)
    const {allowRoles} = useContext(AppContext)

    return(
            <Table
                className={'h-5/6'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={CursoGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       if (allowRoles!([RolesEnum.SECRETARY])) {
                           const item = dataTable!.find((item) => item.id === index)
                           setEditting!(item!)
                       }
                   }}
                isRemoveActive={allowRoles!([RolesEnum.SECRETARY])}
            />
    )
}