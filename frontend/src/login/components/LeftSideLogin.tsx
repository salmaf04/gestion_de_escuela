import {Canvas} from "@react-three/fiber";
import {OrbitControls, SpotLight} from "@react-three/drei";
import Universitario from "./Universitario";

export default function LeftSideLogin(){
    return (
        <div className={'bg-indigo-500 p-10 size-full'}>
            <div className={'w-fit'}>
                <h1 className={'text-white font-bold text-4xl'}>EduManager</h1>
                <p className={'text-lg text-indigo-50 text-end'}>te da la bienvenida</p>
            </div>
            <div className={'w-full h-full '}>
                <Canvas>
                    <SpotLight position={[0, 10, 0]} angle={10} intensity={200} distance={250}/>
                    <SpotLight position={[0, -10, 0]} angle={10} intensity={200} distance={250}/>
                    <Universitario/>
                    <OrbitControls enableZoom={false}/>
                </Canvas>
            </div>
        </div>
    )
}