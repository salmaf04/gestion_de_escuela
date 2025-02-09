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
import SancionIcon from "../../../assets/sanction.svg"
import SancionModal from "./SancionModal.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body() {
    const {dataTable, setEditting, onDeleteTableItem} = useContext(ProfesorContext)
    const {isLoading} = useApiProfesor()
    const [showValoration, setShowValoration] = useState(false)
    const [showSancion, setShowSancion] = useState(false)
    const [profesor, setProfesor] = useState<DBObject>()
    const {setError, profesores, allowRoles, typeRole, valorationPeriod} = useContext(AppContext)

    let data = []
    const actions = []
    let header = ProfesorGetAdapter.Properties.slice(1)
    if (allowRoles!([RolesEnum.STUDENT])){
        header = ["Nombre", "Apellidos", "Especialidad", "Asignaturas", "Valoración"]
        data = dataTable!.map((p) =>{
            return {
                id: p.id,
                name: p.name,
                lastname: p.lastname,
                specialty: p.specialty,
                subjects: p.subjects,
                valoracion: p.valoracion,
            }
        })
        actions.push({
            action: (row: DBObject) => {
                setShowValoration(true)
                setProfesor(row)
            },
            lineColor: 'bg-green-500',
            hoverColor: 'hover:bg-green-100',
            title: "Valorar",
            icon: <img src={ValorarIcon} alt={'Valorar'}/>,
            isVisible: () => valorationPeriod!.open
        })
    }else{
        data = dataTable!
    }
    if (typeRole === "dean"){
        actions.push(
            {
                action: () => {
                    setError!(new Error("Este profesor lleva más de 5 años recibiendo malas valoraciones"))
                },
                lineColor: 'bg-amber-500',
                hoverColor: 'hover:bg-amber-100',
                title: "Alerta",
                icon: <img src={AlertIcon} alt={'Alerta'}/>,
                isVisible: (row: string) => profesores!.find!((profesor) => profesor.id === row)!.alert > 5
            },
            {
                action: (item: DBObject) => {
                    setProfesor(item)
                    setShowSancion(true)
                },
                lineColor: 'bg-red-700',
                hoverColor: 'hover:bg-red-100',
                title: "Sancionar",
                icon: <img src={SancionIcon} alt={'Sancionar'}/>,
                isVisible: () => true
            })
    }
    console.log(dataTable)
    return (
        <>
            <Table
                className={'h-5/6'}
                isLoading={isLoading}
                Data={data ?? []}
                header={header}
                onRemoveRow={(index) => {
                    onDeleteTableItem!(index)
                }}
                onEditRow={(index) => {
                    if (allowRoles!([RolesEnum.SECRETARY])){
                        const item = dataTable!.find((item) => item.id === index)
                        setEditting!({id: index, body: item!})
                    }

                }}
                actions={actions}
                isRemoveActive={allowRoles!([RolesEnum.SECRETARY])}
            />
            {
                showValoration && <ValorarModal profesor={profesor} setShowModal={setShowValoration}/>
            }
            {
                showSancion && <SancionModal profesor={profesor} setShowModal={setShowSancion}/>
            }
        </>


    )
}