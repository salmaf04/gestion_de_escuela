import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {CursoContext} from "../CursosScreen.tsx";
import ExportButton from "../../../components/ExportButton.tsx";
import {CursoGetAdapter} from "../adapters/CursoGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable,

    } = useContext(CursoContext)
    const headers =CursoGetAdapter.Properties.slice(1)
    const {allowRoles} = useContext(AppContext)

    return (
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>
                <ExportButton title={'Cursos'} headers = {headers} data={dataTable}></ExportButton>
                {allowRoles!([RolesEnum.SECRETARY]) &&
                    <AddButton onClick={() => setShowModal!(true)}/>
                }
            </div>
    )
}