import Navbar from "./components/Navbar.tsx";
import Sidebar from "./components/Sidebar.tsx";
import Content from "./components/Content.tsx";
import {useState} from "react";
import AddForm from "./components/AddForm.tsx";
import {header} from "./components/Example_data.tsx";

interface Props
{
    name : string
}



export default function LayoutScreen({name} : Props) {
    const [isFormVisible, setFormVisible] = useState(false);

    const handleAddButtonClick = () => {
        setFormVisible(true);
    };

    const handleCloseForm = () => {
        setFormVisible(false);
    };


    return (

        <div className={' bg-indigo-50'}>
            {isFormVisible && <AddForm onClose={handleCloseForm} />}
            <Navbar name={name}/>
            <div className={'flex'}>
                <Sidebar/>
                <Content setFormVisible={handleAddButtonClick}/>
            </div>
        </div>
    )
}
