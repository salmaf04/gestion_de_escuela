
import Formulario from "./components/Formulario.tsx";



function LoginScreen() {

    return (
        <div className={'h-svh w-svw flex bg-gradient-to-br from-indigo-200 to-indigo-400 justify-center items-center'}>
            <div className={'h-3/4 w-3/4 bg-white shadow-lg shadow-indigo-400 flex rounded-lg'}>
                <div className={' w-1/2 bg-blue-5 p-2'}>
                    {/*<Canvas>
                        <SpotLight position={[0, 10, 0]} angle={10} intensity={200} distance={250}/>
                        <SpotLight position={[4, -2, 4]} intensity={200} distance={250}/>
                        <PerspectiveCamera near={0.1}/>
                        <OrbitControls/>
                        <Universitario/>
                    </Canvas>*/}
                    <img src={'/sign-in.jpg'} className={'h-full hue-rotate-15'} alt={'Imagen de login'}/>
                </div>
                <div className={'h-full w-1/2'}>
                    <Formulario />
                </div>

            </div>

        </div>

    )
}

export default LoginScreen
