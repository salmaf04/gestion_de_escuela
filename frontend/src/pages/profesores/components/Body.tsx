import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";
import {useApiProfesor} from "../hooks/useApiProfesor.ts";
import ValorarIcon from "../../../assets/valorar.svg";

export default function Body() {
    const {dataTable, setEditting, onDeleteTableItem} = useContext(ProfesorContext)
    const {isLoading} = useApiProfesor()
    return (
        <Table
            className={'h-5/6'}
            isLoading={isLoading}
            Data={dataTable ?? []}
            header={ProfesorGetAdapter.Properties.slice(1)}
            onRemoveRow={(index) => {
                onDeleteTableItem!(index)
            }}
            onEditRow={(index) => {
                const item = dataTable!.find((item) => item.id === index)
                setEditting!({id: index, body: item!})
            }}
            actions={[
                {
                    action: (row) => {
                        console.log(row)
                    },
                    color: 'amber',
                    title: "Valorar",
                    icon: <img src={ValorarIcon} alt={'Valorar'}/>
                }
            ]}
        />
    )
}