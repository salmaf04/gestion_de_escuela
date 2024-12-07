import Navbar from "./components/Navbar.tsx";
import Sidebar from "./components/Sidebar.tsx";
import Content from "./components/Content.tsx";

interface Props
{
    name : string
}




export default function LayoutScreen({name} : Props) {
    return (

        <div className={' bg-indigo-50'}>
            <Navbar name={name}/>
            <div className={'flex'}>
                <Sidebar/>
                <Content/>
            </div>
        </div>
    )
}
