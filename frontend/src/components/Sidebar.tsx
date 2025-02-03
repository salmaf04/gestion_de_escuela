import ScreenType from "../types.ts";
import {Screens} from "../utils/router.ts";
import {useLocation, useNavigate} from "react-router-dom";
import {useContext} from "react";
import {AppContext} from "../App.tsx";

function Sidebar() {
    const location = useLocation()
    const navigate = useNavigate()
    const {allowRoles} = useContext(AppContext)
    return <div className={"h-full flex items-center px-4"}>
        <div className={'flex flex-col items-center justify-center h-4/5'}>
            {
                Object.values(Screens).filter((item) => allowRoles!(item.allowedRoles)).map((screen: ScreenType) => {
                    return (
                        <div key={screen.title} onClick={() => navigate(screen.path)}
                             className={`transition-all cursor-pointer font-semibold px-3 size-full space-y-1 justify-center rounded-xl flex flex-col items-center ${location.pathname === screen.path ? 'bg-indigo-100' : ''}`}>
                            <img src={screen.icon} alt={screen.title} className={'size-7'}/>
                            <p className={'text-xs text-indigo-950'}>{screen.title}</p>
                        </div>)
                })
            }

        </div>
    </div>;
}

export default Sidebar