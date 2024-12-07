import {Canvas} from "@react-three/fiber";
import {
    OrbitControls,
     SpotLight,
} from "@react-three/drei";
import Formulario from "./components/Formulario.tsx";
import Universitario from "./components/Universitario";

function LoginScreen() {

    return (
        <div className={'h-svh w-svw flex bg-gradient-to-br from-indigo-400 to-indigo-500 justify-center items-center'}>
            <div className={'h-3/4 w-3/4 bg-white shadow-lg shadow-indigo-600 flex rounded-lg'}>
                <div className={' w-1/2 bg-indigo-500 p-10'}>
                    <div className={'w-fit'}>
                        <h1 className={'text-white font-bold text-4xl'}>EduManager</h1>
                        <p className={'text-lg text-indigo-50 text-end'}>te da la bienvenida</p>
                    </div>
                    <div className={'w-full h-full '}>
                        <Canvas>
                            <SpotLight position={[0,10,0]} angle={10} intensity={200} distance={250}/>
                            <SpotLight position={[0,-10,0]} angle={10} intensity={200} distance={250}/>
                            <Universitario/>
                            <OrbitControls enableZoom={false}/>
                        </Canvas>
                    </div>



                </div>
                <div className={'h-full w-1/2'}>
                    <Formulario />
                </div>

            </div>

        </div>

    )
}

export default LoginScreen
