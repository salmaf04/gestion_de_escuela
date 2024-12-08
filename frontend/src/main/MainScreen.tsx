import {useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";
import Navbar from "./components/Navbar.tsx";
import Sidebar from "./components/Sidebar.tsx";
import Content from "./components/Content.tsx";
import ScreenType, {Screens} from "./types.ts";

export default function MainScreen() {
    const navigate = useNavigate()
    useEffect(() => {
        if (!sessionStorage.getItem('username')) {
            navigate('/login')
        }
    });
    const name = sessionStorage.getItem('username');
    const [actualScreen, setActualScreen] = useState<ScreenType>(Screens.Inicio)
    return (
        <div className={' bg-indigo-50'}>
            <Navbar name={name || ''}/>
            <div className={'flex'}>
                <Sidebar actualScreen={actualScreen} setActualScreen={setActualScreen} />
                <Content actualScreen={actualScreen}/>
            </div>
        </div>
    )
}