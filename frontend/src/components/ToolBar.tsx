
import { useContext } from "react";
import SearchInput from "./SearchInput.tsx";
import AddButton from "./AddButton.tsx";
import {AppContext} from "../App.tsx";
import UserIcon from "../assets/user.svg";

export interface IToolbarContext {
    searchText?: string;
    setSearchText?: (text: string) => void;
    setShowModal?: (show: boolean) => void;
}

export default function ToolBar({context} : {context: React.Context<IToolbarContext> }) {
    const {
        searchText,
        setSearchText,
        setShowModal
    } = useContext(context);
    const {username, setToken} = useContext(AppContext)
    return (
        <div className={'w-full my-4 h-1/6 flex items-center justify-between px-5'}>
            <div className={'flex space-x-4'}>
                <div className={'flex flex-col items-center space-y-2'}>
                    <img src={UserIcon} alt={'usuario'}/>
                    <p className={'text-xs underline font-semibold text-slate-600 cursor-pointer'}
                       onClick={() => {
                           setToken!("")
                           sessionStorage.removeItem('token')
                       }}
                    >
                        Cerrar Sesión
                    </p>
                </div>
                <div className={'flex flex-col '}>
                    <h1 className={'text-3xl text-indigo-600 accent-i font-bold'}>
                        Bienvenido/a
                    </h1>
                    <p className={'text-slate-800 text-sm italic'}>
                        {username}
                    </p>

                </div>
            </div>

            <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                setSearchText!(text);
            }}/>
            <AddButton onClick={() => setShowModal!(true)}/>
        </div>
    );
}