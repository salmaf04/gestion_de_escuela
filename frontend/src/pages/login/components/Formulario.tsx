import VisibilityOn from '../assets/visibility-on.svg';
import VisibilityOff from '../assets/visibility-off.svg';
import {useState} from "react";
import Spinner from "../../../components/Spinner.tsx";
import {useLogin} from "../hooks/useLogin.ts";
import {SubmitHandler, useForm} from 'react-hook-form';

interface IUser {
    username: string;
    password: string;
}

export default function Formulario() {
    const {getToken, isLoading} = useLogin()
    const [isPassVisible, setIsPassVisible] = useState(false)
    const {handleSubmit, register} = useForm<IUser>()
    const onSubmit: SubmitHandler<IUser> = (data: IUser) => {
        getToken(data.username, data.password)
    }
    return (
        <>
            <form onSubmit={handleSubmit(onSubmit)}
                  className={"size-full flex flex-col items-center justify-around p-10 text-indigo-500"}>
                <h1 className={" surface font-bold text-3xl"}>Iniciar Sesión</h1>
                <div className={"w-2/3 space-y-4 translate-y-2"}>
                    <div className={'group'}>
                        <label className={'text-indigo-500 text-xs font-semibold invisible group-focus-within:visible opacity-0 group-focus-within:opacity-100 translate-y-5 group-focus-within:translate-y-0 transition-all'}>
                            Usuario
                        </label>
                        <input
                            {...register("username", {
                                required: "true"
                            })}
                            placeholder={"Usuario"}
                            type="text"
                            autoFocus={true}
                            className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}
                            />
                    </div>
                    <div className={'group'}>
                        <label className={'text-indigo-500 text-xs font-semibold opacity-0 invisible group-focus-within:visible group-focus-within:opacity-100 translate-y-5 group-focus-within:translate-y-0 transition-all'}>
                            Contraseña
                        </label>
                        <div className={"relative flex items-center"}>
                            <input placeholder={"Contraseña"} type={isPassVisible ? "text" : "password"}
                                   required={true}
                                   {...register("password", {
                                       required: "true",
                                   })}
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