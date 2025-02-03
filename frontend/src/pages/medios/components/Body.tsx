import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {MedioGetAdapter} from "../adapters/MedioGetAdapter.ts";
import {MedioContext} from "../MediosScreen.tsx";
import SolicitarIcon from "../../../assets/solicitar.svg";
import {useApiMedio} from "../hooks/useApiMedios.ts";
import AlertIcon from "../../../assets/alert.svg";
import {AppContext} from "../../../App.tsx";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(MedioContext)
    const {solicitarMedio} = useApiMedio()
    const {setError, medios} = useContext(AppContext)
    return(
            <Table
                className={'h-5/6 accentgree'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={MedioGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       console.log(item)
                       setEditting!(item!)
                   }}
                actions={[
                    {
                        action: (row) => {
                            solicitarMedio!({mean_id: row.id})
                        },
                        color: 'green',
                        title: "Solicitar",
                        icon: <img src={SolicitarIcon} alt={'Solicitar'}/>,
                        isVisible: ()=>true
                    },
                    {
                        action: () => {
                            setError!(new Error("Este profesor lleva mas de 3 años recibiendo malas valoraciones"))
                        },
                        color: 'bg-amber-500',
                        title: "Alerta",
                        icon: <img src={AlertIcon} alt={'Alerta'}/>,
                        isVisible: (row) => medios!.find!((medio) => medio.id === row)!.to_be_replaced
                    }
                ]}
            />
    )
}