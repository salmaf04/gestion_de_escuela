import VisibilityOn from '/visibility-on.svg';
import VisibilityOff from '/visibility-off.svg';
import { useState} from "react";

interface User {
    username: string;
    password: string;
}

export default function Formulario() {
    const [user, setUser] = useState<User>({username: '', password: ''});
    const [isPassVisible, setIsPassVisible] = useState(false)
    const [isLoading, setIsLoading] = useState(false)
    return <form onSubmit={
        (e) => {
            e.preventDefault();
            setIsLoading(true)
            fetch('https://0c3d9c50-6ab6-4266-beae-94adbb883f39.mock.pstmn.io/get').then((res)=>{
                setIsLoading(false)
                res.text().then((text)=>{
                    setUser({username: text, password: ''})
                })
                console.log(res.text())
            })
        }
    } className={"size-full flex flex-col items-center justify-around p-10 text-indigo-400"}>
        <h1 className={"text-indigo-400 surface font-bold text-4xl"}>Bienvenido</h1>
        <div className={"w-2/3 space-y-8 translate-y-4"}>
            <div>
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

        <button
            className={`${isLoading? 'bg-indigo-200': 'bg-indigo-400 shadow-md'}  shadow-indigo-300 transition-all text-indigo-50 font-semibold hover:scale-105 rounded-lg py-3 w-2/3 hover:bg-indigo-500`}
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