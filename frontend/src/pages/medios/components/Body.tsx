import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {MedioGetAdapter} from "../adapters/MedioGetAdapter.ts";
import {MedioContext} from "../MediosScreen.tsx";
import SolicitarIcon from "../../../assets/solicitar.svg";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(MedioContext)
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
                            console.log(row)
                        },
                        color: 'green',
                        title: "Solicitar",
                        icon: <img src={SolicitarIcon} alt={'Solicitar'}/>
                    }
                ]}
            />
    )
}