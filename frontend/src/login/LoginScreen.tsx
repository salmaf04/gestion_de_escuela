import {Canvas} from "@react-three/fiber";
import {
    PerspectiveCamera, SpotLight,
} from "@react-three/drei";
import {useEffect, useState} from "react";
import Universitario from "./components/Universitario";
import VisibilityOn from '/visibility-on.svg';
import VisibilityOff from '/visibility-off.svg';

interface User {
    username: string;
    password: string;
}


function LoginScreen() {
    const [user, setUser] = useState<User>({username: '', password: ''});
    useEffect(() => {
        console.log(user);
    }, [user]);
    const [isVisible, setIsVisible] = useState(false)

    return (
        <div className={'h-svh w-svw flex bg-indigo-50 justify-center items-center'}>
            <div className={'h-3/4 w-3/4 bg-white flex rounded-lg'}>
                <div className={' w-1/2 bg-blue-5'}>
                    <Canvas>
                        <SpotLight position={[0,10,0]} angle={10} intensity={200} distance={250}/>
                        <SpotLight position={[4,-2,4]} intensity={200} distance={250}/>
                        <PerspectiveCamera near={0.1}/>
                        {/*<OrbitControls/>*/}
                        <Universitario />
                        {/*<mesh>
                    <boxGeometry/>
                    <meshBasicMaterial color="hotpink"/>
                </mesh>*/}
                    </Canvas>
                </div>
                <form onSubmit={(e) => {
                    e.preventDefault();
                }
                } className={'h-full w-1/2 flex flex-col items-center justify-around p-10 text-indigo-400'}>
                    <h1 className={'text-indigo-400 surface font-bold text-4xl'}>Bienvenido</h1>
                    <div className={'w-2/3 space-y-8 translate-y-4'}>
                        <div>
                            <input
                                value={user.username}
                                placeholder={'Usuario'} type="text"
                                required={true}
                                className={'rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50'}
                                onChange={(newText)=>{setUser(prevState => {
                                    return {...prevState, username: newText.target.value}
                                })}}/>
                        </div>
                        <div className={'relative flex items-center'}>
                            <input placeholder={'Contraseña'} type={isVisible? 'text': 'password'}
                                   value={user.password}
                                   required={true}
                                   onChange={(newText)=>{setUser(prevState => {
                                       return {...prevState, password: newText.target.value}
                                   })}}
                                   className={' rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50'}/>
                            <img className={'absolute end-2 cursor-pointer '}
                                 alt={'Cambiar visibilidad'}
                                 onClick={
                                        (e) => {
                                            e.preventDefault();
                                            setIsVisible(!isVisible);
                                        }
                                 }
                                 src={isVisible? VisibilityOff: VisibilityOn}/>
                        </div>
                    </div>

                    <button
                        className={'bg-indigo-400 shadow-md shadow-indigo-300 transition-all text-indigo-50 font-semibold hover:scale-105 rounded-lg py-3 w-2/3 hover:bg-indigo-500'}
                        type={"submit"}
                        onSubmit={(e) => {
                            e.preventDefault();
                            console.log("Hola "+user.username);
                        }
                        }
                        >
                        Iniciar Sesión
                    </button>

                </form>
            </div>

        </div>

    )
}

export default LoginScreen
