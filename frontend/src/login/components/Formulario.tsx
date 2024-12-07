import VisibilityOn from '/visibility-on.svg';
import VisibilityOff from '/visibility-off.svg';
import { useState} from "react";
import {useNavigate} from "react-router-dom";

interface User {
    username: string;
    password: string;
}

export default function Formulario() {
    const [user, setUser] = useState<User>({username: '', password: ''});
    const [isPassVisible, setIsPassVisible] = useState(false)
    const [isLoading, setIsLoading] = useState(false)
    const navigate = useNavigate()
    return <form onSubmit={
        (e) => {
            e.preventDefault();
            setIsLoading(true)
            fetch('https://0c3d9c50-6ab6-4266-beae-94adbb883f39.mock.pstmn.io/get').then((res)=>{
                setIsLoading(false)
                res.text().then((text)=>{
                    setUser({username: text, password: ''})
                    sessionStorage.setItem('username', user.username);
                    sessionStorage.setItem('password', user.password);
                    navigate('/')
                })
                console.log(res.text())
            })
        }
    } className={"size-full flex flex-col items-center justify-around p-10 text-indigo-500"}>
        <h1 className={" surface font-bold text-3xl"}>Iniciar Sesión</h1>
        <div className={"w-2/3 space-y-4 translate-y-2"}>
            <div className={'group'}>
                <h2 className={'text-indigo-500 text-xs font-semibold opacity-0 group-focus-within:opacity-100 translate-y-5 group-focus-within:translate-y-0 transition-all'}>
                    Usuario
                </h2>
                <input
                    value={user.username}
                    placeholder={"Usuario"} type="text"
                    required={true}
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
                <h2 className={'text-indigo-500 text-xs font-semibold opacity-0 group-focus-within:opacity-100 translate-y-5 group-focus-within:translate-y-0 transition-all'}>
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
            className={`${isLoading ? 'from-indigo-300 to-indigo-300' : 'from-indigo-400 hover:from-indigo-500 hover:to-indigo-500 to-indigo-500 shadow-md shadow-indigo-300 hover:scale-105'} bg-gradient-to-br  transition-all text-indigo-50 font-semibold  rounded-lg py-3 w-2/3`}
            type={"submit"}
        >
            Iniciar Sesión
        </button>
        {/*<DotLottieReact
                            src='/loading-button-animation.lottie'
                            loop
                            autoplay
                        />*/}


    </form>;
}