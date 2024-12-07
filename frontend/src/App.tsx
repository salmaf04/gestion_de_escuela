import LoginScreen from "./login/LoginScreen.tsx";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import MainScreen from "./main/MainScreen.tsx";

function App() {

  return (
    <BrowserRouter>
        <Routes>
            <Route path={'/login'} element={<LoginScreen/>}/>
            <Route path={'/main'} element={<MainScreen />}/>
            <Route path={'*'} element={<Navigate to={"/login"} />}/>
        </Routes>

    </BrowserRouter>
  )
}

export default App
