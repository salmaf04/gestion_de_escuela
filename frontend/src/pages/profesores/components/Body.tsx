import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import Table from "../../../components/Table.tsx";
import {useContext, useState} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";
import {useApiProfesor} from "../hooks/useApiProfesor.ts";
import ValorarIcon from "../../../assets/valorar.svg";
import {AppContext} from "../../../App.tsx";
import ValorarModal from "./ValorarModal.tsx";
import {DBObject} from "../../../types.ts";

export default function Body() {
    const {dataTable, setEditting, onDeleteTableItem} = useContext(ProfesorContext)
    const {isLoading} = useApiProfesor()
    const {valorarProfesor} = useApiProfesor()
    const {personalId} = useContext(AppContext)
    const [showValoration, setShowValoration] = useState(false)
    const [profesor, setProfesor] = useState<DBObject>()
    return (
        <>
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
                            setShowValoration(true)
                            setProfesor(row)
                        },
                        color: 'amber',
                        title: "Valorar",
                        icon: <img src={ValorarIcon} alt={'Valorar'}/>
                    }
                ]}
            />
            {
                showValoration && <ValorarModal profesor={profesor} setShowModal={setShowValoration}/>
            }
        </>


)
}