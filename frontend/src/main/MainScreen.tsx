import {useEffect} from "react";
import {useNavigate} from "react-router-dom";

export default function MainScreen() {
    const navigate = useNavigate()
    useEffect(() => {
        if (!sessionStorage.getItem('username')) {
            navigate('/login')
        }
    });
    return (
        <div>
            <h1>Esto es la pantalla principal</h1>
        </div>
    )
}