import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import Table from "../../../components/Table.tsx";
import {useContext, useState} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";
import {useApiProfesor} from "../hooks/useApiProfesor.ts";
import AlertIcon from "../../../assets/alert.svg";
import ValorarIcon from "../../../assets/valorar.svg";
import ValorarModal from "./ValorarModal.tsx";
import {DBObject} from "../../../types.ts";
import {AppContext} from "../../../App.tsx";

export default function Body() {
    const {dataTable, setEditting, onDeleteTableItem} = useContext(ProfesorContext)
    const {isLoading} = useApiProfesor()
    const [showValoration, setShowValoration] = useState(false)
    const [profesor, setProfesor] = useState<DBObject>()
    const {setError, profesores} = useContext(AppContext)
    console.log(dataTable)
    return (
        <>
            <Table
                className={'h-5/6 amber accengree'}
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
                        lineColor: 'bg-green-500',
                        hoverColor: 'bg-green-100',
                        title: "Valorar",
                        icon: <img src={ValorarIcon} alt={'Valorar'}/>,
                        isVisible: () => true
                    },
                    {
                        action: () => {
                            setError!(new Error("Este profesor lleva mas de 3 años recibiendo malas valoraciones"))
                        },
                        lineColor: 'bg-amber-500',
                        hoverColor: 'bg-amber-100',
                        title: "Alerta",
                        icon: <img src={AlertIcon} alt={'Alerta'}/>,
                        isVisible: (row) => profesores!.find!((profesor) => profesor.id === row)!.alert > 5
                    }
                ]}
            />
            {
                showValoration && <ValorarModal profesor={profesor} setShowModal={setShowValoration}/>
            }
        </>


)
}