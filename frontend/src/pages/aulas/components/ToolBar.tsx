import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {AulasContext} from "../AulasScreen.tsx";
import {AulaGetAdapter} from "../../aulas/adapters/AulaGetAdapter.ts";
import ExportButton from "../../../components/ExportButton.tsx";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable
    } = useContext(AulasContext)
    return (
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}

                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>
                <ExportButton title={'Aulas'} headers = {AulaGetAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
                <AddButton onClick={() => setShowModal!(true)}/>
            </div>
    )
}