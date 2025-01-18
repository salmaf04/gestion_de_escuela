import SearchInput from "../../components/SearchInput.tsx";
import AddButton from "../../components/AddButton.tsx";
import {useContext} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal
    } = useContext(ProfesorContext)
    return (
        <div className={'flex flex-col w-full h-1/6 justify-center'}>
            <div className={'self-end w-2/3 my-4 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>
                <AddButton onClick={() => setShowModal!(true)}/>
            </div>
        </div>
    )
}