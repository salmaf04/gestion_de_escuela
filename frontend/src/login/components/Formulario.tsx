import VisibilityOn from '../assets/visibility-on.svg';
import VisibilityOff from '../assets/visibility-off.svg';
import {useState} from "react";
import {useNavigate} from "react-router-dom";
import {getToken} from "../api/requests.ts";
import {TokenResponse} from "../api/types.ts";
import Alert from "../../components/Alert.tsx";
import Spinner from "../../components/Spinner.tsx";

interface User {
    username: string;
    password: string;
}

export default function Formulario() {
    const [user, setUser] = useState<User>({username: '', password: ''});
    const [isPassVisible, setIsPassVisible] = useState(false)
    const [isLoading, setIsLoading] = useState(false)
    const navigate = useNavigate()
    const [errorFetch, setErrorFetch] = useState('')
    return (
        <>
            {errorFetch && <Alert title={"Error"} message={errorFetch} onClick={() => setErrorFetch('')}/>}
            <form onSubmit={
                (e) => {
                    e.preventDefault();
                    setIsLoading(true)
                    getToken(user.username, user.password).then((res) => {
                        if (res.ok) {
                            res.json().then((res: TokenResponse) => {
                                console.log(res)
                                sessionStorage.setItem("token", res.access_token)
                                navigate('/main')
                            })
                        } else
                            res.json().then((r) => setErrorFetch(r.detail))
                    }).catch(() => {
                        setErrorFetch('Error de conexión')
                    })
                        .finally(() => setIsLoading(false))
                }
            } className={"size-full flex flex-col items-center justify-around p-10 text-indigo-500"}>
                <h1 className={" surface font-bold text-3xl"}>Iniciar Sesión</h1>
                <div className={"w-2/3 space-y-4 translate-y-2"}>
                    <div className={'group'}>
                        <h2 className={'text-indigo-500 text-xs font-semibold invisible group-focus-within:visible opacity-0 group-focus-within:opacity-100 translate-y-5 group-focus-within:translate-y-0 transition-all'}>
                            Usuario
                        </h2>
                        <input
                            value={user.username}
                            placeholder={"Usuario"} type="text"
                            required={true}
                            autoFocus={true}
                            className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}
                            onChange={
                                (newText) => {
                                    setUser(prevState => {
                                        return {...prevState, username: newText.target.value}
                                    })
                                }
                            }/>
                    </div>
                    <div className={'group'}>
                        <h2 className={'text-indigo-500 text-xs font-semibold opacity-0 invisible group-focus-within:visible group-focus-within:opacity-100 translate-y-5 group-focus-within:translate-y-0 transition-all'}>
                            Contraseña
                        </h2>
                        <div className={"relative flex items-center"}>

                            <input placeholder={"Contraseña"} type={isPassVisible ? "text" : "password"}
                                   value={user.password}
                                   required={true}
                                   onChange={
                                       (newText) => {
                                           setUser(prevState => {
                                               return {...prevState, password: newText.target.value}
                                           })
                                       }
                                   }
                                   className={" rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                            <img className={"absolute end-2 cursor-pointer scale-90"}
                                 alt={"Cambiar visibilidad"}
                                 onClick={
                                     (e) => {
                                         e.preventDefault();
                                         setIsPassVisible(!isPassVisible);
                                     }}
                                 src={isPassVisible ? VisibilityOff : VisibilityOn}/>
                        </div>
                    </div>

                </div>

                <button
                    className={`${isLoading ? 'from-indigo-300 to-indigo-300 cursor-default' : 'from-indigo-400 hover:from-indigo-500 hover:to-indigo-500 to-indigo-500 shadow-md shadow-indigo-300 hover:scale-105'} bg-gradient-to-br flex justify-center transition-all text-indigo-50 font-semibold  rounded-lg py-3 w-2/3`}
                    type={"submit"}
                >
                    {isLoading && <Spinner />}
                    <p className={`${isLoading ? 'invisible' : 'visible'}`}>
                        Iniciar Sesión
                    </p>
                </button>
            </form>
        </>

    )
}