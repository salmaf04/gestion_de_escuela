import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {NotasContext} from "../NotasScreen.tsx";
import ExportButton from "../../../components/ExportButton.tsx";
import {NotaAdapter} from "../adapters/NotaAdapter.ts";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable
    } = useContext(NotasContext)
    return (
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>
                <ExportButton title={'Notas'} headers = {NotaAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
                <AddButton onClick={() => setShowModal!(true)}/>
            </div>
    )
}