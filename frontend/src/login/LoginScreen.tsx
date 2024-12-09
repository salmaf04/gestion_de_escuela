import Formulario from "./components/Formulario.tsx";
import LeftSideLogin from "./components/LeftSideLogin.tsx";

function LoginScreen() {

    return (
        <div className={'h-svh w-svw flex bg-gradient-to-br from-indigo-400 to-indigo-500 justify-center items-center'}>
            <div className={'h-3/4 w-3/4 bg-white shadow-lg shadow-indigo-600 flex rounded-lg'}>
                <div className={' w-1/2 h-full'}>
                    <LeftSideLogin />
                </div>
                <div className={'h-full w-1/2'}>
                    <Formulario />
                </div>

            </div>

        </div>

    )
}

export default LoginScreen
