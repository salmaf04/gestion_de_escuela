import Navbar from "./components/Navbar.tsx";
import Sidebar from "./components/Sidebar.tsx";
import Content from "./components/Content.tsx";
import {useState} from "react";
import AddForm from "./components/AddForm.tsx";


interface Props
{
    name : string
}



export default function LayoutScreen({name} : Props) {
    const [isAddFormVisible, setIsAddFormVisible] = useState(false);

    const handleAddButtonClick = () => {
        setIsAddFormVisible(true);
    };

    const handleCloseAddForm = () => {
        setIsAddFormVisible(false);
    };


    return (

        <div className={' bg-indigo-50'}>
            {isAddFormVisible && <AddForm onClose={handleCloseAddForm} />}
            <Navbar name={name}/>
            <div className={'flex'}>
                <Sidebar/>
                <Content setFormVisible={handleAddButtonClick}/>
            </div>
        </div>
    )
}
