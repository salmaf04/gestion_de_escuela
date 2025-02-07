import { EstudianteGetAdapter } from "../adapters/EstudianteGetAdapter.ts";
import Table from "../../../components/Table.tsx";
import { useContext } from "react";
import { EstudianteContext } from "../EstudiantesScreen.tsx";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body() {
    const { dataTable, setEditting, onDeleteTableItem, isGetLoading } = useContext(EstudianteContext);
    const {allowRoles} = useContext(AppContext)

    return (
        <Table
            className={'h-5/6'}
            isLoading={isGetLoading!}
            Data={dataTable ?? []}
            header={EstudianteGetAdapter.Properties.slice(1)}
            onRemoveRow={(index) => {
                onDeleteTableItem!(index);
            }}
            onEditRow={(index) => {
                if (allowRoles!([RolesEnum.SECRETARY])) {
                    const item = dataTable!.find((item) => item.id === index);
                    setEditting!({id: index, body: item!});
                }
            }}
            isRemoveActive={allowRoles!([RolesEnum.SECRETARY])}
        />
    );
}