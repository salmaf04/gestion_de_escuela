import {useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";
import Sidebar from "./components/Sidebar.tsx";
import Content from "./components/Content.tsx";
import {Screens} from "./router.tsx";
import ScreenType from "./types.ts";

export default function MainScreen() {
    const navigate = useNavigate()
    useEffect(() => {
        if (!sessionStorage.getItem('username')) {
            navigate('/login')
        }
    });
    //const name = sessionStorage.getItem('username');
    const [actualScreen, setActualScreen] = useState<ScreenType>(Screens.Estudiantes)
    return (
        <div className={'h-dvh bg-indigo-50 flex'}>
            <Sidebar actualScreen={actualScreen} setActualScreen={setActualScreen}/>
            <Content actualScreen={actualScreen}/>
        </div>
    )
}